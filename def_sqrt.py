import math
def quadratic(a,b,c):
    delta=b*b-4*a*c
    x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    if delta<0:
        print("此方程无解")
    elif delta==0:
        return x1
    else:
        return x1,x2

