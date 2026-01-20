# AI Review Generator (Hybrid NLP + FLAN-T5)

An intelligent web-based review generator that combines traditional NLP techniques with modern AI text generation using FLAN-T5. The system automatically detects sentiment, extracts keywords, controls review length, and generates realistic reviews through an intuitive web interface.

## Project Overview

This project demonstrates how NLP preprocessing and AI-based text generation can work together in a hybrid system. Users can now access the powerful review generation capabilities through a modern web interface instead of just the command line.

## Core Idea
User provides product/service details and experience → NLP analyzes the text for sentiment and keywords → AI generates a structured, realistic review

## Features

- **Web Interface** - Modern responsive UI with intuitive controls
- **Automatic Sentiment Detection** (Positive / Neutral / Negative)
- **Keyword Extraction** from user input
- **AI-Powered Review Generation** using **FLAN-T5**
- **Review Length Control** (Short / Medium / Long)
- **One-Click Copy** functionality
- **Real-time Processing** with loading indicators
- **Responsive Design** for desktop and mobile
- **Modular and Extensible** architecture

## Tech Stack

- **Backend**: Python 3.x, Flask
- **AI Model**: FLAN-T5 (google/flan-t5-base) via Hugging Face Transformers
- **NLP Libraries**: NLTK, TextBlob, scikit-learn
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Dependencies**: PyTorch, Transformers, Flask-CORS

## Project Structure

```
review-generator/ │ ├── app.py # Flask application (backend + frontend) ├── ai_generator.py # FLAN-T5 review generation ├── sentiment_detector.py # Auto sentiment detection ├── keyword_extractor.py # NLP keyword extraction ├── file_manager.py # Save reviews to file ├── templates/ │ └── index.html # Main web interface ├── static/ │ └── style.css # Styling for the web interface ├── data/ │ └── reviews.txt # Stored generated reviews │ ├── requirements.txt └── README.md```



## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/review-generator.git
   cd review-generator
```
Install Dependencies
```
pip install -r requirements.txt
```

How to Run
Start the Application

python app.py
Access the Web Interface Open your browser and navigate to:

## Generate Reviews

Select a product category
Enter product/service name
Describe your experience
Choose review length
Click "Generate Review"
Copy the generated review with one click
Generated Reviews
Reviews are automatically saved to:

data/reviews.txt

## Future Enhancements
- Add star rating prediction (1–5 stars)
-Implement multilingual review generation
- Add fine-tuning on custom review datasets
- Create Dockerized deployment
- Add user authentication and history
- Implement WebSocket for real-time updates
- Contributing
- Fork the repository
- Create a feature branch
- Commit your changes
- Push to the branch
- Create a Pull Request
- License
- This project is open-source and intended for educational purposes.

## License
This project is open-source and intended for educational purposes.