

class Factorial:
    def __init__(self,n):
        self.n = n
        self.result = n
        
    def __next__(self):
        n = self.n - 1
        if n == 1:
            raise StopIteration
            return 1
        self.result = self.result * n
        if self.result > 10000:
            raise StopIteration
        self.n = n
        return self.result
    
    def __iter__(self):
        return self
    
fac = Factorial(6)
for val in fac:
    print (val)

fac2 = Factorial(9)    
print(list(fac2))