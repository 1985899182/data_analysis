---
Topic:
    - 农业
,    - 植物

Field:
    - 预测
,    - 数据挖掘
,    - 回归

License:
    - CC-BY 4.0 转载需署名

Ext:
    - .csv

DatasetUsage:
    - 2834940
---

## **背景描述**
蓝莓在全球范围内备受欢迎，其独特的风味和丰富的营养价值令消费者为之倾倒。蓝莓生长对适宜气候和土壤的依赖，因此主要分布于北美、欧洲、澳洲等地区。

野生蓝莓养殖目前正处于蓬勃发展的阶段，吸引了越来越多的投资者和农户投身其中。全球对健康食品的需求不断增加，野生蓝莓以其天然的营养价值和丰富的抗氧化物质而备受瞩目。然而，养殖野生蓝莓也面临一系列挑战，包括气候不稳定、疾病威胁和市场价格波动。因此，成功的野生蓝莓养殖需要不断的创新和可持续的农业实践，以满足日益增长的全球市场需求。

蓝莓是多年生开花植物，浆果呈蓝色或紫色。它们被归类于越橘属中的蓝越橘科。越橘还包括小红莓、山桑子、胡越橘和马德拉蓝莓。商业蓝莓--野生（低丛）和栽培（高丛）--均原产于北美洲。高丛品种在 20 世纪 30 年代引入欧洲。

蓝莓通常是匍匐灌木，高度从 10 厘米（4 英寸）到 4 米（13 英尺）不等。在蓝莓的商业生产中，生长在低矮灌木丛中、浆果较小、豌豆大小的品种被称为 "低丛蓝莓"（与 "野生 "同义），而生长在较高、栽培灌木丛中、浆果较大的品种被称为 "高丛蓝莓"。加拿大是低丛蓝莓的主要生产国，而美国生产的高丛蓝莓约占全球供应量的 40%。

![Image Name](https://cdn.kesci.com/upload/image/s4z3z27c64.png?imageView2/0/w/640/h/640)


## **数据说明**

| 字段 | 说明 |
|-|-|  
| Clonesize* | 蓝莓克隆平均大小,单位：$m^2$  |
| Honeybee | 蜜蜂密度（单位：$蜜蜂/m^2/分钟$ ） |  
| Bumbles | 大型蜜蜂密度（单位：$大型蜜蜂/m^2/分钟$ ） |
| Andrena | 安德烈纳蜂密度（单位：$安德烈纳蜂/m^2/分钟$ ） |
| Osmia | 钥匙蜂密度（单位：$钥匙蜂/m^2/分钟$ ） |
| MaxOfUpperTRange |花期内最高温带日平均气温的最高记录,单位：${^{\circ}C}$ |
| MinOfUpperTRange |  花期内最高温带日平均气温的最低记录,单位：${^{\circ}C}$ | 
| AverageOfUpperTRange | 花期内最高温带日平均气温,单位：${^{\circ}C}$ |
| MaxOfLowerTRange | 花期内最低温带日平均气温的最高记录,单位：${^{\circ}C}$ |  
| MinOfLowerTRange | 花期内最低温带日平均气温的最低记录,单位：${^{\circ}C}$ |
| AverageOfLowerTRange | 花期内最低温带日平均气温,单位：${^{\circ}C}$ |
| RainingDays | 花期内降雨量大于 0 的日数总和,单位：天 |
| AverageRainingDays | 花期内降雨日数的平均值,单位：天 |
|fruitset|果实集|
|fruitmass|果实质量|
|seeds|种子数|

注：
Clonesize 表示每个蓝莓克隆株的平均占地面积大小。
蓝莓克隆(Blueberry clone)指的是蓝莓的克隆体。蓝莓繁殖和种植主要有两种方式:
1. 种子育种。从蓝莓果实中提取种子,播种育苗。这种方式育出来的蓝莓植株遗传特征会有很大变异。
2. 克隆繁殖。选取优良品种蓝莓母株,通过组织培养等焉条繁殖出基因特征高度一致的克隆蓝莓株。这种子植出来的蓝莓园,每个蓝莓株的性状和产量会趋于一致。
所以蓝莓克隆就指的是通过无性繁殖方式培育出来的蓝莓株。整个蓝莓园被同一个蓝莓品种的克隆株占满。

## **数据来源**
```
Qu, Hongchun; Obsie, Efrem; Drummond, Frank (2020), “Data for: Wild blueberry yield prediction using a combination of computer simulation and machine learning algorithms”, Mendeley Data, V1, doi: 10.17632/p5hvjzsvn8.1
```

## **问题描述**
* 蓝莓克隆大小与其他因素的关系分析
可以通过统计分析和数据可视化，探讨蓝莓克隆平均大小（Clonesize）与其他因素之间的关系

* 气温与蓝莓生长的关系分析
可以使用最高温带日平均气温（MaxOfUpperTRange、MinOfUpperTRange、AverageOfUpperTRange）和最低温带日平均气温（MaxOfLowerTRange、MinOfLowerTRange、AverageOfLowerTRange）等气象数据，分析它们与蓝莓果实集（fruitset）、果实质量（fruitmass）以及种子数（seeds）之间的关联

* 降雨对蓝莓生长的影响分析
使用降雨数据（RainingDays、AverageRainingDays），可以研究降雨对蓝莓的生长和生产是否有影响

* 机器学习预测模型
预测蓝莓克隆大小、果实集、果实质量或种子数等目标变量