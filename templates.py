import random

POSITIVE_TEMPLATES = [
    "Overall, my experience with {topic} has been excellent.",
    "{topic} exceeded my expectations.",
    "I am very satisfied with {topic}."
]

NEUTRAL_TEMPLATES = [
    "My experience with {topic} has been average.",
    "{topic} offers a fairly standard experience.",
    "Using {topic} felt acceptable overall."
]

NEGATIVE_TEMPLATES = [
    "My experience with {topic} was disappointing.",
    "{topic} did not meet my expectations.",
    "I was not satisfied with {topic}."
]

DETAIL_PHRASES = [
    "It performs well in areas such as {keywords}.",
    "Key aspects like {keywords} stand out.",
    "The handling of {keywords} could be improved.",
    "There is noticeable room for improvement in {keywords}.",
    "Overall usability around {keywords} varies."
]

def get_base_sentence(sentiment, topic):
    if sentiment == "positive":
        return random.choice(POSITIVE_TEMPLATES).format(topic=topic)
    elif sentiment == "neutral":
        return random.choice(NEUTRAL_TEMPLATES).format(topic=topic)
    elif sentiment == "negative":
        return random.choice(NEGATIVE_TEMPLATES).format(topic=topic)
    else:
        raise ValueError("Invalid sentiment")

def get_detail_sentence(keywords):
    joined_keywords = ", ".join(keywords) if keywords else "various aspects"
    return random.choice(DETAIL_PHRASES).format(keywords=joined_keywords)
