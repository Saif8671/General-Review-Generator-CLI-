import random

POSITIVE_TEMPLATES = [
    "Overall, my experience with {topic} has been excellent. {detail} I would definitely recommend it.",
    "{topic} exceeded my expectations. {detail} The overall quality is impressive.",
    "I am very satisfied with {topic}. {detail} It delivers great value."
]

NEUTRAL_TEMPLATES = [
    "My experience with {topic} has been average. {detail} It works as expected, but nothing exceptional.",
    "{topic} offers a standard experience. {detail} There are both pros and cons.",
    "Using {topic} was neither particularly good nor bad. {detail} It meets basic requirements."
]

NEGATIVE_TEMPLATES = [
    "My experience with {topic} was disappointing. {detail} I expected better performance.",
    "{topic} did not meet my expectations. {detail} There are several areas that need improvement.",
    "I was not satisfied with {topic}. {detail} The overall experience was below average."
]

DETAIL_PHRASES = [
    "The functionality is straightforward.",
    "The design could be improved.",
    "Performance was inconsistent at times.",
    "The concept is good, but execution needs work.",
    "Ease of use varies depending on the situation."
]

def get_template(sentiment):
    if sentiment == "positive":
        return random.choice(POSITIVE_TEMPLATES)
    elif sentiment == "neutral":
        return random.choice(NEUTRAL_TEMPLATES)
    elif sentiment == "negative":
        return random.choice(NEGATIVE_TEMPLATES)
    else:
        raise ValueError("Invalid sentiment type")

def get_detail():
    return random.choice(DETAIL_PHRASES)
