def is_palindrome(n):
    nn = str(n) #转成字符串
    return nn == nn[::-1] #反转字符串并判断是否为回数，返回true/false
print(list(filter(is_palindrome,range(1,1000))))
