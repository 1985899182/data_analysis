import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('../house.csv')

# 演示两种方法的区别
print("原始数据类型:")
print(df['面积'].dtype)
print(df['面积'].head(3))

# 方法1: astype() - 强制转换为float
df_copy1 = df.copy()
df_copy1['面积'] = df_copy1['面积'].str.replace("平米","").astype(float)
print("\n使用astype(float)后的类型:")
print(df_copy1['面积'].dtype)

# 方法2: convert_dtypes() - 自动推断最佳类型
df_copy2 = df.copy()
df_copy2['面积'] = df_copy2['面积'].str.replace("平米","").convert_dtypes()
print("\n使用convert_dtypes()后的类型:")
print(df_copy2['面积'].dtype)

# 显示结果对比
print("\n三种方法的结果对比:")
print("原始:", df['面积'].head(2).tolist())
print("astype:", df_copy1['面积'].head(2).tolist())
print("convert_dtypes:", df_copy2['面积'].head(2).tolist())
