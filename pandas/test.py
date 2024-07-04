#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/3
@Description: 
"""
import pandas as pd

df = pd.DataFrame([[1, 2, 3, 0],
                   [3, 4, None, 1],
                   [None, None, None, None],
                   [None, 3, None, 4]],
                  columns=list("ABCD"))
print(df)
print("\nisnull():\n", df.isnull())  # True 就是空
print("\nnotnull()\n", df.notnull())  # False 为空

print("默认：\n", df.dropna())  # 默认按 axis=0
print("\naxis=1:\n", df.dropna(axis=1))  # 可以换一个 axis drop
