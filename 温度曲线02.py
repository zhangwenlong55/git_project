"""
绘制10:00-12:00随机温度变化曲线
"""
import random

from matplotlib import pyplot as plt

fig = plt.figure(figsize=(50, 30), dpi=80)
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.plot(x, y)

# 设置标题
plt.xlabel("Time/min")
plt.ylabel("Temperature/℃")
plt.title("TEMPERATURE-TIME-CURVE")

# 调整x轴刻度
plt.xticks(x)
# plt.savefig("./t1.png")
plt.show()
