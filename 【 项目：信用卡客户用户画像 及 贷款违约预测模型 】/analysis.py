import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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
    trans_data['amount'] = trans_data['amount'].astype(str).str.replace(r"[,\$]","",regex=True).astype(float)

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

    plt.show()

def plot_clients():
    """
    可视化clients中的数据
    :return: None
    """
    # 绘制不同客户的开户时间分布柱状图
    fig1, ax1 = plt.subplots(nrows=1, ncols=1)
    clients_data["birth_date"] = clients_data["birth_date"].dt.year
    data1 = clients_data.groupby("birth_date").size()
    sns.barplot(x = data1.index,y = data1.values,ax = ax1)
    end_index = (max(data1.index) + 1) % 100
    ax1.set_xticks([0] + [i for i in range(9,end_index,10)])
    # 重新设置刻度标签
    ax1.set_xticklabels(["1901"] + [f"19{i:02}" for i in range(10,end_index,10)])
    ax1.grid()

    # 探究各地区客户数量分布
    fig2, ax2 = plt.subplots(nrows=1, ncols=1)
    data2 = clients_data.groupby(["district_id", "sex"]).size()
    index_ = data2.index

    # 提取男性数据
    male_mask = [i[1] == '男' for i in index_]
    x_m = np.array([i[0] for i, is_male in zip(index_, male_mask) if is_male])
    y_m = np.array([data2.loc[i] for i, is_male in zip(index_, male_mask) if is_male])

    # 提取女性数据
    female_mask = [i[1] == '女' for i in index_]
    x_w = np.array([i[0] for i, is_female in zip(index_, female_mask) if is_female])
    y_w = np.array([data2.loc[i] for i, is_female in zip(index_, female_mask) if is_female])

    width = 0.4
    props_m = {"width": width, "label": "男"}
    props_w = {"width": width, "label": "女"}
    ax2.bar(x_m - width / 2, y_m, **props_m)
    ax2.bar(x_w + width / 2, y_w, **props_w)
    ax2.set_xticks([1] + [i for i in range(5, len(index_) // 2, 5)])
    ax2.legend()

    plt.show()


def plot_loans():
    """
    分析贷款金额与贷款期限的关系
    :return:None
    """
    fig1,ax1 = plt.subplots(nrows=1,ncols=1)
    ax1.scatter(loans_data["duration"],loans_data["amount"])
    ax1.set_xlabel("/月")
    ax1.set_ylabel("/元")
    ax1.set_title("分析贷款金额与贷款期限的关系")
    ax1.grid()

    plt.show()

def plot_loans_rela_district():
    """
    探究不同地区的贷款违约率
    :return: None
    """
    # 先计算每个地区的总数和违约数
    merged = pd.merge(loans_data, accounts_data, how="inner", on="account_id")
    data1 = merged.groupby(["district_id", "status"]).size()

    mask = data1.index.get_level_values('status').isin(['B', 'D'])
    fall_by_district = data1[mask].groupby(level='district_id').sum()
    total_by_district = data1.groupby(level='district_id').sum()
    fall_by_district = fall_by_district.reindex(total_by_district.index,fill_value=0)
    x = data1.index.get_level_values("district_id").unique().tolist()
    y_total = np.array(total_by_district.tolist())
    y_fall = np.array(fall_by_district.tolist())
    y_normal = y_total - y_fall
    y_fall_by_all = y_fall / y_total

    # 条形堆叠图
    fig1,ax1 = plt.subplots(nrows=1,ncols=1)
    ax1.bar(x, y_normal, color='#76FF7B', label='正常还款')
    ax1.bar(x,y_fall,bottom=y_normal,color='#FF4500', label='违约')
    ax1.legend()
    ax1.grid()
    ax1.tick_params('y',color = 'wheat')
    ax1.set_axisbelow(True)

    ax2 = ax1.twinx()
    ax2.plot(x,y_fall_by_all * 100,linewidth = 1,color = 'silver',label = '违约率')
    ax2.set_ylabel('%',color = 'coral')
    ax2.tick_params('y', labelcolor='coral')
    ax2.legend()

    plt.show()

def plot_trans():
    """
    分析交易金额的分布（区分借贷）
    :return:
    """
    data1 = trans_data[trans_data['type'] == '借']
    data2 = trans_data[trans_data['type'] == '贷']

    # 此块数据用于箭头标记
    lower_quartile1 = data1['amount'].quantile(q = 0.25,interpolation='lower')
    lower_quartile2 = data2['amount'].quantile(q = 0.25,interpolation='lower')
    upper_quartile1 = data1['amount'].quantile(q = 0.75,interpolation='higher')
    upper_quartile2 = data2['amount'].quantile(q = 0.75, interpolation='higher')

    fig1,(ax1,ax2) = plt.subplots(nrows=2,ncols=1,figsize=(8, 10),sharex=True)
    ax1.set_title('整体')
    flier_props = {
        'marker': 'o',  # 标记形状：'o'=圆圈，'.'=点，'s'=方块等
        'markerfacecolor': 'none',
        'markersize': 3,
        'markeredgecolor': 'red',
        'markeredgewidth': 1,
        'alpha': 0.8
    }
    ax1.boxplot([data1['amount'],data2['amount']],positions=[2,4],flierprops = flier_props)
    ax1.annotate(upper_quartile1, xy=(2, upper_quartile1), xytext=(3, 20000),
                 arrowprops=dict(width=1, shrink=0.05, headwidth=3, color='black'))
    ax1.annotate(upper_quartile2, xy=(4, upper_quartile2), xytext=(3, 30000),
                 arrowprops=dict(width=1, shrink=0.05, headwidth=3, color='black'))
    ax1.spines['bottom'].set_visible(False)
    ax1.grid()

    ax2.set_ylim(0,400)
    ax2.set_title('局部')
    ax2.spines['top'].set_visible(False)
    ax2.annotate(lower_quartile1,xy = (2,lower_quartile1),xytext = (3,100),
                 arrowprops=dict(width = 1,shrink = 0.05,headwidth = 3,color = 'black'))
    ax2.annotate(lower_quartile2,xy = (4,lower_quartile2),xytext = (3,200),
                 arrowprops=dict(width = 1,shrink = 0.05,headwidth = 3,color = 'black'))
    ax2.boxplot([data1['amount'],data2['amount']],positions=[2,4],tick_labels=["借","贷"])
    ax2.grid()

    trans_data['date'] = trans_data['date'].sort_values(ascending=True)
    amount_sum = trans_data.groupby('date')['amount'].sum()
    fig3,ax3 = plt.subplots(nrows=1,ncols=1,dpi = 300)
    ax3.set_title("不同时间的交易量")
    for i in range(1993,1999):
        data3 = trans_data.loc[trans_data['date'].dt.year == i]
        x = data3['date'].dt.dayofyear.unique()
        y= amount_sum[amount_sum.index.year == i]
        ax3.plot(x,y,label = f'{i}年',alpha = 0.7)
    ax3.set_xticks(np.cumsum([0,31,28,30,31,30,31,31,30,31,30,31]))
    ax3.set_xticklabels([f'{i}月' for i in range (1,13)])
    ax3.legend()
    ax3.grid()

    plt.show()

def plot_order():
    """
    分析定期支付类型（k_symbol）的分布
    :return:None
    """
    data1 = order_data.groupby('k_symbol').size()

    fig1,ax1 = plt.subplots(nrows=1,ncols=1)
    ax1.pie(data1.values,shadow=True,explode=[0.02] *  len(data1),autopct='%.2f%%',labels = data1.index)
    ax1.legend()

    plt.show()

def plot_card_rela_client():
    """
    分析不同性别客户持有信用卡的比例
    :return: None
    """
    data1 = pd.merge(clients_data,disp_data,on='client_id',how='inner') [['sex','disp_id']]
    data2 = pd.merge(data1,card_data,on = 'disp_id',how="inner")[['sex','type']]
    data3 = data2.groupby(['sex','type']).size()

    golden_w = data3.loc[('女','金卡')]
    golden_m = data3.loc[('男','金卡')]
    teenager_w = data3.loc[('女','青年卡')]
    teenager_m = data3.loc[('男','青年卡')]
    normal_w = data3.loc[('女','普通卡')]
    normal_m = data3.loc[('男','普通卡')]

    normal_ls = np.array([normal_w, normal_m])
    teenager_ls = np.array([teenager_w , teenager_m])
    golden_ls = np.array([golden_w,golden_m])

    fig1,ax1 = plt.subplots(nrows=1,ncols=1)
    ax1.bar(['女','男'],normal_ls,label = ['女性持有普通卡总数量','男性持有普通卡总数量'])
    ax1.bar(['女','男'],teenager_ls,bottom = normal_ls,label = ['女性持有青年卡总数量','男性持有青年卡总数量'])
    ax1.bar(['女','男'],golden_ls,bottom = teenager_ls + normal_ls,label = ['女性持有金卡总数量','男性持有金卡总数量'])
    ax1.legend(loc = "lower left")
    ax1.grid()
    ax1.set_axisbelow(True)
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

    plot_accounts()

    plot_clients()

    plot_loans()

    plot_loans_rela_district()

    plot_trans()

    plot_order()

    plot_card_rela_client()

