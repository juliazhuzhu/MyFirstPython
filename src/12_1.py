import random
import os 

dirs = ['a','b','c','f']

dirlist = random.sample(dirs,3)
print('/'.join(dirlist))

if not os.path.exists('/'.join(dirlist)):
    os.makedirs('/'.join(dirlist), 0o777, True)
    print("{} has been create".format('/'.join(dirlist)))