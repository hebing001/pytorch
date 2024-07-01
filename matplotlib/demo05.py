import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.ylim(-2, 1)
plt.plot(x, y)

ax = plt.gca()  # 获取当前的坐标轴

# 隐藏右侧和顶部的坐标轴线
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置 x 轴的刻度位置
ax.xaxis.set_ticks_position('bottom')
# 将底部的坐标轴移动到数据坐标的 y=0 位置
ax.spines['bottom'].set_position(('data', -2))

# 设置 y 轴的刻度位置
ax.yaxis.set_ticks_position('left')
# 将左侧的坐标轴移动到数据坐标的 x=0 位置
ax.spines['left'].set_position(('data', 5))

plt.show()