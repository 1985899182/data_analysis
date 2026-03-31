from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes,mark_inset
from load_data import load_data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_columns',None)

def plot_price_distribution():
    """
    绘制房价在不同区间的分布情况,直方图
    :return: None
    """
    data1 = [data[i]['per_price'] for i in data.keys()]
    data1_labels = [i for i in data.keys()]

    fig1,ax1 = plt.subplots(nrows=1,ncols=1)
    ax1.set_title('不同地区的房价分布')
    ax1.hist(data1,stacked=True,label=data1_labels)
    ax1.set_xlabel("万元/平方米")
    ax1.set_ylabel("数量")
    ax1.legend()
    plt.show()

def plot_judge_price_rela_area():
    """
    判断房价和面积的关系
    :return: None
    """

    data1 = [data[i][['AREA','per_price']] for i in data.keys()]
    data1 = pd.concat(data1,axis=0)
    data2 = data1['AREA']
    data3 = data1['per_price']
    size = data2.apply(lambda x:(int(x / data2.mean()) + 1) * 5)

    fig1,ax1 = plt.subplots(nrows = 1,ncols=1,dpi = 100,figsize = (12,8))
    sc1 = ax1.scatter(data2, data3, s=size, c=data3)
    plt.colorbar(sc1)

    divider = make_axes_locatable(ax1)
    ax_top = divider.append_axes("top",size = 1,pad=0.2,sharex = ax1)
    ax_top.hist(data2,bins = 30)

    ax_right = divider.append_axes("right",size = 1,pad = 0.2)
    ax_right.hist(data3,orientation='horizontal',bins = 20)
    ax_right.set_xticks(range(0,5000,1000))
    ax_right.tick_params('x',rotation = 45)
    ax_right.tick_params('y',labelleft=False)
    ax_top.tick_params('x',labelbottom=False)

    #局部放大，对此部分分析无作用，故注释掉
    # data4 = data1[(data1['AREA'] < 150) & (data1['per_price'] < 10)]
    # data5 = data4['AREA']
    # data6 = data4['per_price']
    # size = data5.apply(lambda x:(int(x / data5.mean()) + 1) * 5)
    # axins = inset_axes(ax1,width="40%",height="40%",loc="upper right")
    # sc2 = axins.scatter(data5,data6,s = size,c = data6)
    # mark_inset(ax1,axins,loc1=2, loc2=4, ec='red')

    plt.show()

    # 用OLS模型检验是否存在房价随面积递增而递减
    data2 = sm.add_constant(data2)
    # y在前x在后
    model = sm.OLS(data3,data2).fit()
    print(model.summary())
    # 结论是不存在

def plot_price_rela_room():
    """
    房价和房屋数量的关系
    :return: None
    """
    data1 = [data[i][['per_price','roomnum','hall']] for i in data.keys()]
    data1 = pd.concat(data1,axis=0)
    data2 = data1.groupby('roomnum')
    data3 = data1.groupby('hall')
    data2_labels = list(data2.groups.keys())
    data3_labels = list(data3.groups.keys())
    data2 = [data2['per_price'].get_group(i) for i in data2.groups.keys()]
    data3 = [data3['per_price'].get_group(i) for i in data3.groups.keys()]

    # 设置箱线图的flierprops参数
    flier_props = dict(markeredgecolor='red', alpha=0.7)

    fig1,ax = plt.subplots(nrows=2,ncols=1)
    ax1,ax2 = ax
    ax1.boxplot(data2,flierprops = flier_props)
    ax1.set_xticklabels(data2_labels)
    ax1.set_xlabel('卧室数量')
    ax1.set_ylabel('万元/平方米')
    ax1.grid()

    # 增大子图之间的间距
    fig1.subplots_adjust(hspace=0.5)

    ax2.boxplot(data3,flierprops = flier_props)
    ax2.set_xticklabels(data3_labels)
    ax2.set_xlabel('客厅数量')
    ax2.set_ylabel('万元/平方米')
    sub_ax2 = inset_axes(ax2,width="30%",height="50%",loc = "upper right")
    sub_ax2.boxplot(data3[-2:])
    sub_ax2.set_xticklabels(data3_labels[-2:])
    ax2.axvline(x = 6,ymin = 0.25,ymax = 0.6, linestyle='--')
    ax2.axvline(x = 7,ymin = 0.2,ymax = 0.6, linestyle='--')
    ax2.text(6.25,7,'放大',bbox=dict(facecolor='blue', alpha=0.5))
    ax2.grid()

    plt.show()


def plot_sch_sub_rela_price():
    """
    比较学区房，地铁房对房价的影响
    :return: None
    """
    data1 = pd.concat([data[i][['school','subway','per_price']] for i in data.keys()])
    data2 = data1.groupby(['school','subway'])
    data3 = [data2.get_group(i)['per_price'].mean() for i in data2.groups.keys()]

    fig1,ax1 = plt.subplots(nrows=1,ncols=1)
    ax1.bar(["no_shc_sub","no_sch","no_sub","have_sch_sub"],data3,color =['#FFB6C1', '#98FB98', '#87CEEB', '#DDA0DD'])
    ax1.set_title('有无学区房/地铁站对房价的普遍影响')
    ax1.set_ylabel('万元/平方米')
    ax1.tick_params('y',rotation = 45)
    ax1.grid()
    ax1.set_axisbelow(True)
    fig1.show()

if __name__ == "__main__":
    data = load_data()
    plot_price_distribution()

    plot_judge_price_rela_area()

    plot_price_rela_room()

    plot_sch_sub_rela_price()