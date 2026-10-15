
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

### Cross-Language Distribution Comparison

| Sentiment | English Count | Spanish Count | English % | Spanish % |
|---|---:|---:|---:|---:|
| Negative | 613 | 613 | 33.33% | 33.33% |
| Neutral | 613 | 613 | 33.33% | 33.33% |
| Positive | 613 | 613 | 33.33% | 33.33% |

The two training samples have identical sentiment label distributions. This reflects the balanced composition of the dataset and should not be interpreted as evidence that real-world sentiment distributions are identical across English- and Spanish-speaking populations.

## 5. Text Length Analysis

### Descriptive Results

English posts:

- Negative: mean 112.98 characters
- Neutral: mean 107.33 characters
- Positive: mean 108.39 characters

Spanish posts:

- Negative: mean 85.28 characters
- Neutral: mean 82.30 characters
- Positive: mean 82.59 characters

### Key Findings

In this sample, English posts are longer on average than Spanish posts across all three sentiment categories. Within each language, the differences in average text length between sentiment categories are relatively small compared with the overall difference between languages.

These findings are descriptive and do not establish that language itself causes differences in text length. Potential explanations, such as dataset collection methods, text preprocessing, and language-specific writing conventions, require further investigation.

### Implications for AI Risk

Text length may be a relevant factor when evaluating sentiment classification across languages. For example, a model may perform differently on short and long posts, or on posts containing slang, hashtags, and informal expressions.

However, this analysis does not measure model performance or demonstrate that either language has a higher classification error rate. Further testing is needed to determine whether text length is associated with classification errors across languages.

### Comparison by Sentiment Category

The average text length difference between English and Spanish posts was observed across all three sentiment categories:

- **Negative:** English posts were 27.69 characters longer on average.
- **Neutral:** English posts were 25.03 characters longer on average.
- **Positive:** English posts were 25.80 characters longer on average.

The differences were similar across sentiment categories. This suggests that the observed language-level difference in average text length is not limited to one sentiment category in this sample.

These results are descriptive. Further analysis is required to investigate possible explanations, including dataset construction, text preprocessing, and language-specific writing conventions.

## 6. Data Quality Checks

The English and Spanish training sets were checked for duplicate texts, missing values, and unexpected sentiment labels.

- **Duplicate texts:** No exact duplicate texts were found within either language dataset.
- **Missing values:** No missing values were found in the text or label columns.
- **Sentiment labels:** Both datasets contain the expected labels: 0 (negative), 1 (neutral), and 2 (positive).

These checks support the basic structural quality of the data. However, they do not verify the correctness of every sentiment label or rule out all possible data quality issues.

## 7. Limitations

This analysis has several limitations:

- **Balanced sentiment labels:** Each language contains equal numbers of negative, neutral, and positive posts. This training sample does not represent the real-world distribution of sentiment.
- **Limited language coverage:** Only English and Spanish are analyzed, so the findings cannot be generalized to other languages.
- **Descriptive analysis only:** The results describe differences in text length but do not establish their causes or demonstrate cultural differences.
- **No model performance evaluation:** This analysis does not test a sentiment classifier, so it cannot determine whether classification accuracy or error rates differ between languages.
- **Dataset representativeness:** The sample may not reflect all social media users, platforms, or writing styles.

Future work should examine data quality, evaluate model performance separately by language, and investigate whether text length and informal expressions are associated with classification errors.

## 8. Next Steps

- Check data quality and duplicate posts.
- Compare sentiment classification performance across languages.
- Evaluate whether text length affects model performance.
- Document dataset licensing and attribution before redistribution.

## 9. Reproducibility

The analysis uses a public dataset and Python.
Record the code, dataset version, and analysis steps so the results
can be reproduced.

## 10. Data Citation

Barbieri, F., Anke, L. E., & Camacho-Collados, J. (2022). XLM-T: Multilingual Language Models in Twitter for Sentiment Analysis and Beyond. *Proceedings of the Thirteenth Language Resources and Evaluation Conference (LREC 2022)*.

Dataset: [Cardiff NLP - Tweet Sentiment Multilingual](https://huggingface.co/datasets/cardiffnlp/tweet_sentiment_multilingual)

The analysis uses the English and Spanish training splits. Please refer to the dataset card and original paper for dataset details, licensing information, and usage conditions.
