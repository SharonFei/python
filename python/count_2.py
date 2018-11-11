Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=2.5e6
>>> b=1.2e7
>>> print(a+b)
14500000.0
>>> a=2.6e75
>>> b=1.2e74
>>> print(a+b)
2.72e+75
>>> 8/3
2.6666666666666665
>>> 8//3
2
>>> 8%3
2
>>> 9%3
0
>>> 9//3
3
>>> 9/3
3.0
>>> 8.0/3
2.6666666666666665
>>> 8.0//3
2.0
>>> 6**4
1296
>>> 1.7e7
17000000.0
>>> 4.56e-5
4.56e-05
>>> 4.56e-1
0.456
>>> (35.27*(1-15%))/3
SyntaxError: invalid syntax
>>> (35.27*(1-15%))/3
SyntaxError: invalid syntax
>>> 35.27*(1-15%)/3
SyntaxError: invalid syntax
>>> (1-15%)*35.27/3
SyntaxError: invalid syntax
>>> (1-15%)*35.27
SyntaxError: invalid syntax
>>> (1-0.15)*35.27/3
9.993166666666667
>>> (1-0.15)*35.27//3
9.0
>>> (1-0.15)*35.27%3
2.9795000000000016
>>> (1+0.15)*35.27/3
13.520166666666666
>>> (1+0.15)*35.27//3
13.0
>>> (1+0.15)*35.27%3
1.5604999999999976
>>> (1+0.15)*35.27
40.5605
>>> 40.5605%3
1.5604999999999976
>>> 
>>> 12.5*16.7
208.75
>>> (12.5+16.7)*2
58.4
>>> rectangle=(12.5+16.7)*2
>>> print ("rectangle =" rectangle)
SyntaxError: invalid syntax
>>> print (rectangle)
58.4
>>> 
>>> 
>>> print ("rectangle =" )
rectangle =
>>> print ("rectangle =" ) rectangle
SyntaxError: invalid syntax
>>> F=38
>>> C=5/9*(F-32)
>>> print C
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(C)?
>>> print (C)
3.3333333333333335
>>> C=5//9*(F-32)
>>> print (C)
0
>>> v=80
>>> l=200
>>> t=l/v
>>> print t
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(t)?
>>> print (t)
2.5
>>> 
