from transformers import pipeline
from functools import lru_cache

@lru_cache(maxsize=1)
def load_model():
    # Load the model only once.
    return pipeline(
        task="text-classification",
        model="cardiffnlp/twitter-roberta-base-sentiment-latest"
    )

def analyze_sentiment(text):
    # Predicts the sentiment of given text

    if not text or not text.strip():
        raise ValueError("Please enter some text.")

    model = load_model()

    result = model(text, truncation=True)[0]

    return {
        "sentiment": result["label"].capitalize(),
        "confidence": round(result["score"] * 100, 2)
    }

if __name__ == "__main__":
    sentence = input("Enter your sentence: ")

    prediction = analyze_sentiment(sentence)

    print("Sentiment: ", prediction["sentiment"])
    print("Confidence: ", prediction["confidence"], "%")