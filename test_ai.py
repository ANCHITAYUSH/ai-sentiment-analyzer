from transformers import pipeline

analyzer = pipeline(
    task="text-classification",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

text = "I absolutely love learning artificial intelligence!"

result = analyzer(text)

print(result)

