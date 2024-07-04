#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/4
@Description: 
"""
import pandas as pd

left = pd.DataFrame({
    "key1": ["K0", "K0", "K1", "K2"],
    "key2": ["K0", "K1", "K0", "K1"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
})
print(left)

right = pd.DataFrame({
    "key1": ["K0", "K1", "K1", "K2"],
    "key2": ["K0", "K0", "K0", "K0"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
})
print(right)
#判断left和right第一列是否相等
print("-------------------------------")
print(left["key1"] == right["key1"])


print("-------------------------------")

# 比较 key1 列
comparison_key1 = left["key1"] == right["key1"]
print("\nElement-wise comparison for key1:\n", comparison_key1)

# 比较 key2 列
comparison_key2 = left["key2"] == right["key2"]
print("\nElement-wise comparison for key2:\n", comparison_key2)

# 将 key1 和 key2 列的比较结果按位与
comparison_both = comparison_key1 & comparison_key2
print("\nElement-wise comparison for both key1 and key2:\n", comparison_both)
