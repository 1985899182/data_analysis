---
Topic:
    - 旅游

Field:
    - 数据挖掘
,    - 分类

License:
    - 其他 - 在文档说明

Ext:
    - .csv

DatasetUsage:
    - 839522
---

## **背景描述**
本数据集提供了某旅游网站上客户行为的各种信息。
这些数据对于理解用户的旅游习惯、偏好以及与旅游内容的互动方式非常重要，对于旅游网站在市场营销、用户体验优化以及新服务开发等方面具有重要的参考价值。通过分析这些数据，旅游公司可以更有效地满足客户需求，提升服务质量，同时增强用户的参与度和忠诚度。

![Image Name](https://cdn.kesci.com/upload/image/s49ij3n0wi.png?imageView2/0/w/640/h/640)

## **数据说明**

| 变量 | 描述 |
|---|---|
| UserID | 用户的唯一ID |
| Buy_ticket | 下个月购买机票（目标变量）|
| Yearly_avg_view_on_travel_page | 用户每年在旅行相关页面的平均浏览次数 |
| preferred_device | 用户登录的首选设备 |
| total_likes_on_outstation_checkin_given | 用户在过去一年对外站签到给予的总点赞数 |
| yearly_avg_Outstation_checkins | 用户平均每年的外站签到次数 |
| member_in_family | 用户账户中提及的家庭成员总数 |
| preferred_location_type | 用户旅行的首选地点类型 |
| Yearly_avg_comment_on_travel_page | 用户每年在旅行相关页面的平均评论数 |
| total_likes_on_outofstation_checkin_received | 用户在过去一年收到的外站签到总点赞数 |
| week_since_last_outstation_checkin | 用户最后一次外站签到更新以来的周数 |
| following_company_page | 客户是否关注公司页面（是或否）|
| montly_avg_comment_on_company_page | 用户每月在公司页面的平均评论数 |
| working_flag | 客户是否在工作 |
| travelling_network_rating | 表明用户是否有喜欢旅行的密切朋友的评级。1是最高，4是最低 |
| Adult_flag | 客户是否为成人 |
| Daily_Avg_mins_spend_on_traveling_page | 用户在公司旅行页面上的平均每日花费时间 |

## **数据来源**
https://www.kaggle.com/datasets/ddosad/customer-behaviour-tourism-portal

## **问题描述**
1. **用户购买行为分析**：
通过分析`Buy_ticket`字段，可以识别出购买机票的用户特征，比如他们的旅行页面浏览次数、签到行为等。这有助于识别潜在的购票客户，从而针对性地制定营销策略。

2. **用户偏好分析**：
通过研究`preferred_device`、`preferred_location_type`等字段，可以了解用户在设备使用和旅行地点选择上的偏好，帮助优化网站或应用的用户体验设计。

3. **社交互动行为分析**：
通过`total_likes_on_outstation_checkin_given`、`Yearly_avg_comment_on_travel_page`等数据，可以分析用户在社交互动方面的行为模式，比如用户对于旅行内容的参与度和反馈。

4. **客户忠诚度和参与度分析**：
利用`week_since_last_outstation_checkin`、`following_company_page`等字段，可以评估用户对旅游网站或应用的忠诚度和参与度。

5. **人口统计特征与旅游行为的关系**：
分析`Adult_flag`、`member_in_family`等人口统计数据与其他旅游行为数据的关系，了解不同人群的旅游习惯和需求。