import os
print("二元一次方程求解计算器")
print("设一个二元一次方程为aX + bY = c")
print("开发者信息：\n鼎天网络\nDTNETWORK\nGary Chan")
print("感谢使用")
import math
a1 = input("a1=")
b1 = input("b1=")
c1 = input("c1=")
a2 = input("a2=")
b2 = input("b2=")
c2 = input("c2=")

a4 = int(a1)
b4 = int(b1)
c4 = int(c1)
a5 = int(a2)
b5 = int(b2)
c5 = int(c2)

x = ( c5 * b4 - c4 * b5 ) / ( a5 * b4 - a4 * b5 )
y = ( a4 * c5 - a5 * c4 ) / ( b5 * a4 - a5 * b4 )

x2 = str(x)
y2 = str(y)

print("x=" + x2 )
print("y=" + y2 )
e = "单击任意键退出"
print(e)
os.system("pause")