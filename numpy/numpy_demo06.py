import numpy as np
# file_path1 = r'E:\A_项目\demo\pytorch\demo01\archive\test.csv'
# file_path2 = r'E:\A_项目\demo\pytorch\demo01\archive\test2.csv'
#
# print()

#3维的矩阵,写出每一个数字出来
a = np.array([[[1,2,3],[4,5,6]],[[7,8,6],[10,11,12]]])
print(a)
print(a.shape)
print ('获取数组中一个值：')
print(np.where(a==6))
print(a[1,1,0])  # 为 6
print ('\n')


print ('调用 rollaxis 函数：')
b = np.rollaxis(a,2,0)
print (b)
print(b.shape)

print ('调用 rollaxis 函数：')
c = np.rollaxis(a,2,1)
print (c)
print(c.shape)
# 查看元素 a[1,1,0]，即 6 的坐标，变成 [1, 0, 1]
# 最后的 0 和 它前面的 1 对换位置
print(np.where(c==6))
print ('\n')