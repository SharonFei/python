try:
    open("abc.text",'r')
except FileNotFoundError:
    print("异常了！")
    
