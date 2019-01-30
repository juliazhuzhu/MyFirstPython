'''
Created on Jan 25, 2019

@author: zhuyiye
'''


print(bin(12345))
print(oct(12345))
print(hex(12345))

print(int(0xF98A))
print(bin(0xF98A))
print(oct(0xF98A))

print(int(0b1100010110))
print(oct(0b1100010110))
print(hex(0b1100010110))

x=5423.5346
print(format(x,'0.3f'))
print(format(x,'0>10.2f'))
print(format(x,'0<10.2f'))
print(format(x,'0>10,.2f'))

'''
below is wrong, need to work out 
padding 0 both on front and end at the same time
'''
print(format(x,'0<10,.2f'))
