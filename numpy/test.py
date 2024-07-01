# #
#
# # 列表示例
# list1 = [1, 2, 3]
# list2 = list1    # 赋值操作
#
# list2[0] = 100    # 修改list2的第一个元素
#
# print("list1:", list1)    # 输出：list1: [100, 2, 3]
# print("list2:", list2)    # 输出：list2: [100, 2, 3]
#
# # 元组示例
# tuple1 = (1, 2, 3)
# tuple2 = tuple1    # 赋值操作
#
# # 元组是不可变对象，无法修改元素
#
# print("tuple1:", tuple1)    # 输出：tuple1: (1, 2, 3)
# print("tuple2:", tuple2)    # 输出：tuple2: (1, 2, 3)
#
# # 字典示例
# dict1 = {"a": 1, "b": 2}
# dict2 = dict1    # 赋值操作
#
# dict2["a"] = 100    # 修改dict2的键为"a"的值
#
# print("dict1:", dict1)    # 输出：dict1: {'a': 100, 'b': 2}
# print("dict2:", dict2)    # 输出：dict2: {'a': 100, 'b': 2}


# 不复制，a 和 b 指向同一个对象
a = [1, 2, 3]
b = a
b[0] = 100
print(a)  # 输出: [100, 2, 3]
print(b)  # 输出: [100, 2, 3]

# 视图，切片操作，创建新的对象 a，但数据仍由原对象保管
a = [1, 2, 3, 4, 5]
b = a[1:]
b[0] = 100
print(a)  # 输出: [1, 2, 3, 4, 5]
print(b)  # 输出: [100, 2, 3, 4, 5]



