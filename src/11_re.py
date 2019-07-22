import re

s = 'python|go'
m = re.match(s, "I love python")

if m is not None:
    print(m.group())
    
print (m)

m = re.match(s, "python I love ")#python from begin, for match to match

if m is not None:
    print(m.group())
    
print (m)

m = re.search(s, "I love python")

if m is not None:
    print(m.group())
    
s = 'Bill|Mike|John'

m = re.match(s,"Bill,my friend,Bill")

if m is not None:
    print(m.group())
    

s = '12-a-abc54-a-xyz---78-A-ytr'
result = re.findall(r'\d\d-a-[a-z]{3}',s)
print(result)
m = re.search(r'\d\d-a-[a-z]{3}',s)
print(m.group())

s = '\w{2}t'

m=re.search(s,'bat')
print(m.group())

s = '\d{4} \d{4} \d{4} \d{4}'
m=re.match(s,'1234 5432 4444 8898')
print(m.group())


s = '2\d{3}-[1-12]{1,2}-[1-31]{1,2}'
m = re.match(s,'2000-2-1')
print(m.group())

m = re.match(s,'2000-12-1')
print(m.group())

m = re.match(s,'2000-1-11')
print(m.group())

m = re.match(s,'1988-1-11')
if m is not None:
    print(m.group())
    
m = re.match(s,'2099-111-11')
if m is not None:
    print(m.group())    
    
m = re.match(s,'2099-13-11')
if m is not None:
    print(m.group())  
    
htmlStr = '<a href=\'a.html\'>aaa</a> <a href=\'b.html\'>bbb</a>'
aList = re.findall('<a[^>]*>',htmlStr)     
print(aList)

for a in aList:
    g = re.search('href[\s]*=[\s]*[\'"]([^>\'""]*)[\'"]',a)
    print(g)
    print(g.group(1))