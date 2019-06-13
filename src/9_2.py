import math
import random
#print (math.factorial(3))


class JCException(Exception):
    pass


class JCCompute:
    def compute(self,n):
        if n < 0:
            raise JCException("{} is less than 0".format(n))
        else:
            return math.factorial(n)    


jc = JCCompute()

try:
    param = random.randint(-10,10)
    val = jc.compute(param)
except JCException as e:
    print(e)
else:
    print(val)