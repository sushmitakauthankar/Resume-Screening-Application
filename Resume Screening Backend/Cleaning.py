import re

def clean(text):
    """
    This function cleans a given text by removing URLs, certain abbreviations,
    non-alphanumeric characters, and extra whitespace.
    It uses regular expressions for these substitutions, replacing undesired patterns with spaces and trimming the result.

    :param text: It takes extracted text as parameter.

    :return: It returns cleaned text.
    """
    clean_text = re.sub('http\S+\s*', ' ', text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    clean_text = clean_text.lower()
    return clean_text