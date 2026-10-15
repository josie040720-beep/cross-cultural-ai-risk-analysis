import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

# Load the public multilingual sentiment dataset
dataset = load_dataset("cardiffnlp/tweet_sentiment_multilingual")

# Analyze the English and Spanish training splits
en_df = dataset["english"]["train"].to_pandas()
es_df = dataset["spanish"]["train"].to_pandas()

label_names = {0: "Negative", 1: "Neutral", 2: "Positive"}

for language, df in [("English", en_df), ("Spanish", es_df)]:
    print(f"\n===== {language} =====")
    print("Number of posts:", len(df))
    print("\nSentiment distribution:")
    print(
        df["label"].map(label_names)
        .value_counts()
        .reindex(["Negative", "Neutral", "Positive"])
    )
    print("\nText length by sentiment:")
    df = df.copy()
    df["text_length"] = df["text"].str.len()
    print(
        df.groupby(df["label"].map(label_names))["text_length"]
        .agg(["count", "mean", "median"])
        .round(2)
    )

# Compare text length distributions
plt.figure(figsize=(10, 6))
plt.hist(en_df["text"].str.len(), bins=25, alpha=0.6, label="English")
plt.hist(es_df["text"].str.len(), bins=25, alpha=0.6, label="Spanish")
plt.xlabel("Text length (characters)")
plt.ylabel("Number of posts")
plt.title("Text Length Distribution by Language")
plt.legend()
plt.tight_layout()
plt.savefig("text_length_comparison.png", dpi=200)
plt.show()
