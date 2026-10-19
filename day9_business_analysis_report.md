
# Day 9: From Data Findings to Business Insights

## 1. Business Objective

Explore how topic-based sentiment analysis can support
cross-language content operations and user research.

The findings are exploratory and should not be treated as
direct measures of user preference or business performance.

## 2. Insight One: Daily Life

The positive sentiment share is 41.7% for English and 41.8%
for Spanish posts.

The difference is very small in this dataset.

Business action:
Use Daily Life as a comparison case and manually review examples
to check whether topic classification is consistent across languages.

Success measure:
The proportion of manually reviewed posts that match the intended topic.

## 3. Insight Two: Emotions

The positive sentiment share is 56.1% for English and 44.0%
for Spanish posts, a difference of 12.1 percentage points.

This is a descriptive difference. It does not establish a cultural
or linguistic cause.

Business action:
Review samples from both languages and compare model predictions
with manual sentiment labels.

Success measures:
Manual topic precision, sentiment classification accuracy, and
macro F1 by language.

## 4. Insight Three: Small Topic Groups

The English Food group has 14 topic matches, while the Spanish
Sports group has 16.

Small groups can produce unstable percentages.

Business action:
Review additional examples and collect more relevant observations
before making content strategy decisions.

Success measure:
The number of reviewed examples and the reliability of the estimates.

## 5. Recommendations for Content Operations

1. Validate topic labels before using topic-level sentiment results.
2. Monitor sentiment model performance separately by language.
3. Prioritize manual review where observed differences are large
   or sample sizes are small.
4. Avoid changing content strategy based on sentiment percentages alone.
5. Use additional engagement and business metrics before evaluating
   real content performance.

## 6. Limitations

- Topics are assigned using keyword rules and may be misclassified.
- Manual audits cover only a small sample.
- Some topic groups contain few observations.
- Model predictions may contain errors.
- The dataset may not represent all users or platforms.
- Observed differences do not establish causality.
- Sentiment is not the same as satisfaction, engagement, or conversion.

## 7. Conclusion

Topic-based sentiment analysis can help identify patterns for further
investigation. Its business value depends on reliable classification,
appropriate sample sizes, and validation against additional evidence.
The current results support exploratory analysis, not definitive
claims about user preferences or business outcomes.
