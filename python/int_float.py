from functools import reduce
def str2float(s):
    def fn(x,y):
        return x*10+y
    n = s.index('.') #得到字符串中.的索引
    print ('n=',n)
    #根据.的位置将字符串切片为两段
    s1 = list(map(int,[x for x in s[:n]])) #列出s中前n个数
    s2 = list(map(int,[x for x in s[n+1:]]))
    return reduce(fn,s1) + reduce(fn,s2) / 10 ** len(s2) #m*n表示m的n次方
#测试结果是否正确
print ('str2float(\'123.456\')=',str2float('123.456'))
