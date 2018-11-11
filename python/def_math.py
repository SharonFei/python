import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
def quadratic(a,b,c):
    delta=b*b-4*a*c
    x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    if delta>0:
        print("此方程无解")
    elif delta==0:
        return x1
    else:
        return x1,x2
a=input("请输入a")
b=input("请输入b")
c=input("请输入c")
print(quadratic(a,b,c))
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
