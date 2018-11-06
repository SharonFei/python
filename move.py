def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
        return
    else:
        move(n-1,a,c,b)
        move(1, a, b, c)# 子目标2
        move(n-1, b, a, c)# 子目标3
n=int(input('n:'))
print(move(n,'A','B','C'))

'''
n=3
move(2,a,c,b)
move(1,a,b,c)
move(2,b,a,c)
A-->C
move(1,a,c,b)
A-->B
move(1,a,b,c)
move(1,b,a,c)
'''
