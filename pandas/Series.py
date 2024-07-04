#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/3
@Description: 
"""
import pandas as pd

l = [11,22,33]
s = pd.Series(l)
print("list:", l)
print("series:", s)

list_data = list(range(-4, 4))
s1 = pd.Series(
  list_data,
  index=list("abcdefgh"))

print("\n", s1)

print(s1.loc[s1.index[[3,2]]])

print(s1.index[[3,2]])
print("按条件过滤筛选1")
print(s1.loc[s1 < 3], "\n")
print("按条件过滤筛选2")
print(type(s1 < 3))

print(s1.iloc[(s1 < 3).values], "\n")
