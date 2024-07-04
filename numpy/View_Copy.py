import timeit
from functools import partial

import numpy as np


def get_run_time(func, *args):
    repeat = 3
    number = 200
    return min(timeit.Timer(partial(func, *args)).repeat(repeat=repeat, number=number)) / number


a = np.random.rand(1000, 1000)
b = np.random.rand(1000, 1000)

def f1():
    global b
    # 这会产生新的 b
    b = 2*b

def f2():
    global a
    # 这不会产生新的 a
    a *= 2    # 和 a[:] *= 2 一样

print('%.6f - b = 2*b' % get_run_time(f1))
print('%.6f - a *= 2' % get_run_time(f2))