# Day 5: Official Test Set Evaluation

## 1. Objective

This analysis evaluates the sentiment classification model on the official test sets for English and Spanish. Unlike the earlier exploratory evaluation on the training data, the test set provides a more appropriate assessment of performance on held-out examples.

## 2. Test Set Overview

Each language contains 870 test examples, with 290 examples in each sentiment class: negative, neutral, and positive.

The test sets are balanced across the three classes, allowing macro F1 to provide a useful summary of performance across sentiment categories.

## 3. Overall Performance

| Language | Test Accuracy | Test Macro F1 |
|---|---:|---:|
| English | 73.22% | 0.7301 |
| Spanish | 69.66% | 0.6933 |

English performed better than Spanish on this test set. The accuracy difference was approximately 3.56 percentage points, while the macro F1 difference was 0.0368.

These results describe performance on this dataset. They do not establish that language or culture itself caused the difference.

## 4. Performance by Sentiment Class

| Language | Sentiment | Precision | Recall | F1 Score |
|---|---|---:|---:|---:|
| English | Negative | 0.72 | 0.88 | 0.79 |
| English | Neutral | 0.65 | 0.61 | 0.63 |
| English | Positive | 0.85 | 0.70 | 0.77 |
| Spanish | Negative | 0.70 | 0.80 | 0.75 |
| Spanish | Neutral | 0.62 | 0.55 | 0.58 |
| Spanish | Positive | 0.75 | 0.74 | 0.75 |

Neutral sentiment was the weakest category in both languages. Its F1 score was 0.63 for English and 0.58 for Spanish.

For English, negative sentiment had the highest recall (0.88), meaning that the model identified a relatively large share of actual negative examples. Positive sentiment had the highest precision (0.85), meaning that positive predictions were comparatively reliable.

For Spanish, negative sentiment also had the highest recall (0.80), while positive sentiment had the highest F1 score (0.75).

## 5. Training and Test Performance

| Language | Training Accuracy | Test Accuracy | Training Macro F1 | Test Macro F1 |
|---|---:|---:|---:|---:|
| English | 79.55% | 73.22% | 0.7938 | 0.7301 |
| Spanish | 81.84% | 69.66% | 0.8163 | 0.6933 |

Performance was lower on the test sets than on the training sets. The accuracy gap was 6.33 percentage points for English and 12.18 percentage points for Spanish.

This gap is a reason to investigate generalisation further, but it does not by itself prove overfitting. Differences in example difficulty or data distribution may also contribute.

## 6. Business and Risk Implications

- **Neutral sentiment is a priority for improvement.** Inaccurate neutral predictions may distort summaries of customer feedback when comments express mixed, weak, or unclear sentiment.
- **Performance should be monitored separately by language.** Aggregate metrics alone may conceal differences between language groups.
- **Human review may be useful for ambiguous cases.** In applications where sentiment labels inform business decisions, uncertain predictions should not automatically be treated as reliable evidence of customer opinion.

These are potential implications for sentiment-analysis workflows, not evidence that the model has caused real-world business harm.

## 7. Limitations

- The evaluation covers English and Spanish only.
- Each test set contains 870 examples from the selected dataset; results may not generalise to other platforms, topics, or time periods.
- Balanced class counts do not guarantee that the examples represent real-world sentiment distributions.
- The observed language difference does not establish a cultural explanation or prove model bias.
- Training-versus-test performance gaps alone are insufficient to diagnose the cause of lower test performance.

## 8. Conclusion

On the official test sets, the model achieved an accuracy of 73.22% for English and 69.66% for Spanish. Neutral sentiment was the weakest class in both languages, suggesting a clear direction for further error analysis and model improvement.

The main practical lesson is to evaluate performance by both language and sentiment class, rather than relying on a single overall accuracy score. Further testing on additional datasets would be needed before drawing broader conclusions about cross-language reliability.
