try:
    open("abc.text",'r')
    print(aa)
except BaseException as msg:#as msg：定义msg变量用于接收异常信息，并通过print打印出来
    print(msg)
