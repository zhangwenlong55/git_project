"""
数组的运算练习
"""
import numpy as np

t1 = np.array(range(15)).reshape((5, 3))
t2 = np.array(range(100, 115)).reshape((5, 3))

print(t1)
print(t2)

# 广播机制
print("************广播机制************")
print(t1 * 2)
print(t1 + 2)

# 矩阵相加
print("**************矩阵相加***********")
print(t1 + t2)
print(t1 * t2)
print(t1 / t2)
