import re

words = 'test star test star;bus  test bill,  new yeah bill,book bike God start python what'
result = re.split('[,;\s]+',words)
print(result)

dict = {}

for value in result:
    if value in dict:
        dict[value]=dict[value]+1
    else:
        dict[value]=1

for key, value in dict.items():
    print("{} = {}".format(key, value))


