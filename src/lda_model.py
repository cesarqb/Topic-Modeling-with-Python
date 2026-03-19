import re
import string
from gensim.corpora import Dictionary
from gensim.models import LdaModel


def tokenize_text(text, stop_words):
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    tokens = re.split(r'\W+', text)
    tokens = [word for word in tokens if word not in stop_words and word != ""]
    return tokens


def build_dictionary(tokens):
    dictionary = Dictionary(tokens)
    dictionary.filter_extremes(
        no_below=2,
        no_above=0.9
    )
    return dictionary


def build_corpus(tokens, dictionary):
    corpus = [dictionary.doc2bow(doc) for doc in tokens]
    return corpus


def train_lda_model(corpus, dictionary, num_topics=20):
    lda = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        random_state=42,
        chunksize=1000,
        passes=10,
        alpha="auto"
    )
    return lda


def save_model(lda_model, dictionary, model_path, dict_path):
    lda_model.save(model_path)
    dictionary.save(dict_path)

    