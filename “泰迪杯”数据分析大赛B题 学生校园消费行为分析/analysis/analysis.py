import os
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------
# Paths
# --------------------
ANALYSIS_DIR = Path(__file__).resolve().parent
BASE_DIR = ANALYSIS_DIR.parent

DATA1 = BASE_DIR / "data1.csv"
DATA2 = BASE_DIR / "data2.csv"
DATA3 = BASE_DIR / "data3.csv"

OUT_DIR = ANALYSIS_DIR
OUT_DIR.mkdir(parents=True, exist_ok=True)

# --------------------
# Plot style (Chinese fonts)
# --------------------
plt.rcParams['font.family'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# --------------------
# Load data
# --------------------
_df1 = pd.read_csv(DATA1, encoding='gbk')
_df2 = pd.read_csv(DATA2, encoding='gbk')
_df3 = pd.read_csv(DATA3, encoding='gbk')

# Rename columns to English for consistency
_df1.columns = ['Index', 'CardNo', 'Sex', 'Major', 'AccessCardNo']
_df2.columns = ['Index', 'CardNo', 'PeoNo', 'Date', 'Money', 'FundMoney', 'Surplus', 'CardCount', 'Type',
                'TermNo', 'TermSerNo', 'conOperNo', 'OperNo', 'Dept']
_df3.columns = ['Index', 'AccessCardNo', 'Date', 'Address', 'Access', 'Describe']

# Parse dates
_df2['Date'] = pd.to_datetime(_df2['Date'], errors='coerce')
_df3['Date'] = pd.to_datetime(_df3['Date'], errors='coerce')

# Basic cleaning
_df2 = _df2.dropna(subset=['Date', 'CardNo', 'Money', 'Type'])
_df3 = _df3.dropna(subset=['Date', 'AccessCardNo'])

# Consumption transactions only
consume = _df2[_df2['Type'] == '消费'].copy()

# Create date parts
consume['Day'] = consume['Date'].dt.date
consume['Hour'] = consume['Date'].dt.hour
consume['Month'] = consume['Date'].dt.to_period('M').astype(str)

# --------------------
# Overall summary
# --------------------
start_date = consume['Date'].min().date()
end_date = consume['Date'].max().date()

overall = {
    'time_range': f"{start_date} ~ {end_date}",
    'total_transactions': int(consume.shape[0]),
    'total_spend': float(consume['Money'].sum()),
    'avg_spend_per_txn': float(consume['Money'].mean()),
    'unique_students': int(consume['CardNo'].nunique()),
}

# --------------------
# Daily trend
# --------------------
daily = consume.groupby('Day', as_index=False).agg(
    txn_count=('Money', 'size'),
    total_spend=('Money', 'sum')
)

daily.to_csv(OUT_DIR / "daily_consumption.csv", index=False, encoding='utf-8-sig')

plt.figure(figsize=(10, 4))
plt.plot(pd.to_datetime(daily['Day']), daily['total_spend'], linewidth=1.2)
plt.title('每日消费总额趋势')
plt.xlabel('日期')
plt.ylabel('消费总额')
plt.tight_layout()
plt.savefig(OUT_DIR / "daily_spend.png", dpi=160)
plt.close()

# --------------------
# Hourly / meal time analysis
# --------------------
# Meal time buckets
bins = [0, 6, 10, 14, 17, 21, 24]
labels = ['深夜(0-6)', '早餐(6-10)', '午餐(10-14)', '下午茶(14-17)', '晚餐(17-21)', '夜宵(21-24)']
consume['MealTime'] = pd.cut(consume['Hour'], bins=bins, labels=labels, right=False, include_lowest=True)

meal = consume.groupby('MealTime', as_index=False).agg(
    txn_count=('Money', 'size'),
    total_spend=('Money', 'sum')
)

plt.figure(figsize=(8, 4))
plt.bar(meal['MealTime'].astype(str), meal['total_spend'])
plt.title('不同时段消费总额')
plt.xlabel('时段')
plt.ylabel('消费总额')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(OUT_DIR / "meal_time_spend.png", dpi=160)
plt.close()

# Hourly
hourly = consume.groupby('Hour', as_index=False).agg(total_spend=('Money', 'sum'))
plt.figure(figsize=(8, 4))
plt.bar(hourly['Hour'], hourly['total_spend'])
plt.title('各小时消费总额')
plt.xlabel('小时')
plt.ylabel('消费总额')
plt.tight_layout()
plt.savefig(OUT_DIR / "hourly_spend.png", dpi=160)
plt.close()

# --------------------
# Canteen / Dept analysis
# --------------------
# Identify canteens by keywords
canteen_keywords = r'食堂|餐厅|风味|清真|面|餐'
consume['DeptType'] = np.where(consume['Dept'].astype(str).str.contains(canteen_keywords, regex=True), '食堂', '非食堂')

dept_summary = consume.groupby('Dept', as_index=False).agg(
    txn_count=('Money', 'size'),
    total_spend=('Money', 'sum'),
    avg_spend=('Money', 'mean')
).sort_values('total_spend', ascending=False)

dept_summary.to_csv(OUT_DIR / "dept_summary.csv", index=False, encoding='utf-8-sig')

# Top 10 depts by spend
_top10_spend = dept_summary.head(10)
plt.figure(figsize=(9, 4))
plt.bar(_top10_spend['Dept'], _top10_spend['total_spend'])
plt.title('消费总额Top10地点')
plt.xlabel('地点')
plt.ylabel('消费总额')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig(OUT_DIR / "dept_top10_spend.png", dpi=160)
plt.close()

# Top 10 depts by transactions
_top10_txn = dept_summary.sort_values('txn_count', ascending=False).head(10)
plt.figure(figsize=(9, 4))
plt.bar(_top10_txn['Dept'], _top10_txn['txn_count'])
plt.title('消费次数Top10地点')
plt.xlabel('地点')
plt.ylabel('消费次数')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig(OUT_DIR / "dept_top10_count.png", dpi=160)
plt.close()

# Canteen vs non-canteen
canteen_summary = consume.groupby('DeptType', as_index=False).agg(
    txn_count=('Money', 'size'),
    total_spend=('Money', 'sum')
)

# --------------------
# Student behavior features
# --------------------
# Access days per student (from data3)
_df3['Day'] = _df3['Date'].dt.date
access_days = _df3.groupby('AccessCardNo', as_index=False)['Day'].nunique().rename(columns={'Day': 'access_days'})

# Consumption features per student
consume['Day'] = consume['Date'].dt.date
student_consume = consume.groupby('CardNo', as_index=False).agg(
    txn_count=('Money', 'size'),
    total_spend=('Money', 'sum'),
    avg_spend=('Money', 'mean'),
    active_days=('Day', 'nunique'),
    first_date=('Date', 'min'),
    last_date=('Date', 'max')
)

student_consume['recency_days'] = (consume['Date'].max() - student_consume['last_date']).dt.days
student_consume['avg_daily_spend'] = student_consume['total_spend'] / student_consume['active_days']

# Merge with student info and access days
student = _df1.merge(student_consume, on='CardNo', how='left')
student = student.merge(access_days, on='AccessCardNo', how='left')
student['access_days'] = student['access_days'].fillna(0).astype(int)

student.to_csv(OUT_DIR / "student_features.csv", index=False, encoding='utf-8-sig')

# --------------------
# Segmentation model
# --------------------
feature_cols = ['total_spend', 'txn_count', 'avg_spend', 'active_days', 'avg_daily_spend', 'access_days']
seg = student[feature_cols].fillna(0)

segment_method = 'quantile'

try:
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans

    scaler = StandardScaler()
    X = scaler.fit_transform(seg)
    k = 4
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X)
    student['segment'] = labels
    segment_method = 'kmeans'
except Exception:
    # Quantile-based fallback
    q_spend = student['total_spend'].quantile([0.33, 0.66]).tolist()
    q_txn = student['txn_count'].quantile([0.33, 0.66]).tolist()

    def bucket(v, q):
        if pd.isna(v):
            return 0
        if v <= q[0]:
            return 1
        if v <= q[1]:
            return 2
        return 3

    spend_level = student['total_spend'].apply(lambda v: bucket(v, q_spend))
    txn_level = student['txn_count'].apply(lambda v: bucket(v, q_txn))
    student['segment'] = (spend_level * 10 + txn_level).astype(int)

# Segment summary
segment_summary = student.groupby('segment', as_index=False).agg(
    count=('CardNo', 'size'),
    total_spend=('total_spend', 'sum'),
    avg_spend=('avg_spend', 'mean'),
    avg_txn=('txn_count', 'mean'),
    avg_active_days=('active_days', 'mean')
).sort_values('count', ascending=False)

segment_summary.to_csv(OUT_DIR / "segment_summary.csv", index=False, encoding='utf-8-sig')

plt.figure(figsize=(7, 4))
plt.bar(segment_summary['segment'].astype(str), segment_summary['count'])
plt.title('学生细分规模')
plt.xlabel('细分群组')
plt.ylabel('人数')
plt.tight_layout()
plt.savefig(OUT_DIR / "segment_size.png", dpi=160)
plt.close()

# --------------------
# Write report
# --------------------
report_path = OUT_DIR / "analysis_report.md"

canteen_txn = int(canteen_summary.loc[canteen_summary['DeptType'] == '食堂', 'txn_count'].sum())
non_canteen_txn = int(canteen_summary.loc[canteen_summary['DeptType'] == '非食堂', 'txn_count'].sum())

canteen_spend = float(canteen_summary.loc[canteen_summary['DeptType'] == '食堂', 'total_spend'].sum())
non_canteen_spend = float(canteen_summary.loc[canteen_summary['DeptType'] == '非食堂', 'total_spend'].sum())

with report_path.open('w', encoding='utf-8') as f:
    f.write('# 学生校园消费行为分析报告\n\n')
    f.write('## 概览\n')
    f.write(f"- 数据时间范围: {overall['time_range']}\n")
    f.write(f"- 消费记录数: {overall['total_transactions']:,}\n")
    f.write(f"- 消费总额: {overall['total_spend']:.2f}\n")
    f.write(f"- 人均消费: {overall['total_spend'] / overall['unique_students']:.2f}\n")
    f.write(f"- 人均交易次数: {overall['total_transactions'] / overall['unique_students']:.2f}\n\n")

    f.write('## 时段特征\n')
    top_meal = meal.sort_values('total_spend', ascending=False).iloc[0]
    f.write(f"- 消费高峰时段: {top_meal['MealTime']}\n")
    f.write('- 图表: `meal_time_spend.png`, `hourly_spend.png`\n\n')

    f.write('## 食堂运营分析\n')
    f.write(f"- 食堂交易次数占比: {canteen_txn / (canteen_txn + non_canteen_txn):.2%}\n")
    f.write(f"- 食堂消费金额占比: {canteen_spend / (canteen_spend + non_canteen_spend):.2%}\n")
    f.write('- Top10地点: `dept_top10_spend.png`, `dept_top10_count.png`\n\n')

    f.write('## 学生消费细分\n')
    f.write(f"- 细分方法: {segment_method}\n")
    f.write('- 细分规模: `segment_size.png`\n')
    f.write('- 细分明细: `segment_summary.csv`\n\n')

    f.write('## 输出文件\n')
    f.write('- `daily_consumption.csv`\n')
    f.write('- `dept_summary.csv`\n')
    f.write('- `student_features.csv`\n')
    f.write('- `segment_summary.csv`\n')
    f.write('- 图表: `daily_spend.png`, `meal_time_spend.png`, `hourly_spend.png`, `dept_top10_spend.png`, `dept_top10_count.png`, `segment_size.png`\n')

print('Analysis completed. Outputs saved to:', OUT_DIR)
