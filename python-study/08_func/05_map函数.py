# map函数
# 用于批量处理可迭代对象中所有数据，返回一个迭代器
from stat import S_IROTH

# 返回一个迭代器，可以for循环
l = [1, 2, 3, 4]
map_result = map(lambda x: x * 10, l)
print(f'map_result: {map_result}')
for i in map_result:
    print(i, end=',')
else:
    print()
print('-' * 40)

# 操作字符串
code_list = ['python', 'java', 'go']
upper_map = map(lambda s: s.upper(), code_list)
upper_map_list = list(upper_map)
print(f'upper_map_list: {upper_map_list}')
print('-' * 40)

# 字符转数字
str_num_list = ['1', '2', '3', '4']
int_map = map(int, str_num_list)
try:
    while True:
        print(next(int_map), end= ',')
except StopIteration as e:
    print('结束')
print('-' * 40)


# 操作字符串
s = 'hello python'
tran = map(lambda x: x.upper(), s)
print(''.join(tran))
