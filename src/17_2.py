from urllib3 import *
import threading 

semaphore = threading.BoundedSemaphore(3)

class DownloadThread(threading.Thread):
    def __init__(self,func, args,name=''):
        super().__init__(target=func, name=name, args=args)

def download(url, filename):
    response = http.request('GET',url)
    data = response.data
    with open(filename, 'wb') as fp:
        fp.write(data)
    semaphore.release()
    return
        

disable_warnings()


http = PoolManager()
f = open('image_url.txt','r')
url = ''
threads=[]
index = 1
while True:
    url = f.readline()
    filename = str(index) + '.jpg'
    url = url.rstrip()
    if url == '':
        break
    else:
        print(url)
        thread = DownloadThread(download,(url, filename))
        threads.append(thread)
        index = index + 1


for thread in threads:
    semaphore.acquire()
    thread.start()
    print(semaphore._value)

for thread in threads:
    thread.join()
    
print('end')