# tuple的其他常用API

# count 统计元素个数
t1 = (4, 5, 2, 1, 3, 9)
print('tuple ele count:', t1.count(5))

# tuple没有reverse，因为tuple不可变，而reverse是原地修改容器，矛盾

# tuple也没有sort方法，也是因为tuple不可变，而sort是原地排序，矛盾