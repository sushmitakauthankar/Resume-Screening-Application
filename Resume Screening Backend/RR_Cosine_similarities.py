
from sklearn.metrics.pairwise import cosine_similarity

def similarity(tfidf_jd, tfidf_resumes, resume_files):
    cosine_similarities = cosine_similarity(tfidf_jd, tfidf_resumes)
    resume_scores = list(enumerate(cosine_similarities[0]))
    resume_scores.sort(key=lambda x: x[1], reverse=True)

    ranked_resumes = [(resume_files[index], f"{score:.4f}") for index, score in resume_scores]
    return ranked_resumes
