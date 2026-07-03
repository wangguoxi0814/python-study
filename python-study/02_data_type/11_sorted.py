# 容器的一些内置函数
# 1. sorted()
# 2. reversed()
# 3. len()
# 4. max() / min() / sum()
# 5. all()
# 6. any()
# 7. enumerate()

# sorted不是原地排序，会返回一个新的容器，因此这里l1本身不会发生变化
# sorted默认升序，reverse=True为降序
# sorted无论传入什么可迭代对象，返回值都是list
l1 = [7, 6, 2, 9]
s_l1 = sorted(l1)
s_l1_desc = sorted(l1, reverse=True)
print('l1 is:', l1)
print('s_l1 is:', s_l1)
print('s_l1_desc is:', s_l1_desc)
print()

# 在10_tuple_of_common_api.py中，说明了tuple由于不可变，因此没有原地排序的sort(),但内置函数sorted不是原地排序，因此也可以操作tuple
t1 = (2, 8, 4, 6, 3)
s_t1 = sorted(t1)
s_t1_desc = sorted(t1, reverse=True)
print('t1 is:', t1)
print('s_t1 is:', s_t1)
print('s_t1_desc is:', s_t1_desc)
print()

# set本身无序，因此其本身也没有sort和reverse方法，元素个数也是唯一，因此也没有count
# 但sorted仍然可以操作它，最终返回一个list
s1 = {5, 3, 2, 8}
s_s1 = sorted(s1)
s_s1_desc = sorted(s1, reverse=True)
print('s1 is:', s1)
print('s_s1 is:', s_s1)
print('s_s1_desc is:', s_s1_desc)
print()

# dict本身也没有sort，reverse方法，但内置函数sorted可以操作它,返回它的key的list
d1 = {'shanghai': 2, 'beijing': 1, 'shenzhen': 3}
s_d1 = sorted(d1)
s_d1_desc = sorted(d1, reverse=True)
print('d1 is:', d1)
print('s_d1 is:', s_d1)
print('s_d1_desc is:', s_d1_desc)
print()
