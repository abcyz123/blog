# # 计算sin曲线的面积
# 1、把曲线分成N份
# 2、计算每一块矩形的面积
# 3、把N块矩形的面积加起来
import math
n = 1000
width = 2 *math.pi / n
x = [i*width for i in range(n)]
s = [abs(math.sin(i))*width for i in x]
S = sum(s)