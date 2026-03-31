# List类型:列表，可以包含多个元素，且类型可以不同
# List是一种连续、有序、可变的数据类型


# 创建列表
list1 = [1, "hello", True, 3.14, 100]
print('list1:', list1)
print('list1的长度：', len(list1))

# 通过索引访问列表元素
# 和字符串一样，索引从左到右，从0开始，到len(list1) - 1
# 索引从右到左，从-1开始，到 0 - len(list1) 结束
print('list1[0]:', list1[0])
print('list1[-1]:', list1[-1])
print('list1[len(list1) - 1]:', list1[len(list1) - 1])
print('list1[0 - len(list1)]:', list1[0 - len(list1)])

# 遍历
for item in list1:
    print(item, end=' ')

# 切片,左闭右开，支持步长，步长默认为1，为负数则逆序
print('list1[1:3]=', list1[1:3])
print('list1[1:]=', list1[1:])
print('list1[:3]=', list1[:3])
print('list1[:]=', list1[:])
print('list1[::2]=', list1[::2])
print('list1[1::2]=', list1[1::2])
print('list1[-1::-1]=', list1[-1::-1])
print('list1[-3::-1]=', list1[-3::-1])
print('list1[-3:]=', list1[-3:])
print('list1[-3::-1]=', list1[-3::-1])

# 可变
list2 = [1,2,3,4,5,6,7,8,9]
list2[0] = 10
print('list2=', list2)
list2[1:4] = [2, 3, 4]
print('list2=', list2)
list2[4:6] = [50,51,60,61]
print('list2=', list2)
list2[-3:] = [90,91,92]
print('list2=', list2)

list3 = [1,2]
list3[-2:-1] = [10,20]
print('list3=', list3)
list3[-1:-3:-1] = [11,12]
print('list3=', list3)
# -1是无法向右步进到-3的，所以是插入
list3[-1:-3] = [30,40]
print('list3=', list3)
