"""
折线图
"""
import matplotlib.pyplot as plt

# 全局变量
fig = plt.figure(figsize=(20, 8), dpi=80)  # 设置图片大小和像素点

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
plt.plot(x, y)

# 保存图片
# plt.savefig("D:\文龙\\t1.png")
# plt.savefig("D:\文龙\\t1.svg")   # 可以保存为 svg 矢量图模式,放大不会有锯齿

# 设置 x,y轴刻度
plt.xticks(range(2, 25))
plt.yticks(range(min(y), max(y) + 1))

plt.show()
