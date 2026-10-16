# AI Sentiment Analyzer

## Project Overview
A beginner-friendly AI web application that predicts whether English text expresses positive, negative, or neutral sentiment.

## Live Demo
[Try the AI Sentiment Analyzer](https://anchitguria-ai-sentiment-analyzer.streamlit.app/)

## Technologies Used
- Python
- Hugging Face Transformers
- PyTorch
- Streamlit

## Features
- Text sentiment classification
- Three sentiment categories
- Model confidence score
- Simple web interface

## Installation

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Start the application using `python -m streamlit run app.py`.

## Model
Uses `cardiffnlp/twitter-roberta-base-sentiment-latest`, a pretrained sentiment classification model.

## Limitations
Predictions may be inaccurate for sarcasm, ambiguous text, specialized language, and some languages other than English. Confidence is not the same as accuracy.
