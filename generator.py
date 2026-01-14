from templates import get_base_sentence, get_detail_sentence
from nlp_keywords import extract_keywords_nlp
from nlp_sentiment import detect_sentiment_nlp
from datetime import datetime

REVIEW_FILE = "reviews.txt"

def save_review(topic, sentiment, length, review, confidence):
    with open(REVIEW_FILE, "a", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write(f"Time      : {datetime.now()}\n")
        f.write(f"Topic     : {topic}\n")
        f.write(f"Sentiment : {sentiment.capitalize()}\n")
        f.write(f"Confidence: {confidence}\n")
        f.write(f"Length    : {length}\n\n")
        f.write(review + "\n\n")

def main():
    print("=== NLP-Based Review Generator (CLI) ===")

    topic = input("Enter the topic to review: ").strip()
    if not topic:
        print("Topic cannot be empty.")
        return

    text = input("Describe your experience: ").strip()

    keywords = extract_keywords_nlp(text)
    sentiment, scores = detect_sentiment_nlp(text)

    print(f"\nDetected sentiment: {sentiment.capitalize()}")
    print(f"Sentiment confidence (compound score): {scores['compound']}")

    print("\nChoose review length:")
    print("1. Short\n2. Medium\n3. Long")
    length_choice = input("Enter choice: ").strip()

    length_map = {
        "1": ("Short", 1),
        "2": ("Medium", 3),
        "3": ("Long", 5)
    }

    if length_choice not in length_map:
        print("Invalid choice.")
        return

    length_label, detail_count = length_map[length_choice]

    sentences = [get_base_sentence(sentiment, topic)]
    for _ in range(detail_count):
        sentences.append(get_detail_sentence(keywords))

    review = " ".join(sentences)

    print("\n--- Generated Review ---")
    print(review)

    save_review(topic, sentiment, length_label, review, scores["compound"])
    print("\nReview saved successfully.")

if __name__ == "__main__":
    main()
