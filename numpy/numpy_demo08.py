# 给上开头的注释
import numpy as np

file1 = r'E:\A_项目\demo\pytorch\demo01\archive\test.csv'
file2 = r'E:\A_项目\demo\pytorch\demo01\archive\test2.csv'
t1 = np.loadtxt(file1, delimiter=',', dtype='int')
t2 = np.loadtxt(file2, delimiter=',', dtype='int')
print(t1)
print("-------------------------------")
print(t2)


temp = np.zeros((t1.shape[0], 1),dtype='int')
print(temp)

temp2 = np.zeros((t2.shape[0], 1),dtype='int')+1
print(temp2)
#t1拼接上temp
t1 = np.hstack((t1,temp))
print(t1)

#t2拼接上temp
t2 = np.hstack((t2,temp2))
print(t2)

print("-------------------------------")
final_data = np.vstack((t1,t2))
print(final_data)

