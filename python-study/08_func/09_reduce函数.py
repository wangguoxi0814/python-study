# reduce函数，合并
# reduce(func, data, default)
#   func: 必须是2个参数
#   data: 可迭代对象
#   default: 默认值

from functools import reduce

def add(a, b):
    return a + b

il = [1, 2, 3, 4, 5]
s = reduce(add, il)
print(f'原始数据: {il}')
print(f's: {s}')

s1 = reduce(add, il, 10)
print(f's1: {s1}')