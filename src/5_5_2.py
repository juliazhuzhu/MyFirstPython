
while 1:
    s = input("请输入星号塔的层数:")
    if s.lower() == "end":
        print("欢迎下次惠顾...")
        break
    level = int(s)
    offset = level
    for row in range (level):
        mat = "{:>%d}" % (row + offset)
        star = "*"*(2 * (row) + 1)
        print(mat.format(star))