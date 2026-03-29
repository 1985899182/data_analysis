import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_columns',None)
# print(os.listdir('D:\python_file\pythonProject4\data_analysis_cases\【 项目：深圳市二手房房价分析及预测 】'))
def load_data() -> dict[str, pd.DataFrame]:
    """加载数据"""
    return {
        'baoan': pd.read_excel('./szfj_baoan.xls').dropna(),
        'dapengxinqu': pd.read_excel('./szfj_dapengxinqu.xls').dropna(),
        'futian': pd.read_excel('szfj_futian.xls').dropna(),
        'guangming': pd.read_excel('szfj_guangming.xls').dropna(),
        'longgang': pd.read_excel('szfj_longgang.xls').dropna(),
        'longhua': pd.read_excel('szfj_longhua.xls').dropna(),
        'luohu': pd.read_excel('szfj_luohu.xls').dropna(),
        'nanshan': pd.read_excel('szfj_nanshan.xls').dropna(),
        'pingshan': pd.read_excel('szfj_pingshan.xls').dropna(),
        'yantian': pd.read_excel('szfj_yantian.xls').dropna(),
    }
