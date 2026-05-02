# 📊 Social Media Sentiment Analysis Dashboard

## 🚀 Project Overview

This project is a Machine Learning-based Social Media Sentiment Analysis Dashboard that classifies text into Positive, Negative, or Neutral sentiments using Natural Language Processing (NLP).

It allows users to input social media text and get real-time sentiment predictions using a trained ML model with a Streamlit dashboard.

---

## 🎯 Problem Statement

Social media platforms generate huge amounts of text data daily. It is difficult for companies to manually analyze customer opinions.

This project solves this by automatically:
- Classifying sentiments
- Understanding customer feedback
- Helping business decision-making

---

## 💡 Real-World Applications

- Amazon / Flipkart reviews analysis
- Zomato / Swiggy feedback analysis
- Netflix user reviews
- Brand reputation monitoring
- Customer sentiment tracking

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLP (TF-IDF)
- Naive Bayes / ML Model
- Streamlit
- Joblib

---

## 🧠 Workflow

Raw Text → Cleaning → TF-IDF → Model Training → Prediction → Dashboard → Output

---
📁 PROJECT STRUCTURE
```text
Social-Media-Sentiment-Analysis-Dashboard/
│
├── app/
│   └── app.py                     → Streamlit Dashboard (User interface for sentiment prediction)
│
├── src/
│   ├── model.py                  → Trains ML model (TF-IDF + classifier)
│   ├── synthetic_dataset.py      → Creates and updates dataset CSV file
│
├── data/
│   └── social_media_data.csv     → Dataset containing text and sentiment labels
│
├── models/
│   ├── sentiment_model.pkl       → Saved trained ML model
│   ├── vectorizer.pkl            → Saved TF-IDF vectorizer
│
├── outputs/
│   └── predictions.csv           → Stores user inputs with predicted sentiment + timestamp
│
├── requirements.txt              → Lists required Python libraries
├── README.md                     → Project documentation
```




---

## ⚙️ Installation

```bash
git clone https://github.com/VinodhiniC1234/Social-Media-Sentiment-Analysis-Dashboard.git
cd Social-Media-Sentiment-Analysis-Dashboard
