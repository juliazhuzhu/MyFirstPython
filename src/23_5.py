from numpy import *

a = arange(9).reshape(3,3)

print(a)

b = a*3
print(b)

c = a*5
print(c)

print(hstack((a,b,c)))

