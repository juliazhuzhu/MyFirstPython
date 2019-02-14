
import random

numbers = [1,2,3,4,5,6]


for number in numbers:
    if number == random.randint(1,12):
        print(number)
        break
else:
    print("no rand matched")
    
print (1, end=" ")
print (2, end=" ")

numbers = range(10,20)
print("\n")
for number in numbers:
    print(number, end=" ")
    
print("\n")    
for number in range(20,30):
    print(number, end=" ")