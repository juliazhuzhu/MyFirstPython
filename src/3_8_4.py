scope = {}
while True:
    codes=input("请输入表达式:")
    if codes == "":
        continue
    print("计算结果:{}".format(eval(codes, scope)))
    