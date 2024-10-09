from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

vectorizer = TfidfVectorizer()
def tfidf(all_text):
    tfidf_matrix = vectorizer.fit_transform(all_text)
    return tfidf_matrix

def tfidf_job_description(processed_jd_str):
    tfidf_jd = vectorizer.transform([processed_jd_str])
    return tfidf_jd