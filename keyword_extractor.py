import re

STOPWORDS = {
    "the", "is", "and", "a", "an", "to", "of", "in", "on", "for",
    "with", "this", "that", "it", "as", "was", "were", "are",
    "by", "from", "at", "be", "or"
}

def extract_keywords(text, max_keywords=3):
    words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())
    filtered = [w for w in words if w not in STOPWORDS]

    unique_keywords = []
    for word in filtered:
        if word not in unique_keywords:
            unique_keywords.append(word)
        if len(unique_keywords) == max_keywords:
            break

    return unique_keywords

