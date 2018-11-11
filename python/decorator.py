def log(func):
    def wrapper(*args,**kw):  #wrapper()函数可以接收任意参数的调用                      
        print('call %s():' %func.__name__) #在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
        return func(*args,**kw)
    return wrapper


@log           #接收一个函数作为参数，并返回一个函数，借助@语法，把decorator置于函数的定义处
def now():
    print('2015-3-25')


#调用now()函数


'''由于log()是一个decorator，返回一个函数，所以，
原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。'''
