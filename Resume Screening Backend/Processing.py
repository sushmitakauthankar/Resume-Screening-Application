
import nltk
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from app.utils.File_constant import f_const

def process_text(text, lemmatize=False):
    """
    This function processes text by removing common stop words.
    It can also lemmatize words if specified.

    :param text: It takes a cleaned job description or resume as a parameter.
    :param lemmatize: Whether to lemmatize the words (default is False).

    :return: Returns the processed text.
    """
    stop_words = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(text)
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    if lemmatize:
        lemmatizer = nltk.WordNetLemmatizer()
        filtered_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return ' '.join(filtered_tokens)

def save_tokens_to_csv(tokens):

    """
    This function takes a list of tokens, counts their occurrences, and stores the results in a CSV file.
    It uses the `Counter` class from the `collections` module to count the frequency of each token,
    creates a DataFrame with the tokens and their frequencies,
    and saves the DataFrame to a CSV file at the specified path.

    :param tokens: It takes a list of filtered tokens as a parameter.

    :return: Null
    """
    word_counts = Counter(tokens)
    df = pd.DataFrame(word_counts.items(), columns=["Word", "Frequency"])
    output_file_path = r"C:\Users\kauth\PycharmProjects\ResumeRanking\Dataset\tokenized_jd\tokenized_words_frequency" + f_const + ".csv"
    df.to_csv(output_file_path, index=False)
