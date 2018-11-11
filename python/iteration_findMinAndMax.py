import random  
def findMinAndMax(l):
    if l == []:  
        return (None,None)  
    else:  
        my_min = l[0]  
        my_max = l[0]  
        for i in l:  
            if my_min > i:  
                my_min = i  
            if my_max < i:  
                my_max = i  
        return (my_min, my_max)  
l = list(range(0, 10))  
random.shuffle(l)  #将序列的所有元素随机排序
print(l)  
print(findMinAndMax(l))
