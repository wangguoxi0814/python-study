# Tuple类型:元组，可以包含多个元素，且类型可以不同
# 元组和list的唯一区别是不可变
# 元组同样是连续的、有序的。支持切片、索引、遍历、拼接、乘法、长度等操作

# 创建空元组
empty_tuple = ()
print('empty tuplee is:', empty_tuple)
# 创建单个元素元组,注意:一定要以逗号结尾，否则括号会视作数学运算中的括号,整体会被当做一个数字
single_tuple = (1,)
not_tuple = (1)
print('single_tuple type is:', type(single_tuple))
print('not_tuple type is:', type(not_tuple))

# 长度
l = len(single_tuple)
print('single_type len is ', l)

# 切片
tuplee = (1, 'Hello', 3.14, -1)
print('tuplee[1:] is ', tuplee[1:])

# 遍历
for t in tuplee:
    print(t, end=' ')

print()

# 拼接
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print('tuple3 is', tuple3)
# 添加元素
# tuple由于不可变，因此没有添加、移除方法。如果要追加，可以先换位list，操作完毕再转回元组
t1 = (1,2,3)
l1 = list(t1)
l1.append(4)
t2 = tuple(l1)
print('t2 is:', t2)

# 乘法
tuple4 = tuple1 * 2
print('tuple4 is :', tuple4)

# 不可变，如下代码会报错
# tuple5 = (1,2,3,4,5)
# tuple5[0] = 10

# 判断元素是否存在于元组中
tuple_contain = (1, 2, 3)
print('1存在于tuple_contain中', 1 in tuple_contain)
