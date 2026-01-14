from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords_nlp(text, max_keywords=3):
    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 1)
    )

    tfidf_matrix = vectorizer.fit_transform([text])
    scores = tfidf_matrix.toarray()[0]
    terms = vectorizer.get_feature_names_out()

    ranked = sorted(
        zip(terms, scores),
        key=lambda x: x[1],
        reverse=True
    )

    keywords = [term for term, score in ranked[:max_keywords]]
    return keywords
