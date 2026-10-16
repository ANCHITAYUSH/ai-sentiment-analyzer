import streamlit as st
from sentiment import analyze_sentiment

st.set_page_config(
    page_icon="🤖",
    page_title="AI Sentiment Analyzer"
)

st.title("🤖 AI Sentiment Analyzer")

st.write(
    "Enter any English sentence and let AI "
    "predict its sentiment."
)

user_text = st.text_area(
    "Enter your text",
    placeholder="I love learning AI!"
)

if st.button("Analyze Sentiment"):

    if not user_text.strip():
        st.warning("Please enter some text.")

    else:
        with st.spinner("Analyzing..."):
            result = analyze_sentiment(user_text)

        sentiment = result["sentiment"]
        confidence = result["confidence"]

        if sentiment == "Positive":
            st.success(f"Positive 😊 — {confidence}%")

        elif sentiment == "Negative":
            st.error(f"Negative 😞 — {confidence}%")

        else:
            st.info(f"Neutral 😐 — {confidence}%")

        st.progress(min(confidence / 100, 1.0))