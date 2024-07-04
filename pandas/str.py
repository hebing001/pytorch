#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/4
@Description: 
"""
import pandas as pd

# 创建一个包含三个字符串元素的列表
py_s = ["a_b_c", "jill_jesse", "frank"]

# 将列表转换为 pandas 的 Series 对象
pd_s = pd.Series(py_s, dtype="string")

# 使用 Python 的 split 方法进行分割
print("python split:\n", [s.split("_") for s in py_s])

# 使用 pandas 的 str.split 方法进行分割
print("\npandas split:\n", pd_s.str.split("_"))
print("\npandas split:\n", pd_s.str.split("_", expand=True))


pd_df = pd.DataFrame([["a", "b"], ["C", "D"]])
