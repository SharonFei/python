Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> score=1
>>> score
1
>>> score=1+5
>>> score
6
>>> t="abcdefg"
>>> print t
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(t)?
>>> print(t)
abcdefg
>>> t="iopjkl"
>>> print (t)
iopjkl
>>> apple=5
>>> apple
5
>>> apple=apple+09
SyntaxError: invalid token
>>> apple=apple+9
>>> apple
14
>>> DaysPerWeek=7
>>> HoursPerDay=24
>>> MinutesPerHour=60
>>> print(DaysPerWeek*HoursPerDay*MinutesPerHour)
10080
>>> HoursPerDay=26
>>> print(DaysPerWeek*HoursPerDay*MinutesPerHour)
10920
>>> 
