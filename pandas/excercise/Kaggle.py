#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/4
@Description: 
"""
import pandas as pd

df = pd.read_csv("../data/archive/day_wise.csv")
print(df.head())

print("日期列表摘取：\n", df["Date"][:4])
print(
    "日期->索引转换：\n",
    df[df["Date"] == "2020-02-03"]
)

# print(df["Date"] == "2020-02-03")


confirmed0124 = df.loc[df["Date"] == "2020-01-24", "Confirmed"]
print("截止 1 月 24 日的累积确诊数：", confirmed0124.values)

print((df["Date"]))
date = pd.to_datetime(df["Date"])
print((date))

date_range = (date >= "2020-01-25") & (date <= "2020-07-22")
new_cases = df.loc[date_range, "New cases"]
overall = new_cases.sum()
print("共新增：", overall)


print(df.loc[df["Date"] == "2020-07-22"].index)
print(df.loc[df["Date"] == "2020-01-25"].index.item())
