
import os
    
ss = input("请输入一个整数:")
number = int(ss)
k = 1
numbers2 = []
if number < 1:
    print("非法输入")
    os._exit(0)
    
for i in range(number):
    numbers = []
    for j in range(number):
        numbers.append(k)
        k=k+1
    numbers2.append(numbers)
print(numbers2)   
            
numbers3=[]
for i in range(number):
    numbers = []
    for j in range(number):
        numbers.append(numbers2[j][i])
    numbers3.append(numbers)
print(numbers3)
        

    