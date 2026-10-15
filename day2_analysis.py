import pandas as pd
import matplotlib.pyplot as plt
import json
from huggingface_hub import hf_hub_download

# Download the English and Spanish training files
en_path = hf_hub_download(
    repo_id="cardiffnlp/tweet_sentiment_multilingual",
    filename="data/english/train.jsonl",
    repo_type="dataset"
)
es_path = hf_hub_download(
    repo_id="cardiffnlp/tweet_sentiment_multilingual",
    filename="data/spanish/train.jsonl",
    repo_type="dataset"
)

# Read JSONL files into pandas DataFrames
en_df = pd.read_json(en_path, lines=True)
es_df = pd.read_json(es_path, lines=True)

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
