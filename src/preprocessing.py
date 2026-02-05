import spacy
import nltk

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    sentences = nltk.sent_tokenize(text)
    doc = nlp(text)
    cleaned = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return sentences, cleaned