from transformers import T5Tokenizer, T5ForConditionalGeneration

model_name = "google/flan-t5-base"

tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def generate_review(topic, sentiment, keywords, length):
    length_map = {
        "short": "3-4 sentences",
        "medium": "5-6 sentences",
        "long": "8-10 sentences"
    }

    prompt = (
        f"Write a {sentiment} review about {topic}. "
        f"Focus on these aspects: {', '.join(keywords)}. "
        f"The review should be {length_map[length]} and realistic."
    )

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    output = model.generate(
        **inputs,
        max_length=256,
        temperature=0.8,
        do_sample=True
    )

    return tokenizer.decode(output[0], skip_special_tokens=True)
