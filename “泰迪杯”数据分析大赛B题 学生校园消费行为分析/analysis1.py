import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
df1 = pd.read_csv("data1.csv", encoding='gbk')
df2 = pd.read_csv("data2.csv", encoding='gbk')
df3 = pd.read_csv("data3.csv", encoding='gbk')
def pre_view():
    """
    初步查看数据
    :return: None
    """
    print("data1数据的大致情况".center(50,'='))
    print("\t***数据分布:")
    print(df1.describe())
    print("\t***数据类型:")
    print(df1.info())
    print()
    print("dat2数据的大致情况".center(50,'='))
    print("\t***数据分布:")
    print(df2.describe())
    print("\t***数据类型:")
    print(df2.info())
    print()
    print("data3数据的大致情况".center(50,'='))
    print("\t***数据分布:")
    print(df3.describe())
    print("\t***数据类型:")
    print(df3.info())

def processing_data() -> tuple[pd.DataFrame,pd.DataFrame,pd.DataFrame]:
    """
    处理异常值和缺失值,转化日期数据
    :return:
    """
    df1.dropna(inplace=True)
    df2.drop(columns = ['TermSerNo','conOperNo'],inplace=True)
    df3.dropna(inplace=True)
    # 修改df1中的AccessCardNo错误
    df1.loc[388,'AccessCardNo'] = 130778
    # 转化日期格式
    df2['Date'] = pd.to_datetime(df2['Date'])
    df3['Date'] = pd.to_datetime(df3['Date'])
    df1.columns = ['序号', '校园卡号', '性别', '专业名称', '门禁卡号']
    df2.columns = ['流水号', '校园卡号', '校园卡编号', '消费时间', '消费金额', '存储金额', '余额', '消费次数', '消费类型', '消费操作编码', '操作编码', '消费地点']
    df3.columns = ['序号', '门禁卡号', '进出时间', '进出地点', '是否通过', '描述']

def plot_what():
    print(df2['存储金额'].unique())
def plot_canteen():
    """
    绘制了食堂和商店的消费次数和消费总金额，意在比较不同的运营地点的优劣
    :return:
    """
    # 绘制饼状图
    group_by_spot = df2[df2['消费地点'].str.contains(r'.*食堂|好利来食品店|红太阳超市',regex = True)].groupby('消费地点')
    labels = group_by_spot.size().index.tolist()
    fig,ax = plt.subplots(2,1,dpi = 100)
    fig.suptitle('不同地点的消费占比',fontsize = 16,fontweight = 'bold')
    ax[0].set_title('不同地点的消费次数')
    props = {
        'shadow' : True,
        'autopct' : '%.2f%%',
        'wedgeprops' : {'linewidth': 1.5,'edgecolor': 'white'},
        'labeldistance' : 1.2,
        'explode' : [0.02] * len(labels),
        'labels' : labels,
        'pctdistance' : 0.85,
        'textprops' : {'fontsize': 10}
    }
    obj,*_ = ax[0].pie(group_by_spot['消费次数'].sum(),**props)
    ax[1].set_title('不同地点的消费总金额')
    ax[1].pie(group_by_spot['消费金额'].sum(),**props)
    fig.legend(handles = obj,labels = labels,fontsize = 10)
    fig.tight_layout()
    fig.show()

    # 绘制柱状图

    fig,ax1 = plt.subplots(nrows=1,ncols=1,dpi = 100)
    fig.suptitle('不同地点的消费占比',fontsize = 16,fontweight = 'bold')
    ax1.set_xlabel('食堂or商店名')
    ax1.set_ylabel('消费次数')
    width = 0.2
    x_pos = np.arange(len(labels))
    obj = ax1.bar(x_pos - width/2,group_by_spot['消费次数'].sum(),color = 'red',alpha = 0.7,width = width)
    ax1.tick_params('x',rotation=35)
    ax1.tick_params('y',labelcolor = 'red')
    ax2 = ax1.twinx()
    ax2.tick_params('y',labelcolor = 'blue',rotation = 60)
    ax2.set_ylabel('消费金额')
    ax2.bar(x_pos + width/2,group_by_spot['消费金额'].sum(),color = 'blue',alpha = 0.7,width = width)
    ax1.set_xticks(x_pos,labels,fontsize = 8)
    ax1.grid()
    fig.show()


if __name__ == "__main__":
    pre_view()
    processing_data()
    plot_what()
    # plot_canteen()


#    序号    校园卡号 性别    专业名称      门禁卡号
# 0   1  180001  男  18国际金融  19762330
# 1   2  180002  男  18国际金融  20521594
# 2   3  180003  男  18国际金融  20513946
# 3   4  180004  男  18国际金融  20018058
# 4   5  180005  男  18国际金融  20945770



#          流水号    校园卡号     校园卡编号                消费时间  消费金额  存储金额     余额  消费次数  \
# 0  117342773  181316  20181316 2019-04-20 20:17:00   3.0   0.0  186.1   818
# 1  117344766  181316  20181316 2019-04-20 08:47:00   0.5   0.0  199.5   814
# 2  117346258  181316  20181316 2019-04-22 07:27:00   0.5   0.0  183.1   820
# 3  117308066  181317  20181317 2019-04-21 07:46:00   3.5   0.0   50.2   211
# 4  117309001  181317  20181317 2019-04-19 22:31:00   2.5   0.0   61.7   209
#
#   消费类型  消费操作编码  操作编码    消费地点
# 0   消费      49   235    第一食堂
# 1   消费      63    27    第二食堂
# 2   消费      63    27    第二食堂
# 3   消费     196   133  好利来食品店
# 4   消费     146    48  好利来食品店


#         序号      门禁卡号                进出时间       进出地点  是否通过    描述
# 0  1330906  25558880 2019-04-01 00:00:00  第六教学楼[进门]     1  允许通过
# 1  1330907  18413143 2019-04-01 00:02:00  第六教学楼[出门]     1  允许通过
# 2  1331384  11642752 2019-04-01 00:00:00    飞凤轩[进门]     1  允许通过
# 3  1330908  24124155 2019-04-01 00:00:00  第六教学楼[出门]     1  允许通过
# 4  1331385  18629328 2019-04-01 00:11:00    飞凤轩[进门]     1  允许通过
# Disconnected from server

# ['消费' '存款' '取款' '退款' '无卡销户' '发卡存款']