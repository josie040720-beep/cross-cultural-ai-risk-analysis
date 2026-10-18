# Day 6: Manual Audit of Keyword-Based Topic Classification

## 1. Objective

This analysis evaluates a simple keyword-based approach for identifying Daily Life and Sports content in English and Spanish social media posts.

The purpose of the manual audit is to check whether posts assigned to a topic are actually relevant to that topic.

## 2. Methodology

Topic labels were assigned using language-specific keyword lists and exact word-boundary matching.

A small sample of classified posts was then manually reviewed. Each reviewed post was assigned one of three labels:

- `yes`: The post is relevant to the assigned topic.
- `no`: The post is not relevant to the assigned topic.
- `uncertain`: The available text does not support a confident decision.

Only posts labelled `yes` or `no` were included in the precision calculation. Uncertain cases were excluded.

Precision was calculated as:

Precision = Relevant reviewed posts / All confirmed reviewed posts

## 3. Manual Audit Results

| Language | Topic | Confirmed Samples | Relevant | Irrelevant | Precision |
|---|---|---:|---:|---:|---:|
| English | Daily Life | 10 | 7 | 3 | 70.0% |
| English | Sports | 10 | 9 | 1 | 90.0% |
| Spanish | Daily Life | 9 | 9 | 0 | 100.0% |
| Spanish | Sports | 6 | 6 | 0 | 100.0% |
| **Overall** | **All audited groups** | **35** | **31** | **4** | **88.6%** |

One additional sample remained uncertain and was excluded from these calculations.

## 4. Key Findings

### English Daily Life

English Daily Life had a precision of 70.0% in the reviewed sample. Some posts matched the selected keywords but did not clearly describe everyday life. This suggests that the current keyword rules can produce false-positive classifications.

### English Sports

English Sports achieved 90.0% precision in the reviewed sample. However, the audit still identified an irrelevant match, showing that keyword matching does not always capture the meaning of a complete post.

### Spanish Topics

Both Spanish topic groups achieved 100.0% precision among the reviewed, confirmed samples. However, the sample sizes were small, especially for Sports. These results should not be interpreted as proof that the Spanish rules are more accurate than the English rules.

## 5. Limitations

- The manual audit covered only a small sample of classified posts.
- The reviewed samples may not represent all posts assigned to each topic.
- Some posts lacked sufficient context for a confident decision.
- Keyword matching identifies words, not the full meaning or intent of a post.
- This audit measures precision among reviewed classified posts. It does not measure recall, because posts not selected by the keyword rules were not systematically reviewed.
- The results do not establish cultural differences or user preferences between English- and Spanish-speaking groups.

## 6. Next Steps

Potential improvements include:

1. Reviewing more randomly selected classified posts.
2. Refining keywords that generate false positives.
3. Checking unclassified posts to estimate how much relevant content the rules miss.
4. Comparing the keyword approach with a more context-aware topic classification method.

## Conclusion

The manual audit provides an initial quality check for the keyword-based topic classification approach. The results highlight potential false positives, particularly in English Daily Life. Further review and validation are needed before using these topic labels for broader cross-language comparisons or business decisions.
