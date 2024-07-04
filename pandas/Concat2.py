#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/7/4
@Description: 
"""
import pandas as pd

df1 = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
}, index=[0, 1, 2, 3],)

new_row = pd.Series(
    ["X0", "X1", "X2", "X3"],
    index=["A", "B", "C", "D"])

print(new_row)

print("new_row.to_frame()\n", new_row.to_frame(),type(new_row.to_frame()))
print("new_row.to_frame().T\n", new_row.to_frame().T,type(new_row.to_frame().T))

print(new_row)

# var = pd.concat(

#     [df1, new_row.to_frame().T],
#     ignore_index=True)
#
# print(var)


#拼接df1和new_row
df1 = pd.concat([df1, new_row.to_frame().T], ignore_index=True)
print(df1)
