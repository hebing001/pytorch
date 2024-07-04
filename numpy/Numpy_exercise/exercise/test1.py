#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/3
@Description: 
"""
import numpy as np

with open("covid19_day_wise.csv", "r", encoding="utf-8") as f:
    data = f.readlines()

covid = {
    "date": [],
    "data": [],
    "header": [h for h in data[0].strip().split(",")[1:]]
}

for row in data[1:]:
    split_row = row.strip().split(",")
    covid["date"].append(split_row[0])
    covid["data"].append([float(n) for n in split_row[1:]])



# print(covid["header"])

# print(covid["date"])
# print(covid["data"])


print("日期列表摘取：", covid["date"][:4])

date_idx = covid["date"].index("2020-02-03")
print("日期->索引转换：", date_idx)

data = np.array(covid["data"])

for header, number in zip(covid["header"], data[date_idx]):
    print(header, ":", number)

