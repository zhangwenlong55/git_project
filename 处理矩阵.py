import numpy as np
import random

t1 = np.array([1, 2, 3, 4])
print(t1)
print(type(t1))

t2 = np.arange(0, 10)
print(t2)
print(t2.dtype)

t3 = np.array([random.random() for i in range(10)])
print(t3)
print(t3.dtype)

print(np.array(t3.round(2)))
