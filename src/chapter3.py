# 用字典表达映射关系
empty_dict = {}
# 初始化的字典
filled_dict = {"one": 1, "two": 2, "three": 3}

# 用[]取值
filled_dict["one"]   # => 1


# 用 keys 获得所有的键。
# 因为 keys 返回一个可迭代对象，所以在这里把结果包在 list 里。我们下面会详细介绍可迭代。
# 注意：字典键的顺序是不定的，你得到的结果可能和以下不同。
print(list(filled_dict.keys()))   # => ["three", "two", "one"]


# 用values获得所有的值。跟keys一样，要用list包起来，顺序也可能不同。
print(list(filled_dict.values()))   # => [3, 2, 1]


# 用in测试一个字典是否包含一个键
print("one" in filled_dict)   # => True
print(1 in filled_dict)   # => False

# setdefault方法只有当键不存在的时候插入新值
filled_dict.setdefault("five", 5)  # filled_dict["five"]设为5
#print(filled_dict["five"])
filled_dict.setdefault("five", 6)  # filled_dict["five"]还是5
print(filled_dict["five"])

# 字典赋值
filled_dict.update({"four":4}) # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4  # 另一种赋值方法

# 用del删除
del filled_dict["one"]  # 从filled_dict中把one删除

