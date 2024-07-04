#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/4
@Description: 
"""
import pandas as pd

s = pd.Series(
  ["小米", "小明",      # 一年一班
   "小命", "小勉",      # 一年二班
   "小牛", "小鸟",      # 二年一班
   "小南", "小妮"       # 二年二班
   ], name="name")

print(s)

tuples = [
  # 年级，班级
  ("one", "1"),
  ("one", "1"),
  ("one", "2"),
  ("one", "2"),
  ("two", "1"),
  ("two", "1"),
  ("two", "2"),
  ("two", "2"),
]
index = pd.MultiIndex.from_tuples(
  tuples, names=["grade", "class"])

print(index)

s = pd.Series(
    ["小米", "小明",      # 一年一班
     "小命", "小勉",      # 一年二班
     "小牛", "小鸟",      # 二年一班
     "小南", "小妮"       # 二年二班
     ],
    name="name",
    index=index)
print(s)
print(s.index)