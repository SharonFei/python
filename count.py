Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print3.0/2
SyntaxError: invalid syntax
>>> print 3.0/2
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(3.0/2)?
>>> 3.0/2
1.5
>>> print (3/2)
1.5
>>> print (3//2)#整除
1
>>> print (2+3*4)
14

>>> print (2+3)*4
5
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print (2+3)*4
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
>>> print （(2+3)*4）
SyntaxError: invalid character in identifier
>>> print ((2+3)*4)
20
>>> print(3*3*3)
27
>>> print(3**3)
27
>>> print(3**5)
243
>>> print(3^3)
0
>>> print(3^5)
6
>>> number=7
>>> number+=1
>>> print number
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(number)?
>>> print (number)
8
>>> number-=2
>>> print (number)
6
>>> 
