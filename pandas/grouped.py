#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/4
@Description: 
"""
import pandas as pd

df = pd.DataFrame(
    [
        ("小红", "哈利波特", 80),
        ("小明", "蜘蛛侠", 72),
        ("小红", "雷神", 83),
        ("小红", "雷神", 90),
        ("小红", "蜘蛛侠", 45),
        ("小明", "超人", 57),
    ],
    columns=("人", "人物", "评价"),
)

grouped = df.groupby("人")

#循环展示分组信息
for name, group in grouped:
    print(name)
    print(group)

print(grouped["评价"].mean())

print("----------------------------------------")

for name, group in grouped["评价"]:
    print("name:", name)
    print(group)