import random

class StartMobileException(Exception):
    pass

class Mobile:
    
    def start(self):
        val = random.randint(1, 100)
        if val < 50:
            raise StartMobileException("{} is less than 50".format(val))
        
        return
    
    
    

m = Mobile()    
for i in range(1,100):
    try:
        m.start()
    except StartMobileException as e:
        print(e)
    else:
        print("{} has no exception".format(i))