'''想要保持第一版fab函数的简洁性，同时又要获得iterable的效果，可以使用yield'''
def fab(max):
    n,a,b= 0,0,1
    while n <max:
        yield b
        #print b
        a,b =b,a+b
        n = n+1
        
