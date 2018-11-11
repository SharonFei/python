from random import randint
#生成一个1到9之间的随机整数
number =randint(1,9)
if number % 2 == 0:
    raise NameError("%d is even" % number)
else:
    raise NameError("%d is odd" % number)
