from templates import get_base_sentence, get_detail_sentence
from keyword_extractor import extract_keywords
from sentiment_detector import detect_sentiment
from datetime import datetime

REVIEW_FILE = "reviews.txt"

def save_review(topic, sentiment, length_label, review):
    with open(REVIEW_FILE, "a", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write(f"Time      : {datetime.now()}\n")
        f.write(f"Topic     : {topic}\n")
        f.write(f"Sentiment : {sentiment.capitalize()}\n")
        f.write(f"Length    : {length_label}\n\n")
        f.write(review + "\n\n")

def main():
    print("=== General Review Generator (CLI) ===")

    topic = input("Enter the topic to review: ").strip()
    if not topic:
        print("Error: Topic cannot be empty.")
        return

    raw_text = input("Enter your experience/description: ").strip()
    keywords = extract_keywords(raw_text)

    auto_sentiment = detect_sentiment(raw_text)
    print(f"\nAuto-detected sentiment: {auto_sentiment.capitalize()}")

    use_auto = input("Use auto-detected sentiment? (y/n): ").strip().lower()
    if use_auto == "y":
        sentiment = auto_sentiment
    else:
        print("\nChoose sentiment manually:")
        print("1. Positive\n2. Neutral\n3. Negative")
        choice = input("Enter choice (1/2/3): ").strip()
        sentiment_map = {"1": "positive", "2": "neutral", "3": "negative"}
        sentiment = sentiment_map.get(choice)
        if not sentiment:
            print("Invalid sentiment choice.")
            return

    print("\nChoose review length:")
    print("1. Short\n2. Medium\n3. Long")
    length_choice = input("Enter choice (1/2/3): ").strip()

    length_map = {
        "1": ("Short", 1),
        "2": ("Medium", 3),
        "3": ("Long", 5)
    }

    if length_choice not in length_map:
        print("Invalid length choice.")
        return

    length_label, detail_count = length_map[length_choice]

    sentences = [get_base_sentence(sentiment, topic)]
    for _ in range(detail_count):
        sentences.append(get_detail_sentence(keywords))

    review = " ".join(sentences)

    print("\n--- Generated Review ---")
    print(review)

    save_review(topic, sentiment, length_label, review)
    print("\nReview saved to reviews.txt")

if __name__ == "__main__":
    main()
