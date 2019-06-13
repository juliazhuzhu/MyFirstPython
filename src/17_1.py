import _thread
from threading import Lock
from time import sleep

lock = Lock()
def fun(threadName):
    lock.acquire()
    for i in range(3):
        print("{} index {}".format(threadName,i))
    lock.release()
    #print(args)

def main():
    for j in range(2):
        threadName = "thread_" + str(j)
        _thread.start_new_thread(fun, (threadName,))
    sleep(2)
        
if __name__ == '__main__':
    main()
    



