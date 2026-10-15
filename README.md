
# Cross-Cultural AI Risk & Business Analytics

## Project Overview

This project explores cross-cultural sentiment analysis using public multilingual social media data. It aims to investigate how language differences may affect text analysis and AI model evaluation.

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
