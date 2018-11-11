from functools import reduce
def multiply(x,y):
    return x*y
def prod(L):
    return(reduce(multiply,L))#需要返回值
    
