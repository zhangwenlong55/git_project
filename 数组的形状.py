import numpy as np

t1 = np.arange(12)
print(t1)

# 查看数组的形状
s1 = t1.shape
print(s1)

# 改变数组的形状重新打印
s2 = t1.reshape((4, 3))
print(s2)

# 展开数组
s3 = s2.flatten()
print(s3)