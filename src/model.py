import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Ensure folder exists
os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_csv("data/social_media_data.csv")

# Shuffle data (VERY IMPORTANT FIX)
df = df.sample(frac=1, random_state=42)

X = df["text"]
y = df["sentiment"]

# Correct TF-IDF (IMPORTANT FIX: include n-grams)
vectorizer = TfidfVectorizer(ngram_range=(1,2))

X_vec = vectorizer.fit_transform(X)

# Train model (better than Logistic Regression for small text data)
model = MultinomialNB()

model.fit(X_vec, y)

# Save BOTH together properly
joblib.dump(model, "models/sentiment_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model trained successfully!")