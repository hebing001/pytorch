#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/4
@Description: 
"""

import pandas as pd
import numpy as np

# 创建示例 DataFrame
data = {
    "A": ["A0", "A1", "A2", "A3", np.nan, np.nan],
    "B": ["B0", "B1", "B2", "B3", np.nan, np.nan],
    "C": ["C0", "C1", "C2", "C3", np.nan, np.nan],
    "D": ["D0", "D1", "D2", "D3", np.nan, np.nan],
    "B": [np.nan, np.nan, "B2", "B3", "B6", "B7"],
    "D": [np.nan, np.nan, "D2", "D3", "D6", "D7"],
    "F": [np.nan, np.nan, "F2", "F3", "F6", "F7"]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 使用 .add_suffix 或 .add_prefix 添加后缀或前缀来区分重复列
df.columns = [f"{col}_{i}" for i, col in enumerate(df.columns)]
print("\nDataFrame with unique column names:\n", df)

# 通过标准索引访问列
print("\nAccessing a column (e.g., B_1):")
print(df["B_1"])

# 通过 loc 访问特定行
print("\nAccessing a specific row (e.g., row index 2):")
print(df.loc[2])
