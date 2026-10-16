# Day 3: Multilingual Sentiment Model Evaluation

## 1. Project Objective

This analysis evaluates a multilingual sentiment classification model on English and Spanish social media posts. The objective is to compare its classification performance across the two languages, identify common prediction errors, and explore the implications for cross-cultural AI applications.

## 2. Dataset and Model

**Dataset:** Cardiff NLP Tweet Sentiment Multilingual  
**Dataset source:** https://huggingface.co/datasets/cardiffnlp/tweet_sentiment_multilingual

The analysis uses 1,839 English posts and 1,839 Spanish posts. Each language dataset contains 613 examples in each sentiment category:

- Negative
- Neutral
- Positive

**Model:** `cardiffnlp/twitter-xlm-roberta-base-sentiment`

The model was used to predict the sentiment of each post. Predictions were compared with the dataset's existing sentiment labels.

## 3. Evaluation Metrics

Two metrics were used:

- **Accuracy:** The proportion of all predictions that were correct.
- **Macro F1-score:** The average F1-score across the three sentiment categories, giving each category equal weight.

Macro F1 is useful because overall accuracy alone may hide differences in performance between sentiment categories.

## 4. Overall Results

| Metric | English | Spanish |
|---|---:|---:|
| Accuracy | 79.55% | 81.84% |
| Macro F1-score | 79.38% | 81.63% |

Spanish performance was higher than English performance in this evaluation. The accuracy difference was 2.29 percentage points, while the Macro F1 difference was 2.25 percentage points.

These results describe performance on the evaluated dataset. They do not establish that the model will perform better on all Spanish-language content or in real-world applications.

![Model performance comparison](day3_model_comparison.png)

## 5. Error Analysis by Sentiment

The error rate is calculated as the proportion of posts in each true sentiment category that the model classified incorrectly.

| Language | Sentiment | Correct Predictions | Total Posts | Error Rate |
|---|---|---:|---:|---:|
| English | Negative | 557 | 613 | 9.14% |
| English | Neutral | 423 | 613 | 31.00% |
| English | Positive | 483 | 613 | 21.21% |
| Spanish | Negative | 548 | 613 | 10.60% |
| Spanish | Neutral | 427 | 613 | 30.34% |
| Spanish | Positive | 530 | 613 | 13.54% |

Neutral sentiment had the highest error rate in both languages. This suggests that neutral posts may be harder for the model to distinguish from positive or negative content.

The positive sentiment error rate was lower for Spanish than for English in this evaluation. However, the negative sentiment error rate was slightly higher for Spanish.

These differences identify areas for further investigation. They do not, on their own, explain why the differences occurred.

## 6. Confusion Matrix Analysis

The confusion matrix compares the true sentiment labels with the model's predicted labels.

![Confusion matrix](day3_confusion_matrix.png)

The main observations are:

- **Negative sentiment:** The model correctly classified 557 English posts and 548 Spanish posts.
- **Neutral sentiment:** The model correctly classified 423 English posts and 427 Spanish posts. Many neutral posts were incorrectly classified as negative.
- **Positive sentiment:** The model correctly classified 483 English posts and 530 Spanish posts. English positive posts were more frequently misclassified as neutral than Spanish positive posts.

These patterns suggest that neutral sentiment and the distinction between neutral and negative content deserve further attention.

## 7. Business Implications

For businesses using AI to analyse customer feedback across languages, overall accuracy is not enough to assess whether a model is suitable for deployment.

First, neutral content deserves particular attention. If neutral feedback is incorrectly classified as negative, a business may overestimate customer dissatisfaction. If neutral feedback is incorrectly classified as positive, it may overlook concerns that require follow-up.

Second, performance should be monitored separately by language and sentiment category. A single overall score can hide important differences that affect customer-service decisions, brand monitoring, and market research.

Third, human review should be considered for ambiguous or high-impact cases. Model predictions should support decision-making rather than automatically determine important business actions.

## 8. Limitations

Several limitations should be considered:

1. **Evaluation design:** This analysis uses the dataset's training split rather than an independent held-out test set. The results should therefore be treated as exploratory, not as a definitive measure of generalisation to unseen data.
2. **Potential data overlap:** The model is trained for multilingual social media sentiment analysis. Possible overlap between its training data and the evaluation examples has not been independently verified.
3. **Limited language coverage:** Only English and Spanish were examined.
4. **Label limitations:** The analysis treats the dataset labels as reference labels. It does not independently verify every annotation.
5. **No causal conclusions:** Differences in model performance do not prove that language or culture caused those differences.
6. **No formal fairness test:** These results alone are insufficient to conclude that the model is biased or fair.

A stronger follow-up study should use a suitable held-out test set, inspect misclassified examples, and evaluate performance across additional languages and relevant content groups.

## 9. Conclusion

The multilingual sentiment model achieved 79.55% accuracy on the evaluated English posts and 81.84% on the evaluated Spanish posts. Neutral sentiment was the most challenging category in both languages.

The findings demonstrate the value of examining class-level errors alongside overall performance when evaluating AI systems for multilingual business applications.

The next stage of the project should focus on independent evaluation, error inspection, and practical recommendations for responsible cross-language AI use.
