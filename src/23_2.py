from numpy import *

a = array([[1,2,3],[4,5,6],[7,8,9]])

print(a[0,0])
print(a[0:])
print(a[0:1])

print(a[0:1])
print(a[0:1][0])
print(a[0:2])
print(a[0:2][1])

b = arange(24).reshape(2,3,4)
print(b)
print(b.ravel())
print(b.flatten())
b.shape=(6,4)
print(b)
b3=b.transpose()
print(b3)

b.shape=(2,12)
print(b)