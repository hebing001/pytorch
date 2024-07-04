#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/4
@Description: 
"""
import pandas as pd
import numpy as np
nd = np.array([[1, 2], [3, 4], [5, 6]])

df = pd.DataFrame(nd, columns=['A', 'B'])
print(df)

# def func(x):
#     return x[0] * 2, x[1] * -1

# df.apply(func, axis=1, result_type='expand')

# print("apply")
#
# print(df.apply(func, axis=1, result_type='expand'))
#
# print("expand")
# # print(df.apply(func, axis=1))
#
# print(type(func([1, 2])))

def func(r):
    return r[2] * 4

last_row = df.apply(func, axis=0)
print("last_row:\n", last_row)
print(type(last_row))

df.iloc[2, :] = last_row
print("\ndf:\n", df)