def odd():
    print ('step 1')
    yield 1  #遇到yield就中断，下次又继续执行
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
    
