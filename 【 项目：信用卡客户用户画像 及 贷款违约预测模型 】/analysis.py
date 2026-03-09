import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)
plt.rcParams['font.family'] = "SimHei"
plt.rcParams['axes.unicode_minus'] = False
# print(os.listdir("../【 项目：信用卡客户用户画像 及 贷款违约预测模型 】"))


def process_data():
    """
    处理原始数据
    :return: None
    """
    accounts_data['date'] = pd.to_datetime(accounts_data['date'])

    card_data.rename(columns = {"issued":"date"},inplace=True)
    card_data['date'] = pd.to_datetime(card_data['date'])

    clients_data['birth_date'] = pd.to_datetime(clients_data['birth_date'])

    loans_data['date'] = pd.to_datetime(loans_data['date'])

    trans_data['date'] = pd.to_datetime(trans_data['date'])

    order_data.dropna(inplace=True)


def print_content(xx_data):
    print(f"{str(xx_data)}的原始数据:".center(20,'*'))
    xx_data.info()
    print(xx_data.describe())
    print(xx_data.head())
    print('\n')

def pre_view():
    """
    查看数据的原始数据
    :return: None
    """
    datas = [accounts_data,card_data,clients_data,disp_data,district_data,loans_data,order_data,trans_data]
    for data in datas:
        print_content(data)

def plot_accounts():
    """
    可视化accounts中的数据
    :return:None
    """
    # frequency的类型分布柱状图
    data1 = accounts_data.groupby("frequency").size()
    fig1,ax1 = plt.subplots(nrows=1,ncols=1)
    ax1.bar(data1.index,data1.values)
    ax1.grid()

    # 还款日期的直方图图
    data2 = accounts_data["date"].dt.dayofyear.sort_values(ascending=True)
    fig2,ax2 = plt.subplots(nrows=1,ncols=1)
    ax2.hist(data2,bins = 72)
    ax2.set_xticks(np.cumsum(np.array([0,31,28,31,30,31,30,31,31,30,31,30])) + 1)
    ax2.set_xticklabels([f"第{i}月" for i in range(1,13)])
    ax2.tick_params('x',rotation = 35)
    ax2.grid(alpha = 0.7)
    ax2.axvline(31)

    # 绘制不同地区的贷款数量
    data3 = accounts_data.groupby("district_id").size().sort_index()
    fig3,ax3 = plt.subplots(nrows=1,ncols=1)
    sns.barplot(data3,ax = ax3)
    end_index = max(data3.index) + 1
    # 将x轴的刻度从-1开始,便于第一个柱子清晰显示
    ax3.set_xlim(-1,end_index)
    # 因为从0开始,所有0到4组成5步
    """
    eg:
        | | | | | | | | | |
        0 1 2 3 4 5 6 7 8 9 (原刻度)
        1 2 3 4 5 6 7 8 9 10 (从0到原刻度4的时候走了4步(与后面计算方式一直，均不算起点)，从4到原刻度9的时候走了5步)
        更改原刻度的0，4，9...为刻度后,更改成从1开始,就是1,5,10
    """
    ax3.set_xticks([0] + [i for i in range(4,end_index,5)])
    # 重新设置刻度标签
    ax3.set_xticklabels([str(1)] + [str(i) for i in range(5,end_index,5)])
    ax3.grid()

    plt.show()


if __name__ == "__main__":

    # accounts(账户表)
    accounts_data = pd.read_csv('accounts.csv', encoding ='gbk')
    # card(信用卡)
    card_data = pd.read_csv('card.csv', encoding ='gbk')
    # client(客户信息表)
    clients_data = pd.read_csv('clients.csv', encoding ='gbk')
    # disp(权限分配表)
    disp_data = pd.read_csv('disp.csv', encoding ='gbk')
    # district(人口地区统计表)
    district_data = pd.read_csv('district.csv', encoding ='gbk')
    # loans(贷款表)
    loans_data = pd.read_csv('loans.csv', encoding ='gbk')
    # order(支付命令表)
    order_data = pd.read_csv('order.csv', encoding ='gbk')
    # trans(交易表)
    trans_data = pd.read_csv('trans.csv', encoding ='gbk', dtype={"bank":str})

    # 数据概览
    # pre_view()

    # 数据预处理
    process_data()

    # 统计并绘制交易类型
    plot_accounts()


#    account_id  district_id frequency       date
# 0         576           55        月结 1993-01-01
# 1        3818           74        月结 1993-01-01
# 2         704           55        月结 1993-01-01
# 3        2378           16        月结 1993-01-01
# 4        2632           24        月结 1993-01-02

#    card_id  disp_id       date type
# 0     1005     9285 1993-11-07  普通卡
# 1      104      588 1994-01-19  普通卡
# 2      747     4915 1994-02-05  普通卡
# 3       70      439 1994-02-08  普通卡
# 4      577     3687 1994-02-15  普通卡

#    client_id sex birth_date  district_id
# 0          1   女 1970-12-13           18
# 1          2   男 1945-02-04            1
# 2          3   女 1940-10-09            1
# 3          4   男 1956-12-01            5
# 4          5   女 1960-07-03            5

#    disp_id  client_id  account_id type
# 0        1          1           1  所有者
# 1        2          2           2  所有者
# 2        3          3           2   用户
# 3        4          4           3  所有者
# 4        5          5           3   用户

#    A1     GDP       A4    A10    A11   A12   A13  A14   A15   a16
# 0   1  283894  1204953  100.0  12541  0.29  0.43  167  35.6  41.1
# 1   2   11655    88884   46.7   8507  1.67  1.85  132  12.1  15.0
# 2   3   13146    75232   41.7   8980  1.95  2.21  111  18.8  18.7
# 3   4   16108   149893   67.4   9753  4.64  5.05  109  17.5  19.7
# 4   5   13452    95616   51.4   9307  3.85  4.43  118  13.7  15.9

#    loan_id  account_id       date  amount  duration  payments status
# 0     5314        1787 1993-07-05   96396        12      8033      B
# 1     5316        1801 1993-07-11  165960        36      4610      A
# 2     6863        9188 1993-07-28  127080        60      2118      A
# 3     5325        1843 1993-08-03  105804        36      2939      A
# 4     7240       11013 1993-09-06  274740        60      4579      A

#       order_id  account_id bank_to  account_to  amount k_symbol
# 1379     29406           3      AB    59972357  3539.0     保险支付
# 1380     29434          25      WX    52864879   164.0     保险支付
# 1381     29441          29      UV    41335338     8.0     保险支付
# 1382     29454          37      YZ    89609831    97.0     保险支付
# 1383     29458          38      OP    64685678   228.0     保险支付

#    trans_id  account_id       date type operation  amount balance k_symbol  \
# 0    695247        2378 1993-01-01    贷      信贷资金    $700    $700      NaN
# 1    171812         576 1993-01-01    贷      信贷资金    $900    $900      NaN
# 2    207264         704 1993-01-01    贷      信贷资金  $1,000  $1,000      NaN
# 3   1117247        3818 1993-01-01    贷      信贷资金    $600    $600      NaN
# 4    579373        1972 1993-01-02    贷      信贷资金    $400    $400      NaN
#   bank  account
# 0  NaN      NaN
# 1  NaN      NaN
# 2  NaN      NaN
# 3  NaN      NaN
# 4  NaN      NaN

