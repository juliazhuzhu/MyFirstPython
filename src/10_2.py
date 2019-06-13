
def fibonacci():
    a = 0
    b = 1
    while True:    
        result = a
        a , b = b, a + b
        if result > 300:
            break
        yield result
    

for num in fibonacci():
    print (num)