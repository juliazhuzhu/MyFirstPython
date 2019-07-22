from bs4 import *
from urllib3 import *
import re

disable_warnings()

http = PoolManager()

headers = {
    'authority':'item.jd.com',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding':'gzip, deflate, br',
    'cookie':'pinId=lSPpC6mw67Gk6riFxae2_Q; shshshfpa=63c2b20a-d0a5-33b9-6d1f-d066e546cf1c-1532654573; shshshfpb=020f219a39302661830cb773ce79f464789f70ab2fbe3fa595b58239c8; pin=juliazhuzhu; unick=%E6%99%93%E5%8F%B62017; _tp=B5PRp1mFSQ1kSB1IHSR2sQ%3D%3D; _pst=juliazhuzhu; TrackID=1ZvKJSRY3pU6TYFPTzr0rlyaWrnpzVyAt9xRG0fLmOxE9vSFOPLbmEKh-bdJyrtFVqV0ecgftoor3mZMT13E-fubKC5qeJiwF8LY6pKQK3g_w1wyrTCGfsFjUoCaI-Y-f; user-key=29b638ab-53cd-4d23-8fc1-3365685fa1ad; __jdu=1517112675477618044204; mt_xid=V2_52007VwMWUltYUlkYTx1ZA2EEEltcXVdZHkwpWAZjURtTXQ9OUxZBG0AAZ1BHTg1YB1kDHkxcVzIDRgVYDVRaL0oYXA17AhROXFFDWhlCG1wOYwMiUG1YYl4fQBtbDW8EFWJYWVtc; __jdv=122270672|direct|-|none|-|1563333095376; areaId=1; ipLoc-djd=1-2800-2848-0; cn=0; __jda=122270672.1517112675477618044204.1517112675.1563357289.1563785271.302; __jdc=122270672; 3AB9D23F7A4B3C9B=H2ELNPYT726UXOCOQBO32MQQ3ELRB2RL7JFRUJXOCLEVHILWFNUK3RX4EPGOHVYGEAEEDTEGYQSKMAU3M55C6I55VY; shshshfp=ac64ac7781f276b9fc881cca79931379; shshshsID=cd33afc6a43f918fd81726f80899ce89_3_1563785498404; __jdb=122270672.8.1517112675477618044204|302.1563785271',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'upgrade-insecure-requests': 1,
    'if-modified-since':'Mon, 22 Jul 2019 09:51:40 GMT',
    'cache-control': 'max-age=0',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'path': '/12490136.html',
    'scheme': 'https',
    'Referrer Policy': 'no-referrer-when-downgrade'
    }
r = http.request('GET','https://item.jd.com/12490136.html',headers)
##no-referrer-when-downgrade

soup = BeautifulSoup(r.data,'lxml')
#print(r.data)
#print(soup.title.text)
#print(soup.body['class'])
#print(r.data)

#print(navigators)
hrefs = soup.find_all(name = 'li')
#print(hrefs)

book_dict = {}
for each in hrefs:
   item_str = each.get_text()
   #print(item_str)
   if '：' in item_str:
       items = item_str.split('：')# 以空格为分隔符，分隔成两个
       book_dict[items[0]] = items[1].strip()
 
print(book_dict)      
   
    