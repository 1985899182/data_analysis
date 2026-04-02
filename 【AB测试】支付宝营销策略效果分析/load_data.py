import pandas as pd
def load_data() -> dict[str,pd.DataFrame]:
    effect_data = pd.read_csv('./effect_tb.csv',names=["营销策略组编号","用户ID","是否点击","曝光顺序/次数"])
    emb_data = pd.read_csv('./emb_tb_2.csv',names=["用户ID","用户特征向量"])
    seed_data = pd.read_csv('./seed_cand_tb.csv',names=["营销策略组编号","用户ID","用户类型"])
    return {
        "effect_data" : effect_data,
        "emb_data" : emb_data,
        "seed_data" : seed_data
    }

if __name__ == "__main__":
    data = load_data()
    for key in data.keys():
        print(data[key].head())