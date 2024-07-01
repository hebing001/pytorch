
import numpy as   np
t1 = np.arange(12)
print(t1)

print(t1.shape)
#分割线
print("-------------------------------")
# 二维数组
t2 = np.array([[1,2,3],[4,5,6]])
print(t2)
print(t2.shape)

#分割线
print("-------------------------------")
# 三维数组
t3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(t3)
print(t3.shape)


#分割线
print("-------------------------------")
#修改 shape
t4 = np.reshape(t1,(3,4))
print(t4)
print(t4.shape)
print(t1)
print("-------------------------------")


#变成一维
t5 = t1.reshape((12,))
print(t5)

#打印分割线
print("-------------------------------")
#临时变量
temp = t1.reshape((12,1))
print(temp)

#打印分割线
print("-------------------------------")
#二维
temp1 = t1.reshape((1,12))
print(temp1)


#打印分割线
print("-------------------------------")
#三维
temp2 = t1.reshape((2,2,3))
print(temp2)
#打印分割线
print("-------------------------------")

print(t2)
print(t2.ndim)


#打印分割线
print("-------------------------------")
t6 = np.array([1,0,1,1,0,1],dtype=bool)
print(t6)

# 打印分割线
print("-------------------------------")
# 二维数组
temp = np.array([[1,2,3],[4,5,6]])
print(temp)
temp2 = temp.flatten()
print(temp2)

