---
Topic:
    - 商业金融

Field:
    - 数据挖掘

License:
    - CC0 公共领域共享

Ext:
    - .csv

DatasetUsage:
    - 258595
---

## **背景描述**
在人力资源管理领域中，分析各项员工工作相关的数据和指标，可以揭示员工流失的趋势和原因、薪酬公平性、员工满意度以及职业发展路径等关键指标。这些见解对于优化人才招聘、留存策略、绩效评估体系和员工发展计划至关重要。
通过对这些多维数据的深入分析，组织可以制定更加人性化的管理措施，改进工作环境，提高员工的工作满意度和忠诚度，从而推动组织的整体业绩和竞争力。此外，分析结果还支持制定更加公正和激励性的薪酬体系，以吸引和保留顶尖人才，确保组织的长期成功和可持续发展。

![Image Name](https://cdn.kesci.com/upload/image/s3wfb2vvqm.png?imageView2/0/w/640/h/640)


## **数据说明**
| 字段            | 说明                                          |
|-----------------|-----------------------------------------------|
| EmpID           | 唯一的员工ID                           |
| Age             | 年龄                                 |
| AgeGroup        | 年龄组                               |
| Attrition       | 是否离职                                          |
| BusinessTravel  | 出差：很少、频繁、不出差                   |
| DailyRate       | 日薪                               |
| Department      | 任职部门：研发部门、销售部门、人力资源部门                    |
| DistanceFromHome| 通勤距离                         |
| Education       | 教育等级                               |
| EducationField  | 专业领域：生命科学、医学、市场营销、技术、其他            |
| EnvironmentSatisfaction  | 工作环境满意度    |
| Gender                   | 性别       |
| HourlyRate               | 时薪       |
| JobInvolvement           | 工作参与度    |
| JobLevel                 | 工作级别     |
| JobRole                  | 工作角色     |
| JobSatisfaction          | 工作满意度    |
| MaritalStatus            | 婚姻状况     |
| MonthlyIncome            | 月收入      |
| SalarySlab               | 工资单      |
| MonthlyRate              | 月薪       |
| NumCompaniesWorked       | 工作过的公司数量 |
| PercentSalaryHike        | 加薪百分比    |
| PerformanceRating        | 绩效评级     |
| RelationshipSatisfaction | 关系满意度    |
| StandardHours            | 标准工时     |
| StockOptionLevel         | 股票期权级别    |
| TotalWorkingYears        | 总工作年数     |
| TrainingTimesLastYear    | 去年培训时间    |
| WorkLifeBalance          | 工作生活平衡评价    |
| YearsAtCompany           | 在公司工作年数   |
| YearsInCurrentRole       | 担任现职年数    |
| YearsSinceLastPromotion  | 上次晋升后的年数  |
| YearsWithCurrManager     | 与现任经理共事年数 |


## **数据来源**
https://www.kaggle.com/datasets/anshika2301/hr-analytics-dataset

## **问题描述**
员工流失分析
   - 识别导致员工离职的因素（Attrition与其他字段的关系，如满意度、工资、通勤距离等）。
   - 分析不同年龄组、婚姻状况、工作年数与离职率之间的关系。

薪酬公平性研究
   - 比较不同性别（Gender）、教育等级（Education）和专业领域（EducationField）的薪资差异。
   - 探讨工作级别（JobLevel）、工作角色（JobRole）与月收入（MonthlyIncome）、时薪（HourlyRate）、日薪（DailyRate）之间的关系。

工作满意度分析
   - 评估工作满意度（JobSatisfaction）、工作环境满意度（EnvironmentSatisfaction）、关系满意度（RelationshipSatisfaction）与员工绩效（PerformanceRating）之间的关联。
   - 分析工作生活平衡评价（WorkLifeBalance）与工作参与度（JobInvolvement）、在公司工作年数（YearsAtCompany）之间的关系。

职业发展和晋升路径分析
   - 检查晋升历史（YearsSinceLastPromotion）与工作满意度、工作级别和绩效评级之间的关联。
   - 分析员工在当前角色的时间（YearsInCurrentRole）对于工作参与度和晋升机会的影响。

培训和发展需求评估
   - 评估培训次数（TrainingTimesLastYear）与员工绩效评级的关系。
   - 分析工作经验（TotalWorkingYears）与培训需求之间的关系。

员工福利和激励措施分析
   - 探索股票期权级别（StockOptionLevel）对员工留存的影响。
   - 分析加薪百分比（PercentSalaryHike）与员工满意度和绩效的关系。

人力资源规划和预测
   - 预测哪些因素会影响员工留存（如工资、工作满意度、工作环境）。
   - 用历史数据建模，预测员工晋升路径和潜在的流失风险。