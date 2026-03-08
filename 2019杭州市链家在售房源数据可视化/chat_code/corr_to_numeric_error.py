import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv(r'/蓝桥杯练习/data_analysis_cases\2019杭州市链家在售房源数据可视化\house.csv')
df = df.fillna(0)
df['面积'] = df['面积'].str.lstrip().str.rstrip().str.replace("平米","").astype(np.float64)
df['单价'] = df['单价'].str.lstrip().str.rstrip().str.replace("元/平米","").astype(np.float64)

# 针对你的房产数据
print("=== 相关性分析 ===")

# 选择数值型列进行相关性分析
numeric_columns = ['单价', '面积', '关注']
correlation_matrix = df[numeric_columns].corr()

print("相关系数矩阵：")
print(correlation_matrix)

# 可视化相关性热力图
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix,
            annot=True,           # 显示数值
            cmap='coolwarm',      # 颜色映射
            center=0,             # 中心值为0
            square=True,          # 正方形格子
            fmt='.2f')            # 保留2位小数
plt.title('特征相关性热力图')
plt.tight_layout()
plt.show()

# 分析具体的相关关系
print("\n=== 相关性解读 ===")
print(f"单价与面积相关系数: {correlation_matrix.loc['单价', '面积']:.3f}")
print(f"单价与关注相关系数: {correlation_matrix.loc['单价', '关注']:.3f}")
print(f"面积与关注相关系数: {correlation_matrix.loc['面积', '关注']:.3f}")

# 找出强相关特征
strong_corr = correlation_matrix.abs() > 0.7
print("\n=== 强相关特征对 ===")
for i in range(len(numeric_columns)):
    for j in range(i+1, len(numeric_columns)):
        corr_value = correlation_matrix.iloc[i, j]
        if abs(corr_value) > 0.7:
            print(f"{numeric_columns[i]} vs {numeric_columns[j]}: {corr_value:.3f}")
