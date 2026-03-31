# 字典（first_dictionary）是Python中另一个非常有用的内置数据类型。

# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

# 键(key)必须使用不可变类型。

# 在同一个字典中，键(key)必须是唯一的。

from cgi import print_directory


first_dict = {}
first_dict['one'] = "1"
first_dict[2]     = "two"

tinyfirst_dict = {'name': 'zhangsan','card_id':'43412', 'age': 22}


print (first_dict['one'])       # 输出键为 'one' 的值
print (first_dict[2])           # 输出键为 2 的值
print (tinyfirst_dict)          # 输出完整的字典
print (tinyfirst_dict.keys())   # 输出所有键
print (tinyfirst_dict.values()) # 输出所有值

# 构造函数 first_dict() 可以直接从键值对序列中构建字典如下：
first_dict1 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(first_dict1)

first_dict2 = {x: x ** 2 for x in (1,2,3,4)}
print(first_dict2)

first_dict3 = dict(zhangsan=1, wangwu=2, lisi=3)
print(first_dict3)