L1 = ['Hello','World',18,'Apple',None]
L2 = []
for s in L1:
    if isinstance(s,str):
        print (s.lower())
    else:
        continue
    L2.append(s.lower())
print (L2)
if L2 == ['hello','world','apple']:
    print('测试通过！')
else:
    print('测试失败！')
