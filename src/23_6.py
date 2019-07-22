from numpy import *

a = arange(12).reshape(3,4)
print(a)

b = arange(16).reshape(4,4)
print(b)

c = arange(20).reshape(5,4)
print(c)

d = vstack((a,b,c))
print(d)

print(hsplit(d,2))

print(vsplit(d,2))

