import time
import datetime

while True:
    try:
        date1 = input("请输入第一个时间:")
        d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        date2 = input("请输入第二个时间:")
        d2 =datetime.datetime.strptime(date2, "%Y-%m-%d")        
        print(d2-d1)
    except Exception as e:
        print(e)
    