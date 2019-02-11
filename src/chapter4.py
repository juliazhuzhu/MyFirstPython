
# 这两种可变参数可以混着用
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
    
# 调用可变参数函数时可以做跟上面相反的，用*展开序列，用**展开字典。
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)   # 相当于 foo(1, 2, 3, 4)
all_the_args(**kwargs)   # 相当于 foo(a=3, b=4)
all_the_args(*args, **kwargs)   # 相当于 foo(1, 2, 3, 4, a=3, b=4)

print("begin dict exampls")
empty_dict = {}
# 初始化的字典
filled_dict = {"one": 1, "two": 2, "three": 3}

# 用[]取值
print(filled_dict["one"])   # => 1

if "one" in filled_dict:
    print("one is ok")
    
if 1 in filled_dict.values():
    print("1 is ok")

if "one" in filled_dict.keys():
    print("one is keys ok")
    
print(filled_dict.get("four", 4))# 4 is the default value when "four" is not present
print(filled_dict.get("one", 4))

for animal in ["dog", "cat", "mouse"]:
    print("{name} is a mammal".format(name=animal))

x = 0
while x < 4:
    print(x)
    x += 1  # x = x + 1 的简写

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable) # => dict_keys(['one', 'two', 'three'])，是一个实现可迭代接口的对象

# 可迭代对象可以遍历
for i in our_iterable:
    print(i)    # 打印 one, two, three   

 
