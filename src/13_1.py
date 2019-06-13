from string import Template
import os

'''
i = 21
while i > 0:
    i=i-1
    temp = Template("{: ^${d}}")
    str =temp.substitute(d=i)
    print(str.format("*"))
'''


while 1:
    s = input("棱形的行数:")
    if s.lower() == "end":
        print("欢迎下次惠顾...")
        break
    f = open('./stars.txt','a+')
    level = int(int(s)/2+1)
    print("level = {}".format(level))
    offset = level
    for row in range (level):
        mat = "{:>%d}" % (row + offset)
        star = "*"*(2 * (row) + 1)
        f.write(mat.format(star)+os.linesep)
        
    while level > 0:
        mat = "{:>%d}" % (level + offset-2)
        #print(mat)
        star = "*"*(2 * (level)-3)
        f.write(mat.format(star)+os.linesep)
        level=level -1
    
    f.close()

