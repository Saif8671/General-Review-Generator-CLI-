from nlp_keywords import extract_keywords_nlp
from nlp_sentiment import detect_sentiment_nlp
from ai_generator import generate_review
from datetime import datetime

REVIEW_FILE = "reviews.txt"

def save_review(review):
    with open(REVIEW_FILE, "a", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write(f"{datetime.now()}\n")
        f.write(review + "\n\n")

def build_prompt(topic, sentiment, keywords, length):
    return (
        f"Write a {sentiment} review about {topic}. "
        f"Focus on the following aspects: {', '.join(keywords)}. "
        f"The review should be {length} and realistic.\n\nReview:"
    )

def main():
    print("=== Hybrid NLP + AI Review Generator ===")

    topic = input("Enter topic: ").strip()
    text = input("Describe your experience: ").strip()

    keywords = extract_keywords_nlp(text)
    sentiment, _ = detect_sentiment_nlp(text)

    print(f"\nDetected sentiment: {sentiment}")
    print(f"Extracted keywords: {keywords}")

    print("\nChoose length:")
    print("1. Short\n2. Medium\n3. Long")
    choice = input("Enter choice: ").strip()

    length_map = {
        "1": ("short", 80),
        "2": ("medium", 150),
        "3": ("long", 250)
    }

    if choice not in length_map:
        print("Invalid choice.")
        return

    length_label, max_len = length_map[choice]

    prompt = build_prompt(topic, sentiment, keywords, length_label)

    review = generate_review(prompt, max_len)

    print("\n--- Generated Review ---")
    print(review)

    save_review(review)
    print("\nReview saved successfully.")

if __name__ == "__main__":
    main()
