
# Day 4: Error Analysis of Multilingual Sentiment Classification

## 1. Objective

This analysis examines sentiment classification errors in English and
Spanish text using the CardiffNLP multilingual sentiment model.

The objective is to identify common error patterns and discuss their
potential implications for business applications.

## 2. Dataset and Evaluation Scope

The analysis covers 3,678 posts: 1,839 English posts and 1,839
Spanish posts.

There are 710 incorrect predictions and 2,968 correct predictions,
giving an overall error rate of 19.30%.

Important limitation: these predictions were evaluated on the
dataset's training splits. The results are exploratory and should
not be interpreted as performance on unseen data.

## 3. Overall Error Patterns

The most frequent error patterns across both languages were:

- Neutral predicted as negative: 242 cases (34.1% of all errors).
- Positive predicted as neutral: 173 cases (24.4%).
- Neutral predicted as positive: 134 cases (18.9%).

Together, these three patterns account for 77.3% of all incorrect
predictions.

This suggests that many errors involve distinguishing neutral
sentiment from positive or negative sentiment.

## 4. Comparison Between Languages

### English

The most frequent error was neutral predicted as negative:
127 cases, accounting for 33.78% of English errors.

Positive predicted as neutral accounted for 28.72% of English errors.

### Spanish

The most frequent error was also neutral predicted as negative:
115 cases, accounting for 34.43% of Spanish errors.

Neutral predicted as positive accounted for 21.26% of Spanish errors,
while positive predicted as neutral accounted for 19.46%.

These differences describe the observed error distributions in this
dataset. They do not establish that language or culture caused the
differences.

## 5. Qualitative Error Inspection

A small sample of misclassified posts was inspected.

Some examples contained emotional words, references to future events,
or potentially ambiguous expressions. In other cases, the available
text was truncated or lacked context.

These observations suggest possible explanations, but they do not
establish the exact cause of each error. The original labels should
not be assumed to be wrong without further verification.

## 6. Potential Business Implications

In social media monitoring, neutral posts misclassified as negative
could lead to an overestimation of negative sentiment.

Positive posts misclassified as neutral could lead to an
underestimation of positive feedback.

Negative posts misclassified as positive could cause genuine
complaints to be overlooked.

These are potential risks inferred from the observed error types,
not measured real-world business outcomes.

## 7. Limitations

- The model was evaluated on the dataset's training splits.
- The qualitative review covered only a small sample of errors.
- Some text examples were truncated or context-dependent.
- Error patterns alone cannot establish cultural differences or
  model bias.
- Further evaluation on held-out data is needed.

## 8. Conclusion

The main observed challenge was distinguishing neutral sentiment
from other sentiment classes in both languages.

The language-specific error distributions differed in some respects,
but further testing is needed before drawing broader conclusions.

A useful next step is to evaluate the model on held-out data and
inspect a larger, systematically selected sample of errors.
