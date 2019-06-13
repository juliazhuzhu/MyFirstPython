from urllib3 import *

disable_warnings()

http = PoolManager()

url = 'https://www.taobao.com'

response = http.request('GET',url)

print(response.info())
print('----------------')
content_type = response.info()['Content-Type']
print(response.info()['Content-Type'])

types = content_type.split(";")

for type in types:
   # print(type)
    if type.find("charset") != -1:
       print(type.split("=")[1])