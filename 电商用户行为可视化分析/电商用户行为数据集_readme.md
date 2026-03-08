---
Topic:
    - 网络电商

Ext:
    - .zip
---


## **数据说明**
第一部分是用户在商品全集上的移动端行为数据（D）,表名为tianchi_fresh_comp_train_user_2w，包含如下字段：
 字段                        字段说明                                                             提取说明
 user_id                   用户标识                                                              抽样&字段脱敏
 item_id                   商品标识                                                              字段脱敏
 behavior_type        用户对商品的行为类型                                         包括浏览、收藏、加购物车、购买，对应取值分别是1、2、3、4。
 user_geohash        用户位置的空间标识，可以为空                          由经纬度通过保密的算法生成
item_category         商品分类标识                                                       字段脱敏
time                         行为时间                                                              精确到小时级别

第二个部分是商品子集（P）,表名为tianchi_fresh_comp_train_item_2w，包含如下字段：
 字段                      字段说明                                                               提取说明
 item_id                  商品标识                                                               抽样&字段脱敏
 item_ geohash      商品位置的空间标识，可以为空                           由经纬度通过保密的算法生成
 item_category       商品分类标识                                                        字段脱敏

## **数据来源**
天池：https://tianchi.aliyun.com/competition/entrance/231522/introduction

## **问题描述**
在真实的业务场景下，我们往往需要对所有商品的一个子集构建个性化推荐模型。在完成这件任务的过程中，我们不仅需要利用用户在这个商品子集上的行为数据，往往还需要利用更丰富的用户行为数据。定义如下的符号：
U——用户集合
I——商品全集
P——商品子集，P ⊆ I
D——用户对商品全集的行为数据集合
那么我们的目标是利用D来构造U中用户对P中商品的推荐模型。