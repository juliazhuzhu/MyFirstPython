import random

dick = {}
for i in range(999):
    dick.setdefault(random.randint(0, 99),random.random())

print(dick.items())

