s = input("请输入一个字符串:")
while 1:
    subStr=input("请输入需要统计的字符串:")
    count = 0
    if subStr.lower() == "end":
        break
    pos = s.find(subStr)
    while pos != -1:
        count=count+1
        pos = s.find(subStr,pos+1)
    print("{}在{}中出现的次数{}".format(subStr,s,count))
