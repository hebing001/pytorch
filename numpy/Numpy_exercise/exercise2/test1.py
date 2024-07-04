raw_data = [
["Name", "StudentID", "Age", "AttendClass", "Score"],
["小明", 20131, 10, 1, 67],
["小花", 20132, 11, 1, 88],
["小菜", 20133, None, 1, "98"],
["小七", 20134, 8, 1, 110],
["花菜", 20134, 98, 0, None],
["刘欣", 20136, 12, 0, 12]
]
print(raw_data)
import numpy as np
data = np.array(raw_data)

#显示数据类型和数据
print(data.dtype)
print(data)
print("数据预处理")

data_process = []
for i in range(len(raw_data)):
    if i == 0:
        continue    # 不要首行字符串
    # 去掉首列名字
    data_process.append(raw_data[i][1:])
data = np.array(data_process, dtype=np.float64)
print("data.dtype", data.dtype)
print(data)

print("清洗数据")
# for i in range(data.shape[1]):
#     temp_col = data[:, i]
#     nan_num = np.count_nonzero(temp_col != temp_col)
#     if nan_num != 0:
#         print("第{}列有nan".format(i))
#         temp_col[temp_col != temp_col] = np.mean(temp_col[temp_col == temp_col])

sid = data[:, 0]

#检查学号重复情况
unique, counts = np.unique(sid, return_counts=True)
print(unique, counts)
print(unique[counts > 1])
data[4, 0] = 20135
print(data)

is_nan = np.isnan(data[:,1])
print("is_nan:", is_nan)
nan_idx = np.argwhere(is_nan)

print(~np.isnan(data[:,1]))

# 计算有数据的平均年龄，用 ~ 符号可以 True/False 对调
mean_age = data[~np.isnan(data[:,1]), 1].mean()
print("有数据的平均年龄：", mean_age)


# ~ 表示 True/False 对调，& 就是逐个做 Python and 的运算
normal_age_mask = ~np.isnan(data[:,1]) & (data[:,1] < 20)

# print("~np.isnan(data[:,1])", ~np.isnan(data[:,1]))
# print("data[:,1] < 20", data[:,1] < 20)
print("normal_age_mask:", normal_age_mask)

normal_age_mean = data[normal_age_mask, 1].mean()
print("normal_age_mean:", normal_age_mean)

data[~normal_age_mask, 1] = normal_age_mean
print("ages:", data[:, 1])

# print(data[-3:, 2:])
print(data)
# 没上课的转成 nan
print("没上课的转成 nan")
data[data[:,2] == 0, 3] = np.nan

print(data)

# 超过 100 分和低于 0 分的都处理一下
data[:, 3] = np.clip(data[:, 3], 0, 100)

print(data[:, 2:])


