from templates import get_base_sentence, get_detail_sentence
from keyword_extractor import extract_keywords

def main():
    print("=== General Review Generator (CLI) ===")

    topic = input("Enter the topic to review: ").strip()
    if not topic:
        print("Error: Topic cannot be empty.")
        return

    raw_text = input("Enter a short description or experience: ").strip()
    keywords = extract_keywords(raw_text)

    print("\nChoose sentiment:")
    print("1. Positive")
    print("2. Neutral")
    print("3. Negative")
    sentiment_choice = input("Enter choice (1/2/3): ").strip()

    sentiment_map = {"1": "positive", "2": "neutral", "3": "negative"}
    sentiment = sentiment_map.get(sentiment_choice)

    if not sentiment:
        print("Error: Invalid sentiment choice.")
        return

    print("\nChoose review length:")
    print("1. Short")
    print("2. Medium")
    print("3. Long")
    length_choice = input("Enter choice (1/2/3): ").strip()

    length_map = {"1": 1, "2": 3, "3": 5}
    detail_count = length_map.get(length_choice)

    if not detail_count:
        print("Error: Invalid length choice.")
        return

    sentences = []
    sentences.append(get_base_sentence(sentiment, topic))

    for _ in range(detail_count):
        sentences.append(get_detail_sentence(keywords))

    review = " ".join(sentences)

    print("\n--- Generated Review ---")
    print(review)

if __name__ == "__main__":
    main()
