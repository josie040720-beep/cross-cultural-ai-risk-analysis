
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

## Business Implications

The findings suggest several practical considerations for businesses developing or deploying multilingual AI systems.

1. **Language-specific evaluation:** English and Spanish posts showed different average text lengths in this dataset. Businesses should evaluate AI systems separately across languages rather than assuming that performance in one language guarantees similar performance in another.

2. **Fairness and risk monitoring:** Differences in text characteristics may affect how text-processing systems interpret user content. Teams should investigate whether sentiment classification errors vary by language before drawing conclusions about fairness or deploying a model at scale.

3. **Evidence-based decision-making:** Data analysis can help identify patterns that deserve further investigation. However, text length alone cannot establish sentiment accuracy, cultural differences, or unfair treatment. These questions require additional evaluation data and appropriate performance metrics.

4. **Business application:** For companies using multilingual sentiment analysis to monitor customer feedback, these findings support language-specific testing and ongoing quality monitoring before using model outputs to inform customer experience or business decisions.

### Recommended Next Steps

- Evaluate sentiment classification performance separately for English and Spanish using metrics such as precision, recall, and F1-score.
- Examine misclassified examples to identify potential language-specific error patterns.
- Compare results across additional languages and datasets before making broader claims.

## 7. Limitations

This analysis has several limitations:

- **Balanced sentiment labels:** Each language contains equal numbers of negative, neutral, and positive posts. This training sample does not represent the real-world distribution of sentiment.
- **Limited language coverage:** Only English and Spanish are analyzed, so the findings cannot be generalized to other languages.
- **Descriptive analysis only:** The results describe differences in text length but do not establish their causes or demonstrate cultural differences.
- **No model performance evaluation:** This analysis does not test a sentiment classifier, so it cannot determine whether classification accuracy or error rates differ between languages.
- **Dataset representativeness:** The sample may not reflect all social media users, platforms, or writing styles.

Future work should examine data quality, evaluate model performance separately by language, and investigate whether text length and informal expressions are associated with classification errors.

## 8. Next Steps

The next stage of this project will move from descriptive analysis to model evaluation.

1. **Evaluate model performance:** Use a sentiment classifier to generate predictions for English and Spanish posts, then compare precision, recall, and F1-score for each language.
2. **Investigate classification errors:** Examine misclassified posts to identify potential issues involving slang, informal expressions, and text length.
3. **Assess potential fairness risks:** Compare error rates across languages and sentiment categories before drawing conclusions about differences in model performance.
4. **Improve reproducibility:** Record the dataset version, code dependencies, and analysis steps. Review the dataset's licensing and attribution requirements before redistributing any data.

These steps would help determine whether the descriptive differences identified in Day 2 are associated with meaningful differences in sentiment classification performance.

## 9. Reproducibility

The analysis uses a public dataset and Python.
Record the code, dataset version, and analysis steps so the results
can be reproduced.

## 10. Data Citation

Barbieri, F., Anke, L. E., & Camacho-Collados, J. (2022). XLM-T: Multilingual Language Models in Twitter for Sentiment Analysis and Beyond. *Proceedings of the Thirteenth Language Resources and Evaluation Conference (LREC 2022)*.

Dataset: [Cardiff NLP - Tweet Sentiment Multilingual](https://huggingface.co/datasets/cardiffnlp/tweet_sentiment_multilingual)

The analysis uses the English and Spanish training splits. Please refer to the dataset card and original paper for dataset details, licensing information, and usage conditions.
