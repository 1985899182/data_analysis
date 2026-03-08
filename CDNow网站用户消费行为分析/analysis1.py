import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn
import seaborn as sns
from matplotlib.pyplot import subplots

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv('CDNOW.txt', sep =r'\s+', engine ='python', names = ['用户ID', '购买日期', '订单数', '订单金额'])
df.dropna(inplace=True)
df['购买日期'] = pd.to_datetime(df['购买日期'],format='%Y%m%d')
group_by_orders = df.groupby('订单数')
group_by_ID = df.groupby('用户ID')

def plot_combined_data():
    """
    绘制1997和1998年订单金额和消费人数的组合图
    :return: None
    """
    fig, ax1 = plt.subplots(1, 1, figsize=(12, 6))
    
    # 左侧Y轴：消费人数
    ax1.set_title('1997和1998年订单数据统计')
    ax1.set_xlabel('购买日期')
    ax1.set_ylabel('消费人数', color='tab:blue')
    data = df['购买日期'].value_counts().sort_index(ascending=True)
    line1 = ax1.plot(data.index, data.values, color='tab:blue', label='消费人数')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    ax1.tick_params(axis='x', rotation=45)
    
    # 右侧Y轴：订单金额
    ax2 = ax1.twinx()
    ax2.set_ylabel('订单金额', color='tab:red')
    group_by_date = df.groupby('购买日期')['订单金额'].sum()
    line2 = ax2.plot(group_by_date.index, group_by_date.values, color='tab:red', label='订单金额')
    ax2.tick_params(axis='y', labelcolor='tab:red')
    
    # 图例设置
    lines = line1 + line2
    labels = [str(line.get_label()) for line in lines]
    print(labels)
    ax1.legend(lines, labels, loc='upper left')
    fig.tight_layout()
    fig.show()


if __name__ == "__main__":
    plot_combined_data()
#    用户ID   购买日期  订单数   订单金额
#      1    19970101    1    11.77
#      2    19970112    1    12.00
#      2    19970112    5    77.00
#      3    19970102    2    20.76
#      3    19970330    2    20.76
