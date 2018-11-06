'''直接在fab中用print打印数字会导致该函数可复用性较差，
因为fab函数返回None,其他函数无法获得该函数生成的数列,
要提高fab函数的可复用性，最好不要直接打印出数列，而是返回一个list。
'''
def fab(max):
    n,a,b =0,0,1
    L=[]
    while n <max:
        L.append(b)
        a,b = b,a+b
        n =n+1
    return L
print (fab(5))
'''或者在调用该方法时 使用如下方式：
for n in fab(5):
    print n
'''                              
