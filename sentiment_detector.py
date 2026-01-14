import re

POSITIVE_WORDS = {
    "good", "great", "excellent", "amazing", "useful", "easy",
    "fast", "smooth", "helpful", "positive", "satisfied", "love"
}

NEGATIVE_WORDS = {
    "bad", "poor", "slow", "difficult", "confusing", "buggy",
    "disappointing", "worst", "negative", "hate", "problem"
}

def detect_sentiment(text):
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    positive_score = sum(1 for w in words if w in POSITIVE_WORDS)
    negative_score = sum(1 for w in words if w in NEGATIVE_WORDS)

    if positive_score > negative_score:
        return "positive"
    elif negative_score > positive_score:
        return "negative"
    else:
        return "neutral"
