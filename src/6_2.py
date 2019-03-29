
str1 = input("请输入一个包含整数的字符串:")

list_str = str1.split(" ")
#list_val = []
dick_map={}
j=0
for i in range(len(list_str)):
    if list_str[i].isnumeric():
        val =  int(list_str[i])
        strnumber="number" + str(j)
        print(strnumber)
        newstr = "{" +strnumber + ":010}"
        list_str[i] = newstr
        dick_map[strnumber]=val
        #list_val.append(val)
        j=j+1

       
str2=" ".join(list_str)
print(str2)
print(dick_map)
#print(str2 % list_val)
print(str2.format_map(dick_map))
