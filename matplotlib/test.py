import matplotlib.pyplot as plt
import numpy as np

# 创建一个新的 figure
plt.figure(1)

# 在 figure 1 中创建第一个子图
plt.subplot(2, 1, 1)  # (行数, 列数, 子图位置)
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Subplot 1: Sine Wave')

# 在 figure 1 中创建第二个子图
plt.subplot(2, 1, 2)
y = np.cos(x)
plt.plot(x, y)
plt.title('Subplot 2: Cosine Wave')

# 显示所有图形
plt.show()
