#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/4
@Description: 
"""
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "a": [1, None, 1],
    "b": [np.nan, 4, 4]
})
print(df)
print("skipped NaN:\n", df.mean(axis=0))
print("\n\nnot skipped:\n", df.mean(axis=0, skipna=False))


df = pd.DataFrame({
    "a": [1, None, 3, None],
    "b": [4, 8, 12, 12]
})
print(df)

a_nan = df["a"].isna()
print("a_nan\n",a_nan)

a_new_value = df["b"][a_nan] / 4
print("a_new_value\n",a_new_value)


new_col = df["a"].fillna(a_new_value)
df["a"] = new_col

