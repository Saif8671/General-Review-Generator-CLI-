from templates import get_template, get_detail

def main():
    print("=== General Review Generator (CLI) ===")
    topic = input("Enter the topic to review: ").strip()

    if not topic:
        print("Error: Topic cannot be empty.")
        return

    print("\nChoose sentiment:")
    print("1. Positive")
    print("2. Neutral")
    print("3. Negative")

    choice = input("Enter choice (1/2/3): ").strip()

    sentiment_map = {
        "1": "positive",
        "2": "neutral",
        "3": "negative"
    }

    sentiment = sentiment_map.get(choice)

    if not sentiment:
        print("Error: Invalid sentiment choice.")
        return

    template = get_template(sentiment)
    detail = get_detail()

    review = template.format(topic=topic, detail=detail)

    print("\n--- Generated Review ---")
    print(review)

if __name__ == "__main__":
    main()
