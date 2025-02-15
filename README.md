Resume Classification & Ranking Model

Resume Classification & Ranking Model developed streamlines the recruitment process by automating the classification and ranking of resumes based on job descriptions using Natural Language Processing (NLP) and Machine Learning algorithms.

Features
- Resume Classification: Categorizes resumes into predefined job roles.
- Resume Ranking: Ranks resumes based on their relevance to a job description.
- Text Processing: Extracts, cleans, and tokenizes text from resumes and job descriptions.
- TF-IDF Vectorization: Converts text into numerical representations.
- Cosine Similarity: Measures the relevance of resumes to job descriptions.
- Interactive UI: Built using React.js, allowing easy file uploads and viewing of ranked results.

Technology Stack
Backend
- Python (Flask framework for API)
- NLTK (Natural Language Toolkit for text processing)
- Scikit-learn (Machine Learning algorithms like TF-IDF and KNN)
- Pandas & NumPy (Data processing)
- PyPDF2 & python-docx (Text extraction from resumes and job descriptions)

Frontend
- React.js (User Interface development)
- Figma (UI/UX design)

Workflow
1. Upload Resumes & Job Description
2. Text Extraction: Extract text from PDF/Word files
3. Text Cleaning & Preprocessing: Remove stopwords, punctuation, and irrelevant text
4. Feature Engineering: Convert text into TF-IDF vectors
5. Classification & Ranking:
   - KNN algorithm classifies resumes into categories
   - Cosine Similarity computes the match score between job descriptions and resumes
6. Result Visualization:
   - Ranked resumes displayed in a table
   - Pie chart showing resume category distribution
  ![image](https://github.com/user-attachments/assets/f2e7d19b-3876-4a1d-ae5c-e4a946703463)


     
Installation & Setup
Prerequisites
- Python 3.8+
- Node.js (for frontend)
- Flask & React installed
  
![image](https://github.com/user-attachments/assets/370f9c43-032f-48c8-8231-c67016192d02)

![image](https://github.com/user-attachments/assets/08678930-4b61-47ae-991c-69116bbfe248)

![image](https://github.com/user-attachments/assets/b74abdff-8d2f-45d1-a335-66a9e7e62d84)




