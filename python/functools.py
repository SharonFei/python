import functools
'''
def main1():
    int2=functools.partial(int,base=4)  #base参数：默认做N进制的转换
    result = int2('1000000')
    print(result)
'''
def main2():
    max2=functools.partial(max,100)
    result=max(1,2,4,7,99)
    result1=max(1,2,3,102)
    print((result,result1))

