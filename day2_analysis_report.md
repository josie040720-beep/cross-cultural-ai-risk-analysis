
# Day 2: Cross-Language Sentiment Analysis

## 1. Project Objective

Explore differences in sentiment classification and text length
between English and Spanish social media posts.

## 2. Dataset Source

Dataset: Cardiff NLP - Tweet Sentiment Multilingual
Source: https://huggingface.co/datasets/cardiffnlp/tweet_sentiment_multilingual

The dataset contains text and sentiment labels.

Label mapping:
- 0: Negative
- 1: Neutral
- 2: Positive

## 3. Data Used

- English training set: 1,839 posts
- Spanish training set: 1,839 posts
- Total: 3,678 posts

## 4. Sentiment Label Distribution

Each language contains:
- Negative: 613 posts (33.33%)
- Neutral: 613 posts (33.33%)
- Positive: 613 posts (33.33%)

Important limitation:
The sentiment labels are balanced in this training split.
This does not establish that real-world sentiment is equally distributed.

## 5. Text Length Analysis

English:
- Negative: mean 112.98 characters
- Neutral: mean 107.33 characters
- Positive: mean 108.39 characters

Spanish:
- Negative: mean 85.28 characters
- Neutral: mean 82.30 characters
- Positive: mean 82.59 characters

Preliminary observation:
English posts are longer on average than Spanish posts in this sample.
This is a descriptive finding, not proof that language itself causes
the difference.

## 6. Next Steps

- Check data quality and duplicate posts.
- Compare sentiment classification performance across languages.
- Evaluate whether text length affects model performance.
- Document dataset licensing and attribution before redistribution.

## 7. Reproducibility

The analysis uses a public dataset and Python.
Record the code, dataset version, and analysis steps so the results
can be reproduced.
