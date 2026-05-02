import pandas as pd

data = {
    "text": [
        # POSITIVE (STRONG + WEAK VARIANTS)
        "I love this product",
        "I love this product so much",
        "This is absolutely amazing",
        "I am extremely happy with this service",
        "Best experience ever I really love it",
        "Fantastic product highly recommended",
        "Very good and I am satisfied",
        "Superb quality I love it",

        # NEGATIVE
        "I hate this product",
        "Worst experience ever",
        "Very bad quality and useless",
        "I am extremely disappointed",
        "Terrible service I hate it",
        "Not worth the money at all",
        "Very poor and frustrating",

        # NEUTRAL
        "It is okay not bad",
        "Average product nothing special",
        "It works fine",
        "Nothing great nothing bad",
        "Normal experience",
        "Product is fine"
    ],
    "sentiment": [
        "positive","positive","positive","positive","positive","positive","positive","positive",
        "negative","negative","negative","negative","negative","negative","negative",
        "neutral","neutral","neutral","neutral","neutral","neutral"
    ]
}

df = pd.DataFrame(data)
df.to_csv("data/social_media_data.csv", index=False)

print("Improved dataset created!")