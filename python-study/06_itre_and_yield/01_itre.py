# 迭代器
# 迭代器是Python中的一种对象，它可以在遍历数据序列时，逐个返回数据元素
# 字符串、列表、元组、集合、字典都可以被迭代
# 迭代器是一个实现了__iter__和__next__方法的对象
# __iter__方法返回迭代器对象本身
# __next__方法返回下一个数据元素
# 迭代器终止时会抛出StopIteration异常(迭代器协议规定)
    # 如果不抛出异常，在for时死循环
    # list(iter)时，会无限读取，死循环/内存溢出
# 迭代器对象可以通过next()函数来获取下一个数据元素
# 迭代器（Iterator）和可迭代对象（Iterable）都可以被for遍历。通过可迭代对象可以得到迭代器.
# 迭代器是惰性计算，不会一次性计算所有结果，能显著降低性能消耗,当数据量很大，或者不知道有多少数据时，就可以使用迭代器
print("==========1==========")
l1 = [1,2,3,4,5]
ite = iter(l1)
print('ite: ', ite)
while True:
    try: 
        print(next(ite))
    except StopIteration:
        break


# 迭代器对象可以通过for循环来遍历数据序列
print("==========2==========")
list2 = [1,2,3,4,5]
iter2 = iter(list2)
for i in iter2:
    print(i, end=' ')
print()

# 字符串迭代器
print("==========3==========")
str1 = "Hello, World!"
iter3 = iter(str1)
for i in iter3:
    print(i, end=' ')
print()
