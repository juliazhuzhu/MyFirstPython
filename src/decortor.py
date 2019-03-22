import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print('used:',end-start)
    
    return wrapper

@timeit
def foo():
    print('in foo()')
    
    
foo()