import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("models/sentiment_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# Title
st.title("📊 Social Media Sentiment Analysis Dashboard")

st.write("Enter any social media text below:")

# Input box
user_input = st.text_area("Type your text here")

# Button
if st.button("Predict Sentiment"):

    if user_input.strip() != "":

        # Convert text to numeric
        data = vectorizer.transform([user_input])

        # Predict
        prediction = model.predict(data)[0]

        # Output
        if prediction == "positive":
            st.success("😊 Positive Sentiment")
        elif prediction == "negative":
            st.error("😡 Negative Sentiment")
        else:
            st.info("😐 Neutral Sentiment")

    else:
        st.warning("Please enter some text!")