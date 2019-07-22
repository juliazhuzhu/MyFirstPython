from numpy import *


b = arange(20).reshape(4,5)
a = arange(24).reshape(4,6)

print(hstack((a,b)))