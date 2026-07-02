# Tuple类型:元组，可以包含多个元素，且类型可以不同
# 元组和list的唯一区别是不可变
# 元组同样是连续的、有序的。支持切片、索引、遍历、拼接、乘法、长度等操作

# 创建空元组
empty_tuple = ()
print('empty tuple is:', empty_tuple)
# 创建单个元素元组,注意:一定要以逗号结尾，否则括号会视作数学运算中的括号,整体会被当做一个数字
single_tuple = (1,)
not_tuple = (1)
print('single_tuple type is:', type(single_tuple))
print('not_tuple type is:', type(not_tuple))

# 长度
l = len(single_tuple)
print('single_type len is ', l)

# 切片
tuple = (1,'Hello', 3.14, -1)
print('tuple[1:] is ', tuple[1:])

# 遍历
for t in tuple: 
    print(t, end=' ')

print()

# 拼接
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = tuple1 + tuple2
print('tuple3 is', tuple3)

# 乘法
tuple4 = tuple1 * 2
print('tuple4 is :', tuple4)

# 不可变，如下代码会报错
# tuple5 = (1,2,3,4,5)
# tuple5[0] = 10
