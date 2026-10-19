# Cross-Cultural AI Risk & Business Analytics

跨文化 AI 风险与商业分析项目

多语言数据分析： 基于英语和西班牙语社交媒体文本数据，使用 Python 进行数据清洗与探索性分析，对比不同语言文本的长度特征、情感分布及主题分布，识别多语言内容分析中的差异与共性。
情感分析与模型评估： 运用多语言情感分类模型开展文本情感识别，通过准确率、宏平均 F1 值、分类报告及混淆矩阵评估模型表现，发现中性情感是相对较难准确识别的类别。
主题分类与结果验证： 基于关键词规则构建内容主题分类方法，围绕日常生活、情绪、娱乐、食物及体育等主题进行分析，并对 35 条主题分类结果开展人工抽样核验，其中 31 条符合预设主题标准，样本核验准确率为 88.6%。
商业洞察与应用： 将数据分析结果转化为多语言内容运营建议，包括针对不同语言开展分类质量检查、重点关注模型易错类别，以及对小样本分析结果保持谨慎，避免将观察到的差异直接解释为文化差异或因果关系。

## Project Overview

This project explores multilingual sentiment analysis using English and Spanish social media text. It combines exploratory data analysis, AI model evaluation, error analysis, keyword-based topic classification, manual validation, and business insight development.

The goal is to understand how sentiment classification performs across languages, identify potential reliability issues, and explore how multilingual text analysis can support content operations and business research.

**Project focus:** Multilingual AI evaluation, cross-cultural content analysis, and business insights.

**Tools:** Python, pandas, matplotlib, scikit-learn, Google Colab, GitHub.

## Business Value

This project demonstrates how data analysis and multilingual AI evaluation can support exploratory content research.

Key capabilities demonstrated:

- **Data analysis:** Compared text characteristics and sentiment distributions across English and Spanish datasets.
- **AI evaluation:** Evaluated classification performance using accuracy, macro F1-score, and class-level metrics.
- **Quality assurance:** Investigated classification errors and manually audited keyword-based topic labels.
- **Business insights:** Identified patterns requiring further investigation and proposed validation steps for content operations.

The results are exploratory. They do not establish cultural causes, actual user preferences, or measurable business impact.

## Project Workflow

1. Explore and compare English and Spanish datasets.
2. Analyse text length and sentiment label distributions.
3. Evaluate multilingual sentiment classification performance.
4. Investigate model errors and class-level performance.
5. Assign topics using keyword-based rules.
6. Manually audit a sample of topic assignments.
7. Compare sentiment distributions across topics and languages.
8. Translate data findings into cautious, actionable business recommendations.

## Key Findings

### 1. Dataset

The training split contains 1,839 English posts and 1,839 Spanish posts. Each language has 613 examples for each of the three sentiment labels.

The official test split contains 870 examples for each language.

Sentiment labels:

- `0`: Negative
- `1`: Neutral
- `2`: Positive

The balanced training labels are useful for comparing model performance, but they do not necessarily reflect real-world sentiment distributions.

### 2. Text Length Comparison

Average text length in the training data:

- English: 109.57 characters
- Spanish: 83.39 characters
- Difference: 26.18 characters

This is a descriptive difference in the sampled text. It does not establish why the difference exists or imply that one language communicates more effectively than the other.

![Text length comparison](text_length_comparison.png)

### 3. Sentiment Model Evaluation

Model: `cardiffnlp/twitter-xlm-roberta-base-sentiment`

Official test-set results:

| Metric | English | Spanish |
|---|---:|---:|
| Accuracy | 0.7322 | 0.6966 |
| Macro F1-score | 0.7301 | 0.6933 |

In this evaluation, the model performs better on the English test split than on the Spanish test split. This is a result for these particular datasets, not proof of a general performance gap across all English and Spanish content.

Class-level test-set F1-scores:

| Sentiment | English F1 | Spanish F1 |
|---|---:|---:|
| Negative | 0.79 | 0.75 |
| Neutral | 0.63 | 0.58 |
| Positive | 0.77 | 0.75 |

Neutral sentiment has the lowest F1-score in both languages, making it a useful priority for further error analysis.

### 4. Model Performance Visualisation

#### Performance Comparison Across Languages

![Model performance comparison](day3_model_comparison.png)

#### Confusion Matrices

![Confusion matrices](day3_confusion_matrix.png)

These visualisations help compare model performance and identify patterns in classification errors.

## Error Analysis

The project examines classification errors by language and sentiment class.

The results suggest that neutral sentiment is more difficult for the model to classify than negative or positive sentiment in the official test evaluation.

This matters for content analysis because sentiment predictions may be less reliable for ambiguous or neutral posts. Predicted labels should not be treated as verified user opinions without additional validation.

See:

- `day3_error_summary.csv`
- `day4_error_analysis_report.md`
- `day5_test_evaluation_report.md`
- `day5_test_set_comparison.csv`
- `day5_classification_report.csv`

## Topic Analysis and Manual Validation

Keyword-based rules were used to assign posts to five exploratory topics:

- Daily Life
- Emotions
- Entertainment
- Food
- Sports

The project compares the original keyword-based topic distribution with a refined set of rules for selected topics.

The refined rules reduce the number of matches for Daily Life and Sports. A lower match count does not, by itself, prove that classification quality improved.

### Manual Audit Results

A small sample of topic assignments was manually reviewed.

| Language and Topic | Reviewed | Relevant | Precision |
|---|---:|---:|---:|
| English — Daily Life | 10 | 7 | 70.0% |
| English — Sports | 10 | 9 | 90.0% |
| Spanish — Daily Life | 9 | 9 | 100.0% |
| Spanish — Sports | 6 | 6 | 100.0% |
| **Total** | **35** | **31** | **88.6%** |

One uncertain case was excluded from the precision calculation.

These results are based on small samples. In particular, the 100% precision figures for Spanish topics should not be interpreted as proof of perfect classification. The audit also does not measure recall, so it cannot tell us how many relevant posts the keyword rules missed.

Related files:

- `topic_manual_audit_labeled.csv`
- `day6_topic_audit_report.md`
- `day7_topic_distribution_original.png`
- `day7_topic_distribution_original.csv`
- `day7_manual_audit_precision.png`

## Day 8: Topic-Based Sentiment Analysis

Sentiment distributions were compared across the five topics for English and Spanish posts.

A total of 1,362 unique posts had at least one matched topic. Posts without a topic match were excluded. Posts matching multiple topics were counted in each matching topic, so topic counts should not be added together as if every post belonged to exactly one topic.

### Daily Life

The positive sentiment shares were very similar:

- English: 41.7%
- Spanish: 41.8%

This is a descriptive similarity within the current dataset. It does not prove that user preferences are the same across languages.

### Emotions

The positive sentiment shares were:

- English: 56.1%
- Spanish: 44.0%

The difference is 12.1 percentage points. This is a pattern worth investigating, not evidence of a cultural or linguistic cause.

Further checks should examine topic classification quality, manually reviewed examples, and sentiment model errors.

### Small Topic Groups

Some groups contain few matches, including English Food and Spanish Sports. Their percentages may be unstable and should not be used alone to justify content strategy decisions.

### Sentiment Distribution Charts

#### English

![English topic sentiment distribution](day8_sentiment_distribution_english.png)

#### Spanish

![Spanish topic sentiment distribution](day8_sentiment_distribution_spanish.png)

Related files:

- `day8_topic_sentiment_report.md`
- `day8_topic_sentiment_counts.csv`
- `day8_topic_sentiment_percentages.csv`

## Day 9: Business Insights

The analysis translates descriptive findings into possible next steps for content operations and multilingual AI evaluation.

### Insight 1: Use Daily Life as a Comparison Case

The English and Spanish positive sentiment shares are nearly identical in this sample.

**Suggested action:** Review examples from both languages to check whether the topic definitions are applied consistently.

### Insight 2: Investigate the Emotions Difference

The positive sentiment share differs by 12.1 percentage points between the two language groups.

**Suggested action:** Manually review examples and compare model errors before proposing explanations or changing content decisions.

### Insight 3: Be Cautious with Small Samples

Some topic groups contain very few matched posts.

**Suggested action:** Review additional examples or collect more relevant observations before drawing strong conclusions.

### Potential Business Applications

For content operations, topic-based sentiment analysis may help teams identify categories that warrant further review.

For multilingual AI quality assurance, it can help identify where model evaluation and manual checks should be prioritised.

These applications remain exploratory. The current project does not measure actual engagement, satisfaction, conversion, or business impact.

Related files:

- `day9_business_insights.csv`
- `day9_business_analysis_report.md`

## Repository Contents

| File | Description |
|---|---|
| `README.md` | Project overview, findings, and limitations |
| `day2_analysis.py` | Exploratory analysis code |
| `day2_analysis_report.md` | Exploratory analysis report |
| `text_length_summary.csv` | Text length summary statistics |
| `text_length_comparison.png` | Text length comparison chart |
| `day3_error_summary.csv` | Model error summary |
| `day3_model_comparison.png` | Model performance comparison chart |
| `day3_confusion_matrix.png` | Confusion matrix visualisation |
| `day4_error_analysis_report.md` | Error analysis report |
| `day5_test_set_comparison.csv` | Test-set comparison results |
| `day5_classification_report.csv` | Classification metrics by class |
| `day5_test_evaluation_report.md` | Official test-set evaluation report |
| `topic_manual_audit_labeled.csv` | Manually reviewed topic assignments |
| `day6_topic_audit_report.md` | Topic audit report |
| `day7_topic_distribution_original.png` | Topic distribution under original keyword rules |
| `day7_manual_audit_precision.png` | Manual audit precision chart |
| `day7_topic_distribution_original.csv` | Topic counts under original keyword rules |
| `day8_topic_sentiment_report.md` | Topic-based sentiment analysis report |
| `day8_sentiment_distribution_english.png` | Topic-level sentiment chart for English |
| `day8_sentiment_distribution_spanish.png` | Topic-level sentiment chart for Spanish |
| `day8_topic_sentiment_counts.csv` | Sentiment counts by language and topic |
| `day8_topic_sentiment_percentages.csv` | Sentiment percentages by language and topic |
| `day9_business_insights.csv` | Summary of business findings and next steps |
| `day9_business_analysis_report.md` | Business recommendations and limitations |

## Methods

The project uses Python and pandas for data processing, matplotlib for visualisation, and scikit-learn metrics for model evaluation.

The analysis includes:

- Descriptive statistics
- Accuracy and macro F1-score
- Class-level classification metrics
- Confusion matrix and error analysis
- Keyword-based topic assignment
- Manual precision audit
- Topic-level sentiment distributions

## Limitations

1. The dataset may not represent all English- or Spanish-speaking users.
2. Balanced training labels do not necessarily reflect real-world sentiment prevalence.
3. Model predictions may contain errors, especially for neutral sentiment.
4. Keyword-based topic rules may produce false positives and miss relevant posts.
5. Manual validation covered only a small sample and did not measure recall.
6. Some topic groups contain few observations.
7. Posts may match multiple topics, resulting in repeated counts across topic groups.
8. Observed language differences do not establish cultural causes.
9. Sentiment distributions are not direct measures of user preferences or business performance.
10. The analysis is exploratory and requires further validation before operational decisions.

## Reproducibility

The project was developed using Python in Google Colab. Analysis outputs and reports are stored in this repository.

To reproduce the analysis, use the corresponding scripts or notebooks and ensure that the dataset and model are available. Dataset and model access may require following their original hosting instructions.

## Conclusion

This project demonstrates an end-to-end workflow for exploratory multilingual text analysis: from data exploration and model evaluation to error investigation, topic validation, and business insight development.

The key lesson is that useful AI analysis requires more than model scores. Reliable interpretation also depends on data quality, classification validation, sample size, and clear communication of uncertainty.

# 跨文化 AI 风险与商业分析

**项目方向：** 多语言文本分析、情感分析、内容分类、用户洞察

**项目工具：** Python、Pandas、Scikit-learn、Matplotlib、预训练多语言情感分类模型

**项目链接：** [GitHub 项目仓库](https://github.com/josie040720-beep/cross-cultural-ai-risk-analysis)

## 一、项目简介

本项目基于英语和西班牙语社交媒体文本数据，使用 Python 开展多语言文本分析、情感分类、主题识别与结果验证。

项目主要研究以下问题：

1. 英语与西班牙语社交媒体文本在长度等特征上是否存在差异？
2. 多语言情感分类模型在不同语言和不同情感类别上的表现如何？
3. 如何利用关键词规则识别社交媒体内容主题？
4. 如何验证自动分类结果，并将分析发现转化为内容运营和用户洞察建议？

项目不仅关注模型的分类结果，也关注数据质量、分类可靠性及分析结论的适用范围。

## 二、项目数据

### 2.1 数据来源

本项目使用 Cardiff NLP 发布的多语言推文情感数据集。

数据包含英语和西班牙语文本，情感标签分为三类：

| 标签 | 含义 |
|---|---|
| 0 | 负面情感 |
| 1 | 中性情感 |
| 2 | 正面情感 |

训练集与测试集分别用于不同阶段的分析和评估。

### 2.2 数据特点

- 分析对象为英语和西班牙语社交媒体文本。
- 训练集的两种语言各包含 1,839 条文本，三类情感标签数量均衡。
- 项目对不同语言的文本特征、情感分类表现及内容主题进行比较。

需要注意，训练集的类别均衡并不代表真实社交媒体环境中的情感分布也同样均衡。

## 三、项目分析流程

```text
数据读取与整理
      ↓
文本特征分析
      ↓
多语言情感分类与模型评估
      ↓
分类错误分析
      ↓
基于关键词的主题识别
      ↓
人工抽样核验
      ↓
主题与情感分布分析
      ↓
形成业务洞察与改进建议
```

## 四、主要分析结果

### 4.1 多语言文本特征分析

项目比较了英语与西班牙语文本的长度特征。

| 指标 | 英语 | 西班牙语 |
|---|---:|---:|
| 平均文本长度（字符） | 109.57 | 83.39 |

英语文本的平均长度比西班牙语文本高 26.18 个字符，约高 31.39%。

这一结果说明，在当前数据集中，两种语言的文本长度存在明显差异。该差异可能与语言表达方式、数据来源或样本构成有关，不能仅凭这一结果直接判断其原因。

### 4.2 多语言情感分类模型评估

项目使用多语言情感分类模型，对英语和西班牙语测试集进行评估。

测试集评估结果如下：

| 评估指标 | 英语 | 西班牙语 |
|---|---:|---:|
| 准确率 | 73.22% | 69.66% |
| 宏平均 F1 值 | 0.7301 | 0.6933 |

其中：

- **准确率**反映模型整体预测正确的比例。
- **宏平均 F1 值**先分别计算各情感类别的 F1 值，再进行平均，能够帮助评估模型在不同类别上的综合表现。

从当前测试结果看，模型在英语测试集上的整体表现优于西班牙语测试集，但这一结果仅适用于本项目所使用的数据和评估设置。

### 4.3 不同情感类别的识别表现

测试集分类结果显示，中性情感是相对较难识别的类别。

| 语言 | 负面情感 F1 值 | 中性情感 F1 值 | 正面情感 F1 值 |
|---|---:|---:|---:|
| 英语 | 0.79 | 0.63 | 0.77 |
| 西班牙语 | 0.75 | 0.58 | 0.75 |

中性情感的 F1 值低于另外两类情感，说明模型在区分中性表达时面临更大挑战。

这一发现对内容分析具有实际意义：如果运营团队依赖自动情感分类结果，就应重点检查中性内容的识别质量，避免直接将模型预测结果视为真实用户态度。

## 五、内容主题分类与人工核验

### 5.1 主题分类方法

项目采用基于关键词的规则，对文本进行初步主题识别，主题包括：

- 日常生活
- 情绪表达
- 娱乐
- 食物
- 体育

关键词规则实现简单、容易解释，适合用于初步探索。但由于文本表达丰富，同一个词可能出现在不同语境中，因此关键词匹配不一定等同于真正理解文本主题。

### 5.2 人工抽样核验

为了检查主题分类结果的可靠性，项目对部分分类结果进行了人工抽样核验。

| 核验项目 | 数量 |
|---|---:|
| 人工核验文本 | 35 条 |
| 符合预设主题的文本 | 31 条 |
| 不符合预设主题的文本 | 4 条 |
| 样本核验准确率（符合比例） | 88.6% |

本次核验中，31 条文本符合预设主题标准，35 条样本中的符合比例为 88.6%。

需要注意，该指标仅反映本次人工核验样本的结果，不能直接代表整个数据集的分类准确率，也不能说明所有主题的分类效果都相同。

此外，人工抽样核验主要用于检查分类结果的准确性，尚不能充分衡量关键词规则漏掉了多少真正相关的文本。

## 六、主题与情感分布分析

在主题识别的基础上，项目进一步分析了不同语言、不同内容主题下的情感分布。

分析时，同一条文本可能同时匹配多个主题，因此各主题的样本数量不能简单相加并视为独立文本总量。

### 6.1 英语文本的观察结果

- 日常生活主题中，正面情感占 41.7%，负面情感占 29.1%，中性情感占 29.2%。
- 情绪表达主题中，正面情感占 56.1%，在该主题的三类情感中比例最高。
- 娱乐主题中，正面情感占 46.7%，中性情感占 30.7%。
- 体育主题中，中性情感占 38.8%，高于负面情感和正面情感。

### 6.2 西班牙语文本的观察结果

- 日常生活主题中，正面情感占 41.8%，负面情感与中性情感均占 29.1%。
- 情绪表达主题中，正面情感占 44.0%。
- 娱乐主题中，中性情感占 50.0%。
- 食物主题中，中性情感占 50.0%，正面情感占 17.9%。
- 体育主题中，中性情感占 56.2%。

部分主题的样本数量较少，例如西班牙语体育主题，因此相关比例容易受到少量文本的影响，应谨慎解释。

### 6.3 如何理解这些结果

主题与情感分布能够帮助我们初步了解不同内容类别中的情感构成，并为后续内容分析提供方向。

但这些结果并不能直接证明：

- 某种语言的用户整体上更积极或更消极；
- 某个主题必然导致特定情感；
- 观察到的语言差异一定来自文化差异。

原因包括关键词主题识别的局限、情感模型可能产生的分类错误，以及样本数量和样本构成的影响。

## 七、业务洞察与应用建议

结合上述分析，项目形成以下建议。

### 7.1 优化多语言内容质量检查

英语与西班牙语测试集的模型表现存在差异。对于多语言内容运营场景，可以分别检查不同语言下的模型表现，而不是默认同一个模型在所有语言中都具有相同的可靠性。

### 7.2 重点关注模型容易出错的情感类别

中性情感的识别表现相对较弱。对于需要监测用户反馈、分析评论情绪或开展内容质量评估的场景，可以优先抽查中性类别及模型置信度较低的文本。

### 7.3 持续优化关键词分类规则

人工核验显示，部分关键词规则能够识别出符合预设主题的文本，但仍存在误分类。后续可以结合人工标注样本调整关键词、补充上下文判断规则，并扩大核验样本。

### 7.4 谨慎解读跨语言差异

语言之间的文本长度、主题分布和情感分布差异，可以作为进一步调查的线索。实际业务决策还应结合更多数据、样本背景和人工验证，避免仅凭描述性统计得出过强结论。

## 八、项目成果与能力体现

通过本项目，完成了以下工作：

- 使用 Python 对多语言社交媒体文本进行整理和探索性分析。
- 比较不同语言下的文本特征和情感分布。
- 使用准确率、宏平均 F1 值和分类报告评估情感分类模型。
- 通过分类结果分析识别模型相对薄弱的情感类别。
- 构建基于关键词的主题分类规则，并进行人工抽样核验。
- 将数据分析发现转化为多语言内容运营、分类质量检查和后续验证建议。

本项目体现了从数据整理、分析评估到业务解释的完整分析思路。

## 九、项目局限性

本项目仍存在以下限制：

1. **数据代表性有限：** 当前结果基于指定的社交媒体数据集，不能直接推广到所有平台、用户或语言群体。
2. **情感分类存在误差：** 自动情感识别结果不等同于人工判断的真实情感。
3. **关键词规则存在局限：** 规则容易解释，但可能受到语境、同义表达和关键词覆盖范围的影响。
4. **人工核验样本有限：** 35 条样本不足以全面代表所有主题及全部语言文本。
5. **主题样本数量不均：** 部分主题的样本量较小，分布比例可能不够稳定。
6. **分析以描述性结果为主：** 项目主要识别数据中的分布特征，尚不能据此建立因果关系。

## 十、后续改进方向

未来可以从以下方向进一步完善项目：

- 扩大人工标注与核验样本，提高主题分类评估的可靠性。
- 同时评估主题分类的准确率与召回率，了解误分类和漏分类情况。
- 进一步分析模型的错误案例，探索不同语言下的分类薄弱点。
- 引入更多样本和更丰富的主题特征，验证当前发现是否稳定。
- 将分析结果整理为更直观的可视化仪表板，方便业务人员查看多语言内容趋势。

## 十一、项目文件说明

仓库包含数据分析脚本、分析报告、评估结果、可视化图表及人工核验相关文件。主要文件包括：

| 文件 | 用途 |
|---|---|
| `README.md` | 项目介绍、主要结果与业务洞察 |
| `day2_analysis.py` | 数据分析脚本 |
| `day2_analysis_report.md` | 初步数据分析报告 |
| `day3_error_summary.csv` | 模型错误分析汇总 |
| `day4_error_analysis_report.md` | 错误分析报告 |
| `day5_test_set_comparison.csv` | 测试集比较结果 |
| `day5_classification_report.csv` | 分类评估结果 |
| `day5_test_evaluation_report.md` | 测试集评估报告 |
| `topic_manual_audit_labeled.csv` | 主题人工核验数据 |
| `day6_topic_audit_report.md` | 主题核验报告 |
| `day7_topic_distribution_original.csv` | 原始主题分布数据 |
| `day8_topic_sentiment_report.md` | 主题与情感分布分析报告 |
| `day8_topic_sentiment_counts.csv` | 主题与情感数量统计 |
| `day8_topic_sentiment_percentages.csv` | 主题与情感比例统计 |
| `day9_business_insights.csv` | 业务洞察汇总 |
| `day9_business_analysis_report.md` | 业务分析报告 |

注：以上文件清单应以仓库当前实际存在的文件为准；图表文件及其他辅助文件可在后续更新中补充。

## 十二、总结

本项目围绕多语言社交媒体数据，完成了文本特征分析、情感分类评估、主题识别、人工核验及业务洞察整理。

项目的核心价值不仅在于获得分类指标，更在于识别自动分析方法的局限、验证分析结果的可靠性，并将数据发现转化为可执行的内容质量检查和运营改进方向。

**项目关键词：** Python 数据分析、多语言文本分析、情感分析、主题分类、模型评估、人工核验、用户洞察、内容运营、商业分析。
