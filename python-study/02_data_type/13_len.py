# 容器的一些内置函数
# 1. sorted()
# 2. reversed()
# 3. len()
# 4. max() / min() / sum()
# 5. all()
# 6. any()
# 7. enumerate()


# len() 返回容器长度（即元素个数）
rl = [1, 2, 3, 4, 5]
print('rl len is:', len(rl))

rl1 = [1, 2, 3, 4, [4, 5]]
print('rl1 len is:', len(rl1))
print()

# set是无序的，它本身就没有reverse方法，当然内置函数reversed()也无法操作它。因为既然无序，何来反转呢？
# TypeError: 'set' object is not reversible
rs = {2, 3, 4, 5}
sl = len(rs)
print('rs len is:', sl)
print()

rt = (1, 2, 3, 4, 5)
tl = len(rt)
print('rt len is:', tl)
print()

d1 = {"shanghai": 1, "beijing": 2, "shenzhen":3}
print('d1 len is:', len(d1))
print()

str = 'Hello AI Agent'
str_len = len(str)
print('str len is:', str_len)
print()

r = range(1, 10)
range_len = len(r)
print('r len is:', range_len)
print()

