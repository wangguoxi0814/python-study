# Set是集合，是无序的，元素唯一的，可变的
# Set因为是无序的，所以不支持索引,所以也不支持切片
# Set支持交集、并集、差集、对称差集、遍历、长度、判断元素是否存在等操作

# 创建空set必须用set()
empty_set = set()
print('empty_set is ', empty_set)

# 创建非空set
set1 = {1, 'Hello', 3.14, -1}
print('set1 is ', set1)
print('set1 len is ', len(set1))

# 遍历
for s in set1:
    print(s, end=' ')

# 判断元素是否在set中
if 1 in set1:
    print('1 is in set1')
elif 'Hello' in set1:
    print('Hello is in set1')
else:
    print('not in set1')


set2 = {1,2,3,4}
set3 = {3,4,5,6}
# 交集
print('交集：',set2 & set3)
# 并集
print('并集：',set2 | set3)
# 差集
print('差集：', set2 - set3)
# 对称差集
print('对称差集：', set2 * set3)