s = 3  #设置全局变量
def createCounter():
    def counter():
        global  s  #引用全局变量
        s = s+1
        return s
    return counter
counterA =createCounter()
print(counterA())   #每次调用子函数都会保留上次s的值进行计算
