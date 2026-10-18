# Cross-Cultural AI Risk & Business Analytics

## Project Overview

This project investigates multilingual sentiment classification using English and Spanish social media text from the Cardiff NLP Tweet Sentiment Multilingual dataset.

The project combines exploratory data analysis, text-length comparison, sentiment classification evaluation, and error analysis to examine how model performance varies across languages and sentiment categories.

**Objective:** To demonstrate how data analysis and model evaluation can help identify reliability risks in multilingual AI applications.

## Key Findings

### 1. Exploratory Data Analysis

The English and Spanish training splits each contain 1,839 posts, with balanced negative, neutral, and positive labels.

| Metric | English | Spanish |
|---|---:|---:|
| Number of posts | 1,839 | 1,839 |
| Average text length | 109.57 characters | 83.39 characters |

English posts were longer on average in this sample. This is a descriptive observation and does not establish a causal linguistic or cultural explanation.

### 2. Official Test Set Evaluation

The model `cardiffnlp/twitter-xlm-roberta-base-sentiment` was evaluated on the dataset's official test splits.

| Metric | English | Spanish |
|---|---:|---:|
| Test set size | 870 | 870 |
| Accuracy | 73.22% | 69.66% |
| Macro F1-score | 0.7301 | 0.6933 |

English performed better than Spanish on these test sets, with an accuracy difference of 3.56 percentage points. This result describes performance on the selected data and does not establish that language or culture caused the difference.

### 3. Sentiment-Specific Performance

| Language | Negative F1 | Neutral F1 | Positive F1 |
|---|---:|---:|---:|
| English | 0.79 | 0.63 | 0.77 |
| Spanish | 0.75 | 0.58 | 0.75 |

Neutral sentiment was the weakest category in both languages. This highlights why overall accuracy alone may conceal important weaknesses in classification performance.

### 4. Model Performance Visualisation

**Performance comparison across languages**

![Model performance comparison](day3_model_comparison.png)

**Confusion matrices showing classification patterns**

![Confusion matrix](day3_confusion_matrix.png)

### 5. Error Analysis

Exploratory error analysis on the training splits found that neutral sentiment was frequently confused with negative or positive sentiment.

The three most common error types accounted for approximately 77.3% of all errors in that exploratory analysis. These results helped identify neutral sentiment as a priority for further investigation.

**Evaluation note:** Training-split error patterns and official test-set metrics are reported separately because they serve different purposes.

## Business and AI Risk Implications

- **Language-specific monitoring:** Evaluate model performance separately across languages instead of relying only on an overall score.
- **Category-level evaluation:** Monitor precision, recall, and F1-score for each sentiment category, especially neutral sentiment.
- **Human review:** Consider additional review for ambiguous comments or predictions used in high-impact business decisions.
- **Responsible interpretation:** Performance differences should trigger further investigation, not automatic conclusions about cultural differences or model bias.

These are potential implications for multilingual customer-feedback analysis; this project does not measure actual business harm.

## Dataset and Model

- **Dataset:** [Cardiff NLP — Tweet Sentiment Multilingual](https://huggingface.co/datasets/cardiffnlp/tweet_sentiment_multilingual)
- **Model:** `cardiffnlp/twitter-xlm-roberta-base-sentiment`
- **Languages:** English and Spanish
- **Sentiment labels:** Negative, Neutral, Positive
- **Tools:** Python, pandas, Matplotlib, Hugging Face Datasets, Hugging Face Transformers, scikit-learn

## Repository Contents

| File | Description |
|---|---|
| `day2_analysis.py` | Python script for exploratory data analysis |
| `day2_analysis_report.md` | Data-quality checks and descriptive findings |
| `text_length_comparison.png` | Text-length comparison visualization |
| `text_length_summary.csv` | Text-length summary statistics |
| `day3_error_summary.csv` | Exploratory error summary by language and sentiment |
| `day4_error_analysis_report.md` | Detailed analysis of common classification errors |
| `day5_test_set_comparison.csv` | Training-versus-test performance comparison |
| `day5_classification_report.csv` | Test-set metrics by language and sentiment |
| `day5_test_evaluation_report.md` | Detailed official test-set evaluation |

## Methods

1. Inspect dataset structure, label balance, missing values, and duplicate records.
2. Compare text-length statistics across languages and sentiment categories.
3. Evaluate sentiment classification using accuracy, macro F1, and class-level metrics.
4. Analyse confusion patterns to identify categories that require further investigation.
5. Translate evaluation findings into potential business and AI reliability implications.

## Limitations

- The analysis covers only English and Spanish from one dataset.
- Balanced sentiment labels may not represent real-world customer-feedback distributions.
- Training-split results are exploratory and should not be interpreted as independent test performance.
- Test-set results may not generalise to different platforms, topics, or time periods.
- The observed performance gap does not prove cultural causation or model bias.
- The project does not establish the cause of the training-versus-test performance gap.

## Reproducibility

The exploratory analysis script can be run in a Python environment with the required packages installed. The model evaluation was conducted using Hugging Face tools and scikit-learn.

For full reproducibility, the analysis environment, package versions, dataset version, and exact evaluation procedure should be documented.

## Data Attribution

Dataset: Cardiff NLP, *Tweet Sentiment Multilingual*. Consult the dataset card and applicable terms before redistributing data or derived content.
