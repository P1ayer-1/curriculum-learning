import spacy
import markdown
import unicodedata
from selectolax.parser import HTMLParser
import torch
import json

# check if GPU is available and set spacy to use it if possible
if torch.cuda.is_available():
    print("GPU is available. Using GPU for spacy.")
else:
    print("GPU is not available. Using CPU for spacy.")

spacy.require_gpu()
# Load English NLP model
nlp = spacy.load(
    "en_core_web_trf",
    disable=["ner", "parser", "textcat"]
)


def normalize_text(text):
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("—", " ")
    text = text.replace("–", " ")
    return text

def strip_markdown(md: str) -> str:
    html = markdown.markdown(md)
    tree = HTMLParser(html)
    return tree.text()


import re

def is_valid_token(token):
    text = token.lemma_.lower()

    # Remove punctuation and spaces
    if token.is_punct or token.is_space:
        return False

    # Only alphabetic tokens
    if not token.is_alpha:
        return False

    # Remove stopwords (optional)
    if token.is_stop:
        return False

    # Remove short tokens
    if len(text) < 2:
        return False

    return True

def chunk_text(text, size=20000):
    return [text[i:i+size] for i in range(0, len(text), size)]

def extract_pos(text): # right now doesn't account for words that fall into multiple categories (e.g. "run" can be a noun or a verb). We could potentially add some logic to handle this in the future.
    """
    Extract nouns, verbs, and adjectives from text.
    """
    nouns, verbs, adjectives = set(), set(), set()  # Use sets to avoid duplicates
    chunks = chunk_text(text)

    for doc in nlp.pipe(chunks, batch_size=16):
        for token in doc:
            if not is_valid_token(token):
                continue
            if token.pos_ == "NOUN":
                nouns.add(token.lemma_)
            elif token.pos_ == "VERB":
                verbs.add(token.lemma_)
            elif token.pos_ == "ADJ":
                adjectives.add(token.lemma_)

    return list(nouns), list(verbs), list(adjectives)

def main():
    file_path = r"data_handling\process_books\input\anneofgreengables.txt"  # Replace with your file path

    # Read file
    with open(file_path, "r", encoding="utf-8") as file:
        raw_text = file.read()

    # Remove markdown
    clean_text = strip_markdown(raw_text)

    # Normalize text
    clean_text = normalize_text(clean_text)

    # Extract parts of speech
    nouns, verbs, adjectives = extract_pos(clean_text)

    print("Nouns:", nouns)
    print("Verbs:", verbs)
    print("Adjectives:", adjectives)

    # save as json
    output = {
        "nouns": nouns,
        "verbs": verbs,
        "adjectives": adjectives
    }
    with open(r"data_handling\process_books\output\anneofgreengables_lexicon.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    main()