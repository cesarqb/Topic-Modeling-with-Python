import string
from nltk.corpus import stopwords

# stopwords en español
stop_words_sp = set(stopwords.words("spanish"))

def remove_punct(text):
    """
    Elimina signos de puntuación de un texto
    """
    text = "".join([char for char in text if char not in string.punctuation])
    return text


def remove_stopwords(text):
    """
    Elimina stopwords del texto
    """
    words = text.split()
    words = [word for word in words if word.lower() not in stop_words_sp]
    return " ".join(words)


def clean_text(text):
    """
    Pipeline básico de limpieza de texto
    """
    text = remove_punct(text)
    text = remove_stopwords(text)
    text = text.lower()
    return text