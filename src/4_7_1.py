
numbers = []
while True:
    ss = input("请输入一个整数:")
    if ss == "end":
        break
    numbers.append(int(ss))
numbers.sort(reverse=True)    
print(numbers)