#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/3
@Description: 
"""
import pandas as pd
df = pd.DataFrame([
  [1,2],
  [3,4]
])
print(df)
print(df[0])
print(df[1])
print(df.at[0,0])

df = pd.DataFrame({"col1": [1,3], "col2": [2, 4]})
print(df)
print(df["col1"])

print("取出来之后的数据")
print(df.loc[0, "col1"])
print(df.loc[0, "col2"])

print(df["col1"])
print(type(df["col1"]))
print(type)
df = pd.DataFrame({"col1": pd.Series([1,3]), "col2": pd.Series([2, 4])})

print(df)
