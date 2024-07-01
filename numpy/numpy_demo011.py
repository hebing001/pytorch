# NAN和INF值
import numpy as np
# 生成一个随机数组
temp = np.random.randint(0,10,(3,4))
print(temp)
temp = temp.astype(float)

#随机加入一个NAN
temp[1,1] = np.nan
print(temp)

count = np.count_nonzero(temp!=temp)
print(count)

print(np.sum(temp,axis=0))

print("将nan替换成均值")

temp[np.isnan(temp)] = 0
print(temp)
