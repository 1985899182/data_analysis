# 学生校园消费行为分析报告

## 概览
- 数据时间范围: 2019-04-01 ~ 2019-04-30
- 消费记录数: 500,755
- 消费总额: 2109251.22
- 人均消费: 250.36
- 人均交易次数: 59.44

## 时段特征
- 消费高峰时段: 午餐(10-14)
- 图表: `meal_time_spend.png`, `hourly_spend.png`

## 食堂运营分析
- 食堂交易次数占比: 89.77%
- 食堂消费金额占比: 80.60%
- Top10地点: `dept_top10_spend.png`, `dept_top10_count.png`

## 学生消费细分
- 细分方法: kmeans
- 细分规模: `segment_size.png`
- 细分明细: `segment_summary.csv`

## 输出文件
- `daily_consumption.csv`
- `dept_summary.csv`
- `student_features.csv`
- `segment_summary.csv`
- 图表: `daily_spend.png`, `meal_time_spend.png`, `hourly_spend.png`, `dept_top10_spend.png`, `dept_top10_count.png`, `segment_size.png`
