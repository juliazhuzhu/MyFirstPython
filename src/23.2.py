from numpy import *

a = arange(20).reshape(5,4)

print(a)

b = hsplit(a, 2)
print(b)
print(b[0].shape)

print(b[0])

savetxt('a.txt',b[0],fmt='%d',delimiter=';')
savetxt('b.txt',b[1],fmt='%d',delimiter=';')