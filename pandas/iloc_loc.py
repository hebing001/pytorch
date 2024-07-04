#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/3
@Description: 
"""
import pandas as pd

# 创建一个示例 DataFrame
data = {'A': [-12, 15, 17, -5],
        'B': [20, -2, 30, -8],
        'C': [25, -10, 35, -15]}
df = pd.DataFrame(data)

# 创建一个布尔 Series
condition = df.iloc[0] < -10  # 选择第0行中小于-10的元素，返回布尔 Series
print(condition)
# 输出:
# A     True
# B    False
# C    False
# Name: 0, dtype: bool

# 使用布尔 Series 选择列
print(df.loc[:, condition])
# 输出:
#     A
# 0 -12
# 1  15
# 2  17
# 3  -5


print(df.iloc[:, condition])