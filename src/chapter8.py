# 装饰器(decorators)
# 这个例子中，beg装饰say
# beg会先调用say。如果返回的say_please为真，beg会改变返回的字符串。
from functools import wraps
import time

def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg

    return wrapper

def beg2(target_function):
    @wraps(target_function)
    def wrapper():
        msg = target_function()
        print("beg2:",msg)
        return msg

    return wrapper

def timeit(func):
    @wraps(func)
    def wrapper():
        start = time.clock() 
        msg = func()
        end = time.clock() 
        print('timeit:',msg)
        return "{:e}".format(end - start)
    return wrapper

@beg
def say(say_please=False):
    msg = "Can you buy me a beer?"
    return msg, say_please


@beg2
@timeit
def foo():
    print('in foo()')
    msg = "Can you buy me a beer?"
    return msg
    
#print(say())  # Can you buy me a beer?
#print(say(say_please=True))  # Can you buy me a beer? Please! I am poor :(

foo()