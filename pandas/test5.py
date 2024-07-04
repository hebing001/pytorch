#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/4
@Description: 
"""
import pandas as pd

df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

df4 = pd.DataFrame({
    'B': [10, 11],
    'A': [12, 13],
    'D': [14, 15]
})

result1 = pd.concat([df4, df1], ignore_index=True, sort=False)
print(result1)
result2 = pd.concat([df4, df1], ignore_index=True, sort=True)
print(result2)

result3 = pd.concat([df1, df4], ignore_index=True, sort=False)
print(result3)
result4 = pd.concat([df1, df4], ignore_index=True, sort=True)
print(result4)


