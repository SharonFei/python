#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .* ',line, re.M|re.I)
if matchObj:
    print("matchObj.groups():", matchObj.groups())  #返回包含所有一个小组字符串的元组
    print("matchObj.group():", matchObj.group())
    print("matchObj.group(1):", matchObj.group(1))
    print("matchObj.group(2):", matchObj.group(2))
else:
    print("No match!!")


test = '正则表达式'
if re.match(r'正则表达式',test):
	print('ok')
else:
    print('failed')