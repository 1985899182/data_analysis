import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv(r'/蓝桥杯练习/data_analysis_cases\2019杭州市链家在售房源数据可视化\house.csv')
df = df.fillna(0)
df['面积'] = df['面积'].str.lstrip().str.rstrip().str.replace("平米","").astype(np.float64)
df['单价'] = df['单价'].str.lstrip().str.rstrip().str.replace("元/平米","").astype(np.float64)
group_by_floor = df.groupby('楼层')
#%%
# 绘制 关注,单价,面积之间的线性图
def attention_price_square_relationship():
    df1 = df.sort_values('单价',ascending=True)
    # rand_index = df1.sample(df1.size,replace=False).index
    fig,ax = plt.subplots(1,1,dpi = 150)
    ax.bar(df1['单价'],df1['关注'] * 600,color = 'blue',label = '关注',alpha = 0.5,linewidth = 50)
    ax.bar(df1['单价'],df1['面积'] * 100,color = 'red',label = '面积',alpha = 0.7,linewidth = 50)
    # ax.axvline(x = 19800,linestyle='--',color = 'black',linewidth = 1)
    # ax.axvline(x = 30800,linestyle='--',color = 'black',linewidth = 1)
    ax.set_xlim(0, 80000)
    ax.set_ylim(0, 110000)
    ax.text(20800,ax.get_ylim()[1]*0.9,'密集开始点',horizontalalignment = 'left',fontsize = 6,color = 'purple',bbox=dict(facecolor = 'white',edgecolor = 'pink'))
    ax.annotate(text = '密集结束点',xy = (40200,ax.get_ylim()[1]*0.9),fontsize = 6,arrowprops=dict(arrowstyle = '->',color = 'grey'))
    ax.legend()
    ax.set_xlabel('单价')

    plt.show()
attention_price_square_relationship()

#%%
df['挂牌时间'] = pd.to_datetime(df['挂牌时间'])
print(df)

#%%
print(df.loc[df['楼层'].str.contains("/")])
#      产权  关注    区域         单价     小区  ...        挂牌时间   朝向        楼层   装修情况        面积
# 0   70年   0  余杭临平  21015元/平米  众安理想湾  ...  2019-06-12  南 北  低楼层/共33层  平层/精装   99.93平米
# 1   70年   4  余杭临平  28416元/平米  众安理想湾  ...  2019-04-04    南    联排/共3层     毛坯   274.5平米
# 2   70年   2  余杭临平  17323元/平米  众安理想湾  ...  2018-09-07    南  高楼层/共33层     精装     127平米
# 3   70年   4  余杭临平  18249元/平米  众安理想湾  ...  2018-08-15    南  中楼层/共33层     简装     137平米
# 4   70年   1  余杭临平  24112元/平米  众安理想湾  ...  2019-04-21    南  高楼层/共34层     精装   89.17平米
# 5   70年   1  余杭临平  24882元/平米  众安理想湾  ...  2019-06-03    南  低楼层/共34层  平层/精装   88.42平米
# 6   70年   0  余杭临平  18750元/平米  众安理想湾  ...  2019-05-28    南  中楼层/共34层     简装     112平米
# 7   70年   1  余杭临平  21625元/平米  众安理想湾  ...  2019-03-08    南  低楼层/共34层     精装      80平米
# 8   70年   6  余杭临平  20505元/平米  众安理想湾  ...  2019-04-29    南  高楼层/共33层     毛坯   80.47平米
# 9   70年   0  余杭临平  16042元/平米  众安理想湾  ...  2019-06-21    南  低楼层/共33层     其他  275.53平米
# 10  70年   5  余杭临平  40154元/平米   金都夏宫  ...  2019-04-13    南    联排/共3层     毛坯  336.21平米
# 11  70年  11  余杭临平  26423元/平米   金都夏宫  ...  2018-09-24    南  高楼层/共31层     精装  136.25平米
# 12  70年   1  余杭临平  25281元/平米   金都夏宫  ...  2018-10-19    南  高楼层/共40层     毛坯      89平米
# 13  70年   7  余杭临平  23620元/平米   金都夏宫  ...  2019-03-16    南  中楼层/共40层     简装   88.91平米
# 14  70年   0  余杭临平  26297元/平米   金都夏宫  ...  2019-06-09    南  高楼层/共31层  平层/其他     135平米
# 15  70年   0  余杭临平  23489元/平米   金都夏宫  ...  2019-03-26    南  低楼层/共15层  平层/精装      86平米
# 16  70年   3  余杭临平  22869元/平米   金都夏宫  ...  2019-03-06    南  低楼层/共32层     毛坯  135.56平米
# 17  70年   0  余杭临平  27942元/平米   金都夏宫  ...  2019-03-13    南  高楼层/共32层     精装     136平米
# 18  70年   1  余杭临平  23342元/平米   金都夏宫  ...  2019-03-14    南  低楼层/共34层  平层/精装   89.11平米
# 19  70年   0  余杭临平  20492元/平米   金都夏宫  ...  2019-06-04    南  高楼层/共37层     其他     122平米
