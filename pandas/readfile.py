#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/3
@Description: 
"""
import chardet
import pandas as pd

df = pd.read_excel("data/体检数据.xlsx", index_col=0)

print(df)

df.loc[2, "体重"] = 1
print(df)
df.to_excel("data/体检数据_修改.xlsx")

f = open(r"data/体检数据_修改.xlsx",'rb')
its_code = f.read()
print(chardet.detect(its_code))

print("读取 csv 文件")
df2 = pd.read_excel("data/体检数据_修改.xlsx", index_col=0)
print(df2)
df = pd.read_clipboard()
print(df)
