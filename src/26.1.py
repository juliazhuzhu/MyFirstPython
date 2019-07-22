from bs4 import *
from urllib3 import *
import re

disable_warnings()

http = PoolManager()
r = http.request('GET','http://www.taobao.com')
soup = BeautifulSoup(r.data,'lxml')

#print(soup.title.text)
#print(soup.body['class'])
#print(r.data)

navigators = soup.find(role = 'navigation')
#print(navigators)
hrefs = navigators.find_all(name = 'a')
#print(hrefs)


for each in hrefs:
   print(each.get_text())
    