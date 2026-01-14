from ai_generator import generate_review
from keyword_extractor import extract_keywords
from sentiment_detector import detect_sentiment
from file_manager import save_review

topic = input("Enter product/service: ")
user_text = input("Describe your experience: ")
length = input("Review length (short/medium/long): ").lower()

sentiment = detect_sentiment(user_text)
keywords = extract_keywords(user_text)

review = generate_review(topic, sentiment, keywords, length)

print("\n--- Generated Review ---\n")
print(review)

save_review(review)
import re 