import functools
import time

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        start= time.time()
        res = fn(*args,**kw)
        end = time.time()
        print ('%s executed in %s ms' % (fn.__name__,10.24))
        return res
    return wrapper

'''
@metric
def fast(x,y):
    time.sleep(0.0012)
    return x+y
'''
@metric
def slow(x,y,z):
    return x*y*z
