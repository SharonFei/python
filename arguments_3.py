list=[]
def the_input(count=eval(input("输入乘数的总个数："))):
    for i in range(count):
        N=eval(input("依次输入乘数："))
        list.append(N)
    print("一共有",count,"个要相乘的数")
    print("把这些乘放在列表里面：",list)

the_input()

def product(*numbers):
    sum=1
    for n in numbers:
        sum=sum*n
    return sum

print("这些数相乘的结果是：",product(*list))
