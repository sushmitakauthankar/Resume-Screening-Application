from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from .utils.Extraction import read
from .utils.Cleaning import clean
from .utils.Processing import process_text, save_tokens_to_csv
from .utils.RR_Cosine_similarities import similarity
from .utils.RR_tfidf import tfidf, tfidf_job_description
from .utils.RC_Model_training import train_model
from .utils.File_constant import f_const
from prettytable import PrettyTable
import pickle
import numpy as np

main = Blueprint('main', __name__)

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

job_description_data = None
resumes_data = []

# Load your vectorizer, classifier, and label encoder here
with open('tfidf.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('clf.pkl', 'rb') as f:
    clf = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

@main.route('/upload-job-description', methods=['POST'])
def upload_job_description():
    global job_description_data
    if 'file' not in request.files:
        return jsonify({"error": "Job description file is required"}), 400

    job_description_file = request.files['file']
    if job_description_file and allowed_file(job_description_file.filename):
        filename = secure_filename(job_description_file.filename)
        try:
            job_description_data = read(job_description_file)
        except Exception as e:
            print(f"Error reading job description file: {str(e)}")
            return jsonify({"error": "Error reading the job description file"}), 500

        return jsonify({"message": "Job description uploaded successfully"}), 200

    return jsonify({"error": "Invalid file format"}), 400

@main.route('/upload-resumes', methods=['POST'])
def upload_resumes():
    global resumes_data
    if 'files' not in request.files:
        return jsonify({"error": "Resume files are required"}), 400

    resume_files = request.files.getlist('files')
    resumes_data = []

    for resume_file in resume_files:
        if resume_file and allowed_file(resume_file.filename):
            filename = secure_filename(resume_file.filename)
            try:
                resume_text = read(resume_file)
                if resume_text:
                    resumes_data.append({
                        'filename': filename,
                        'content': resume_text
                    })
                else:
                    print(f"Warning: No content extracted from file {filename}")
            except Exception as e:
                print(f"Error processing resume file {filename}: {str(e)}")
                return jsonify({"error": f"Error processing file: {filename}"}), 500

    return jsonify({"message": "Resumes uploaded successfully"}), 200


import numpy as np

@main.route('/process', methods=['POST'])
def process_files():
    global job_description_data, resumes_data

    print("Processing files...")

    if not job_description_data:
        print("Job description data is missing or empty.")
        return jsonify({"error": "Job description is missing"}), 400

    if not resumes_data:
        print("Resumes data is missing or empty.")
        return jsonify({"error": "Resumes are missing"}), 400

    try:
        cleaned_jd = clean(job_description_data)
        processed_jd = process_text(cleaned_jd)
        save_tokens_to_csv(processed_jd.split())
    except Exception as e:
        print(f"Error processing job description file: {str(e)}")
        return jsonify({"error": "Error processing job description file"}), 500

    try:
        tokenized_resumes = []
        classification_results = {}

        for resume in resumes_data:
            cleaned_resume = clean(resume['content'])
            processed_resume = process_text(cleaned_resume)
            tokenized_resumes.append(processed_resume)

            input_features = vectorizer.transform([processed_resume])
            probabilities = clf.predict_proba(input_features)[0]
            top_two_indices = probabilities.argsort()[-2:][::-1]
            top_two_categories = label_encoder.inverse_transform(top_two_indices)
            top_two_probs = probabilities[top_two_indices]

            # Convert NumPy array to list
            top_two_probs = top_two_probs.tolist()
            top_two_categories = top_two_categories.tolist()

            # Ensure only top category is used if first probability is 1.00
            if top_two_probs[0] == 1.00:
                top_two_categories = [top_two_categories[0]]
                top_two_probs = [top_two_probs[0]]

            classification_results[resume['filename']] = {
                "categories": top_two_categories,
                "probabilities": top_two_probs
            }

    except Exception as e:
        print(f"Error processing resume files: {str(e)}")
        return jsonify({"error": "Error processing resumes"}), 500

    try:
        all_text = [processed_jd] + tokenized_resumes
        tfidf_matrix = tfidf(all_text)
        tfidf_jd = tfidf_job_description(processed_jd)
        tfidf_resumes = tfidf_matrix[1:]
        ranked_resumes = similarity(tfidf_jd, tfidf_resumes, [resume['filename'] for resume in resumes_data])
    except Exception as e:
        print(f"Error during TFIDF processing: {str(e)}")
        return jsonify({"error": "Error during TFIDF processing"}), 500

    combined_table = PrettyTable()
    combined_table.field_names = ["Rank", "Resume File", "Predicted Categories", "Probabilities", "Similarity Score"]

    results = []
    for rank, (resume, similarity_score) in enumerate(ranked_resumes, start=1):
        categories = classification_results.get(resume, {}).get("categories", ["Unknown", "Unknown"])
        probabilities = classification_results.get(resume, {}).get("probabilities", [0, 0])

        categories_str = ', '.join(categories)
        probabilities_str = ', '.join([f"{prob:.2f}" for prob in probabilities])

        combined_table.add_row([rank, resume, categories_str, probabilities_str, similarity_score])

        results.append({
            "rank": rank,
            "resume_file": resume,
            "predicted_categories": categories,
            "probabilities": probabilities,  
            "similarity_score": similarity_score
        })

    print(combined_table)
    return jsonify({"results": results}), 200



