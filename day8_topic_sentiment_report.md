
# Day 8: Topic-Based Sentiment Analysis

## 1. Objective

This analysis compares sentiment distributions across five keyword-defined
topics in English and Spanish social media posts.

The five topics are Daily Life, Emotions, Entertainment, Food, and Sports.

## 2. Method

The analysis uses the existing topic labels and sentiment labels.

- 0 = Negative
- 1 = Neutral
- 2 = Positive

Posts without a matched topic are excluded.
Posts matching multiple topics are counted in each matched topic.
Percentages are calculated within each language-topic group.

A total of 1,362 unique posts have at least one matched topic.

## 3. Key Findings

### Daily Life

The sentiment distributions are very similar across the two languages.

- English: 29.1% negative, 29.2% neutral, 41.7% positive.
- Spanish: 29.1% negative, 29.1% neutral, 41.8% positive.

Positive sentiment is the largest category in both groups.

### Emotions

The positive sentiment share is 56.1% in English and 44.0% in Spanish.
The negative share is 30.4% in English and 32.7% in Spanish.

These are descriptive differences and do not establish why the distributions differ.

### Entertainment

English posts have 46.7% positive sentiment, while Spanish posts have
42.1% positive sentiment.

The Spanish Entertainment group is relatively small, with 38 topic matches,
so its percentages should be interpreted cautiously.

### Food

The English Food group contains only 14 matches. Its sentiment percentages
are therefore unstable and should not support strong conclusions.

The Spanish Food group contains 28 matches and has a 50.0% neutral share.

### Sports

English Sports posts have 38.0% positive sentiment and 23.3% negative sentiment.
Spanish Sports posts have 31.2% positive sentiment and 12.5% negative sentiment.

The Spanish Sports group is small, with 16 matches, so the apparent differences
require further validation.

## 4. Business Relevance

Topic-based sentiment analysis can help content teams identify patterns
that deserve further investigation.

For Global Content Operations, it can support exploratory monitoring of
content categories across languages.

For business trainee roles, it demonstrates the ability to summarize data,
compare groups, and communicate findings with appropriate caution.

These results do not directly measure user preferences, content performance,
or business impact.

## 5. Limitations

1. Topics are assigned using keyword rules and may be misclassified.
2. Manual validation covered only a small sample and does not measure recall.
3. Some topic groups have very few observations.
4. The dataset may not represent all English- or Spanish-speaking users.
5. Sentiment model errors may affect the observed distributions.
6. Differences are descriptive and do not establish causal or cultural explanations.
7. Posts matching multiple topics may be counted more than once across topics.

## 6. Next Steps

- Improve and validate topic classification.
- Review more examples from small topic groups.
- Compare model errors across languages and sentiment classes.
- Avoid making business recommendations without additional evidence.
