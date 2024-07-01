import numpy as np

file_path1 = r'/archive/test.csv'
t1 = np.loadtxt(file_path1, delimiter=',', dtype='int')
print(t1)
print(t1.dtype)

print(t1<10)
#小于10的都变成零
t1[t1<10] = 0
# print((t1[t1<10] = 0))
print(t1)
print("nmpy.where()函数的使用：")

temp = np.where(t1<10,20,30)
print(t1)
print(temp)