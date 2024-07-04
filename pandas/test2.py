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
                   [3, 5, 2, 1],
                   [3, 2, 2, 3]],
                  columns=list("ABCD"))
print(df)
print("\nidxmax():\n", df.idxmax())
print("\nidxmax(skipna=False):\n", df.idxmax(skipna=False))
print("\nidxmin():\n", df.idxmin())
