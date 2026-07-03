# 容器的一些内置函数
# 1. sorted()
# 2. reversed()
# 3. len()
# 4. max() / min() / sum()
# 5. all()
# 6. any()
# 7. enumerate()


# reversed() 反转， 不是原地反转，会返回结果为reverseiterator，即反转迭代器对象，这样不会一次性把反转结果放到内存，而是使用时，再逐个生成结果
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
