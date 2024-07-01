#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Hebing
@Date: 2024/6/28
@Description: 学习numpy库
"""
import random

#导入numpy库
import numpy as np

t1= np.array([1, 2, 3])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)
print(type(t2))

t3 = np.arange(10)
print(t3)
print(type(t3))

print(t3.dtype)
t4 = np.array(range(1, 4), dtype=float)
print(t4)
print(t4.dtype)

t5 = np.array([1, 0, 1, 1, 0, 1], dtype=bool)
print(t5)
print(t5.dtype)

t6 = t5.astype("int8")
print(t6)
print(t6.dtype)

print("-----------------------------------")

print(t5)


# print([random.random() for i in range(10)])

t7 = np.array([random.random() for i in range(10)])
print(t7)

t8 = np.round(t7, 2)
print(t8)
