---
License:
    - CC-BY-NC 署名-禁止商用

Ext:
    - .xlsx
---

## **背景描述**
数据集为两个Excel文件，其中test为某次A/B测试相关数据，city为某城市运营数据。

## **数据说明**
**test.xlsx**

date：日期
group：组别（控制组/实验组）
requests：订单请求数
gmv：成交总额
coupon per trip：每单优惠券金额
trips：订单数
canceled requests：取消请求数

**city.xlsx**

date：日期
hour：时点
requests：请求数
trips：订单数
supply hours：可服务时长
average minutes of trips：平均订单时长（分钟）
pETA：顾客预计等待时长
aETA：顾客实际等待时长
utiliz：司机在忙率

## **数据来源**
数据来自滴滴出行内部

## **问题描述**
可以使用该数据来做A/B测试效果分析与城市运营分析。