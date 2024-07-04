import numpy as np
# seed(1) 代表的就是 1 号随机序列  传入随机种子


np.random.seed(1)
print(np.random.randint(2, 10, size=3))
print(np.random.randint(2, 10, size=3))