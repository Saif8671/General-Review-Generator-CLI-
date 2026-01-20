from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ai_generator import generate_review
from keyword_extractor import extract_keywords
from sentiment_detector import detect_sentiment
from file_manager import save_review

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate-review', methods=['POST'])
def generate_review_endpoint():
    try:
        data = request.json
        topic = data.get('topic', '')
        user_text = data.get('description', '')
        length = data.get('length', 'medium')
        
        if not topic or not user_text:
            return jsonify({'error': 'Missing topic or description'}), 400
        
        sentiment = detect_sentiment(user_text)
        keywords = extract_keywords(user_text)
        review = generate_review(topic, sentiment, keywords, length)
        
        save_review(review)
        
        return jsonify({
            'review': review,
            'sentiment': sentiment,
            'keywords': keywords
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
