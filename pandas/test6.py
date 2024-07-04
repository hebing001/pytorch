#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/4
@Description: 
"""
#构建一个df
import pandas as pd
df = pd.DataFrame({
    "A": ["A0", "A1", "A2"],
    "B": ["B0", "B1", "B2"]
})
print(df)

print(df.values)