def save_review(review):
    with open("data/reviews.txt", "a", encoding="utf-8") as f:
        f.write(review + "\n\n")
