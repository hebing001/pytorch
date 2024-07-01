# # 副本和视图
#
# import numpy as np
#
# a = np.arange(6)
# print('我们的数组是：')
# print(a)
# print('调用 id() 函数：')
# print(id(a))
# print('a 赋值给 b：')
# b = a
# print(b)
# print('b 拥有相同 id()：')
# print(id(b))
# print('修改 b 的形状：')
# b.shape = 3, 2
# print(b)
# print('a 的形状也修改了：')
# print(a)

import numpy as np

# 最开始 a 是个 3X2 的数组
a = np.arange(6).reshape(3, 2)
print('数组 a：')
print(a)
print('创建 a 的视图：')
b = a.view()
print(b)
print('两个数组的 id() 不同：')
print('a 的 id()：')
print(id(a))
print('b 的 id()：')
print(id(b))

a[0][1] = 123
print(a)
print(b)


arr = np.arange(12)
print ('我们的数组：')
print (arr)
print ('创建切片：')
a=arr[3:]
b=arr[3:]
a[1]=123
b[2]=234
print(arr)
print(a)
print(b)
print(id(a),id(b),id(arr[3:]))