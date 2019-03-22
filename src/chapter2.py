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
padding 0 both on front and end at the same time
'''
print(format(x,'0^10,.2f'))


print("{:^10.2f}".format(-4.56))
print("{0:^10.2f}".format(-4.56))
print("{0:=^10.2f}".format(-4.56))
print("{0:#=10.2f}".format(-4.56))
print("{0:=10.2f}".format(-4.56))

print("{:$^20}".format(" 美元 "))

print("{:$=10.2f}".format(4.56))

print("{:10.2f}".format(4.52))
print("{:=10.2f}".format(4.52))
print("{:=<10.2f}".format(4.52))

s3 = "Today is {week}, {}, the {} temperature is {degree} degrees"

print (s3.format("aaaa", 12345, week= "SUNDAY", degree = 23))

s4 = "Today is {week}, {1}, the {0} temperature is {degree} degrees"
print (s4.format("aaaa", 12345, week= "SUNDAY", degree = 23))

print ("Unicode 输出: {first!a}".format(first="中国"))
print ("原样输出: {first!s}".format(first="中国"))

print("二进制数字{num:b}".format(num=10))