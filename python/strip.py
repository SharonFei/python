#!/usr/bin/python
# -*- coding:UTF-8 -*-

str = "00000003210Runoob0123000000"
print (str.strip( '0' ))  #去除首尾字符0

str2 = "  Runoob   "  #去除首尾空格
print (str2.strip())

#只要头尾包含有指定字符序列中的字符就删除
str3 = "123abcrunoob321"
print (str3.strip( '21' )) #字符序列为12
