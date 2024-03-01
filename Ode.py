import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # or another compatible backend

# 定义二阶非齐次常系数微分方程
def model(u, x):
    u1, u2 = u
    du1dx = u2
    du2dx = -p*u2 - q*u1 + f(x)
    return [du1dx, du2dx]

# 定义常数和已知函数
p = 0.1
q = 1.0

def f(x):
    # return np.sin(x)
    return 1

# 初值条件
u0 = [0.0, 1.0]

# 定义x的值
x = np.linspace(0, 100, 100)

# 使用odeint函数解一阶方程组
u = odeint(model, u0, x)

# 提取解
u1, u2 = u[:, 0], u[:, 1]

# 绘制解
plt.plot(x, u1, label='x(t)')
plt.plot(x, u2, label="x'(t)")
plt.xlabel('time/s')
plt.legend(['x','v'])
plt.title('Spring-mass-damping system')
plt.show()
