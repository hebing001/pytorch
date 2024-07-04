#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/4
@Description: 
"""
import pandas as pd

# 创建两个示例 DataFrame
df1 = pd.DataFrame({
    "A": ["A0", "A1", "A2"],
    "B": ["B0", "B1", "B2"]
})

df4 = pd.DataFrame({
    "A": ["A3", "A4", "A5"],
    "C": ["C3", "C4", "C5"]
})

# 使用 pd.concat 进行拼接
# result = pd.concat([df1, df4], ignore_index=True, sort=False)
# result = pd.concat([df1, df4], sort=False)
result1 = pd.concat([df1, df4], axis=1, sort=False)
result2 = pd.concat([df1, df4], axis=1, sort=False,ignore_index=True)
print(result1)
print(result2)


