import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
data = np.random.randn(1000)
print(data)
# 绘制直方图
plt.hist(data, bins=30, alpha=0.75, color='blue', edgecolor='black')

# 添加标题和标签
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 显示图形
plt.show()
