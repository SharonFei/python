def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >=0:
        return x
    else:
        return -x
#函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
def nop():
    pass
#pass语句可以用来作为占位符，比如现在还没想好怎么写函数的代码，
#就可以先放一个pass，让代码能运行起来
