'''fab2在运行中占用的内存会随着参数max的增大而增大，
   如果要控制内存占用，最好不要用List来保存中间结果，
   而是通过iterator对象来迭代。
'''
class Fab(object):

    
    def __init__(self,max):
        self.max = max
        self.n,self.a,self.b = 0,0,1

        
    def __iter__(self):
        return self

    
    def __next__(self):
        if self.n < self.max:
            r=self.b
            self.a,self.b = self.b,self.a+self.b
            self.n = self.n+1
            return r
        raise StopIteration()

#Fab 类通过 next() 不断返回数列的下一个数，内存占用始终为常数：
    #for n in Fab(5):
        #print n
         

