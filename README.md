
# Cross-Cultural AI Risk & Business Analytics

## Project Overview

This project explores cross-cultural sentiment analysis using public multilingual social media data. It aims to investigate how language differences may affect text analysis and AI model evaluation.

## Key Findings

This project compares English and Spanish posts from the Cardiff NLP Tweet Sentiment Multilingual dataset to explore differences in text length across languages and sentiment categories.

- **Text length:** English posts had an average length of 109.57 characters, compared with 83.39 for Spanish posts.
- **Sentiment categories:** Negative posts were slightly longer on average than neutral and positive posts in both languages.
- **Data quality:** Both language datasets contained 1,839 posts, with balanced sentiment labels and no missing text or label values.
- **AI risk implications:** Differences in text length suggest that language-specific text characteristics should be considered when designing and evaluating multilingual sentiment analysis systems.

**Important limitation:** These are descriptive findings from this dataset. They do not establish that language or culture causes differences in writing style, nor do they measure sentiment model accuracy.

## Research Questions

- How does sentiment distribution differ across languages?
- Do text-length distributions vary between English and Spanish posts?
- How might language differences affect multilingual AI evaluation?
- What data-quality and evaluation risks should be considered?

## Dataset

**Source:** [Cardiff NLP — Tweet Sentiment Multilingual](https://huggingface.co/datasets/cardiffnlp/tweet_sentiment_multilingual)

The dataset contains social media text and three sentiment labels:

- `0`: Negative
- `1`: Neutral
- `2`: Positive

This project currently analyzes the English and Spanish training splits, with 1,839 posts per language.

## Preliminary Findings

- Both language subsets contain equal numbers of negative, neutral, and positive labels in the selected training split.
- English posts are longer on average than Spanish posts in this sample.
- These findings are descriptive and should not be interpreted as proof of causal cultural or linguistic differences.
- The balanced label distribution may not reflect real-world social media sentiment.

## Repository Contents

| File | Description |
|---|---|
| `day2_analysis.py` | Python analysis script |
| `day2_analysis_report.md` | Summary of data checks and findings |
| `text_length_comparison.png` | Comparison of text-length distributions |

## Methods

- Python and pandas for data inspection and summary statistics
- Matplotlib for visualization
- Hugging Face Datasets for data access

## Limitations and Next Steps

- Verify dataset version and licensing requirements.
- Check duplicates and data quality.
- Evaluate sentiment classification performance separately by language.
- Examine potential language-related performance gaps.
- Expand the analysis before drawing conclusions about cultural differences or business outcomes.

## Reproducibility

Run `day2_analysis.py` in a Python environment with the required packages installed. The script downloads the public dataset through Hugging Face Datasets.

## Data Attribution

Dataset: Cardiff NLP, *Tweet Sentiment Multilingual*.

Please consult the dataset card and the applicable Twitter/X terms before redistributing data or derived content.

## Day 3: Multilingual Sentiment Model Evaluation

### Objective
Evaluate a multilingual sentiment classification model on English and Spanish social media posts, compare performance across languages, and identify sentiment-specific classification errors.

### Model and Dataset
- **Dataset:** [Cardiff NLP Tweet Sentiment Multilingual](https://huggingface.co/datasets/cardiffnlp/tweet_sentiment_multilingual)
- **Model:** `cardiffnlp/twitter-xlm-roberta-base-sentiment`
- **Languages:** English and Spanish
- **Sample size:** 1,839 posts per language
- **Tools:** Python, Hugging Face Transformers, pandas, scikit-learn, Matplotlib

### Key Findings

| Metric | English | Spanish |
|---|---:|---:|
| Accuracy | 79.55% | 81.84% |
| Macro F1-score | 79.38% | 81.63% |

- Spanish achieved slightly higher accuracy and Macro F1-score in this evaluation.
- Neutral sentiment was the most difficult category to classify, with error rates of 31.00% for English and 30.34% for Spanish.
- Positive sentiment error rates were 21.21% for English and 13.54% for Spanish.
- Performance varied by sentiment category, showing why overall accuracy alone is insufficient for evaluating multilingual AI systems.

### Visual Results

**Model Performance Comparison**

![Model performance comparison](day3_model_comparison.png)

**Confusion Matrix**

![Confusion matrix](day3_confusion_matrix.png)

### Business Implications

Businesses using AI to analyse multilingual customer feedback should monitor model performance by both language and sentiment category. Misclassifying neutral feedback may distort customer satisfaction insights. Human review should be considered for ambiguous or high-impact decisions.

### Limitations

This is an exploratory evaluation using the dataset's training split, not an independent held-out test set. The results do not establish real-world generalisation, prove cultural differences, or independently demonstrate model bias. Further validation on independent data is needed.

### Project Files

- [`day3_model_evaluation_report.md`](day3_model_evaluation_report.md) — Detailed evaluation and business implications.
- [`day3_model_comparison.png`](day3_model_comparison.png) — Comparison of model performance across languages.
- [`day3_confusion_matrix.png`](day3_confusion_matrix.png) — Classification error patterns.
- [`day3_error_summary.csv`](day3_error_summary.csv) — Error rates by language and sentiment category.

