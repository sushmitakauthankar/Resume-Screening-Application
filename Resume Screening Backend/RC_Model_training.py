import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.multiclass import OneVsRestClassifier
import pickle

def train_model(data_path):
    df = pd.read_csv(data_path)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['Resume'])

    label_encoder = LabelEncoder()
    label_encoder.fit(df['Category'])

    df['Category_ID'] = label_encoder.transform(df['Category'])

    X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix, df['Category_ID'], test_size=0.2, random_state=42)

    clf = OneVsRestClassifier(KNeighborsClassifier(n_neighbors=5))
    clf.fit(X_train, y_train)

    with open('tfidf.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    with open('clf.pkl', 'wb') as f:
        pickle.dump(clf, f)
    with open('label_encoder.pkl', 'wb') as f:
        pickle.dump(label_encoder, f)

    return clf, vectorizer, label_encoder
