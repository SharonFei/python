def _odd_iter():  #从3开始的奇数序列
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n): #定义一个筛选函数
    return lambda x: x%n >0

def primes(): #定义一个生成器，不断返回下一个素数
    yield 2
    it = _odd_iter() #初始序列
    while True:
        n = next(it) #返回序列的第一个数
        yield n
        it = filter(_not_divisible(n),it)  #构造新序列
for n in primes():  #打印1000以内的素数
    if n <1000:
        print(n)
    else:
        break

