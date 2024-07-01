#广播机制
#二维数组

import numpy as np
t1 = np.array([[1,2,3],[4,5,6]])
t2 = t1 + 2
print(t1)
#分割线
print("-------------------------------")
print(t2)

#二行三列
t3 = np.array([[1,2,3],[4,5,6]])
print(t3)
print("-------------------------------")
t3 = t3 + t1
print(t3)


temp = np.array([1,2,3])
print(temp)
print(t1-temp)
print("-------------------------------")
temp2 = np.array([[1],[2]])
print(temp2)
print(t1-temp2)