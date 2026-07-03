# 字典（first_dictionary）是Python中另一个非常有用的内置数据类型。

# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

# 键(key)必须使用不可变类型。

# 在同一个字典中，键(key)必须是唯一的。

## 注意：
# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。



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

# {x: x**2 for x in (2, 4, 6)} 该代码使用的是字典推导式
first_dict2 = {x: x ** 2 for x in (1,2,3,4)}
print(first_dict2)

first_dict3 = dict(zhangsan=1, wangwu=2, lisi=3)
print(first_dict3)


# dict 增删改查
d_op = {'zhangsan': 68, 'wangwu': 90, 'zhaoliu': 88}
# 修改
d_op['zhangsan'] = 80
print(f'update ele d_op is {d_op}')
# 查询
d_op = {'zhangsan': 68, 'wangwu': 90, 'zhaoliu': 88}
score = d_op['wangwu']
print(f'wangwu score is {score}')
# 获取不存在的key，执行异常 KeyError: 'Peter'
# 可以使用get()获取key的value，如果key不存在，返回None。get()也可以设置默认值，当key不存在时，返回默认值
# p_score = d_op['Peter']
# p_score = d_op.get('Peter')
p_score = d_op.get('Peter', 0)
print(f'Peter score is {p_score}')

# 删除
d_op = {'zhangsan': 68, 'wangwu': 90, 'zhaoliu': 88}
del d_op['zhaoliu']
print(f'del key d_op is {d_op}')
# 增加
d_op = {'zhangsan': 68, 'wangwu': 90, 'zhaoliu': 88}
d_op['lisi'] = 99
print(f'add ele d_op is {d_op}')

# pop
d_op = {'zhangsan': 68, 'wangwu': 90, 'zhaoliu': 88}
pop_entry = d_op.pop('zhangsan')
print(f'pop item is {pop_entry}')
print(f'pop ele d_op is {d_op}')

# 如果pop操作的key不存在，执行异常 KeyError: 'Peter'
# p_item = d_op.pop('Peter')
# pop可以给默认值，如果pop的key不存在，而返回默认值, 如果key存在，则返回实际key对应的value
p_item = d_op.pop('Peter', 'key不存在')
print(f'pop item p_item is {p_item}')

# keys / values / items
# keys 返回 dict_keys ，可遍历，但不可索引,一般转为list索引。直接对dict_keys索引会报：TypeError: 'dict_keys' object is not subscriptable
# values 返回 dict_values,可遍历，但不可索引，一般转为list索引
# items 返回dict_items, 元素是一个元组,可遍历，但不可索引，一般转为list索引
score_dict = {'Peter': 68, 'Lucy': 90, 'Mia': 88}
ks = score_dict.keys()
print(f'ks is {ks}, type is {type(ks)}')
# print(f'ks index 0 ele is {ks[0]}')  # TypeError: 'dict_keys' object is not subscriptable
lks = list(ks)
print(f'lks index 0 ele is {lks[0]}')

vs = score_dict.values()
print(f'vs is {vs}, type is {type(vs)}')
lvs = list(vs)
print(f'lvs index 0 ele is {lvs[0]}')

items = score_dict.items()
print(f'items is {items}, type is {type(items)}')
lis = list(items)
print(f'lis index 0 ele is {lis[0]}')