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

# dict本身也没有sort，reverse方法，等内置函数sorted可以操作它,返回它的key的list
d1 = {'shanghai': 2, 'beijing': 1, 'shenzhen': 3}
s_d1 = sorted(d1)
s_d1_desc = sorted(d1, reverse=True)
print('d1 is:', d1)
print('s_d1 is:', s_d1)
print('s_d1_desc is:', s_d1_desc)
print()

# reversed() 反转， 返回结果为reverseiterator，即反转迭代器对象，这样不会一次性把反转结果放到内存，而是使用时，再逐个生成结果
# reversed操作list，会返回list_reversed_iterator，它持有list的引用，迭代效率更高
# reversed操作tuple/str等迭代对象，统一返回reversed迭代器对象
# reversed操作range，返回range_iterator
rl = [1, 2, 3, 4, 5]
reversed_ite = reversed(rl)
reversed_list = list(reversed_ite)
print('rl is:', rl)
print('reversed_ite is:', reversed_ite)  # <list_reverseiterator object at 0x0000019178432140>
print('reversed_list is:', reversed_list)
print()

# set是无序的，它本身就没有reverse方法，当然内置函数reversed()也无法操作它。因为既然无序，何来反转呢？
# TypeError: 'set' object is not reversible
# rs = {2, 3, 4, 5}
# reversed_set = reversed(rs)
# print('rs is:', rs)
# print('reversed_set is:', reversed_set)
# print()

rt = (1, 2, 3, 4, 5)
reversed_t_ite = reversed(rt)
reversed_t = tuple(reversed_t_ite)
print('rt is:', rt)
print('reversed_t_ite is:', reversed_t_ite)   # <reversed object at 0x0000025D79C32380>
print('reversed_t is:', reversed_t)
print()

str = 'Hello AI Agent'
reversed_str_ite = reversed(str)
# 先把反转迭代器转为list，再join为字符串。 或者直接一步到位：reversed_str = ''.join(reversed_str_ite)
# c_list = list(reversed_str_ite)
# reversed_str = ''.join(c_list)
reversed_str = ''.join(reversed_str_ite)
print('str is:', str)
print('reversed_str_ite is:', reversed_str_ite)
print('reversed_str is:', reversed_str)
print()

r = range(1, 10)
re_ite = reversed(r)
re = list(re_ite)
print('r is:', r)
print('re_ite is:', re_ite)
print('re is:', re)
