# 轴    CSV文件
import numpy as np
import os

file_path1 = r'/archive/USvideos.csv'
file_path2 = r'/archive/GBvideos.csv'
file_path3 = r'/archive/test.csv'

#读取文件
with open(file_path3, 'r', encoding='utf-8') as f:
    t1 = np.loadtxt(f, delimiter=',', dtype='str')

#读取文件
with open(file_path3, 'r', encoding='utf-8') as f:
    temp = np.loadtxt(f, delimiter=',', dtype='str',unpack=True)

print(t1)
print("-------------------------------")
print(temp)


t2 = np.arange(24).reshape(4,6)
print(t2)
print("-------------------------------")
temp = t2.transpose()
print(temp)
print(t2.T)
print("-------------------------------")
print(t2.swapaxes(1,0))

#清理控制台输出


print(t1)
print("-------------------------------")
print(t1.shape)
print("-------------------------------")
print(t1[1])

print("-------------------------------")
print(t1[2:])
print("-------------------------------")
print(t1[[0,3]])

print("-------------------------------")
print(t1[:,1])

print("-------------------------------")
print(t1[1,:])
print("-------------------------------")
print(t1[:,2:])

print("-------------------------------")
print(t1[:,[0,2]])

print(t1)
#取多行多列
print("-------------------------------")
print(t1[1:3,1:3])

print(t1[0:3])

print("-------------------------------")
print(t1[[2,3,6],[1,3,1]])

print("-------------------------------")
print(t1[1,1])