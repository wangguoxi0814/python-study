# List类型:列表，可以包含多个元素，且类型可以不同
# List是一种连续、有序、可变的数据类型

# 构造器构建list
lc = list()
print('lc is:', lc)
lc = list((1,2,3))
print('lc is:', lc)

# 创建列表
list1 = [1, "hello", True, 3.14, 100]
print('list1:', list1)
print('list1的长度：', len(list1))
double_list = list1 * 2
print('double_list=', double_list)
tiny_list = ['tiny', 'mini']
print('list1 + tiny_list=', list1 + tiny_list)

# 追加
list_append = [1,2,3]
list_append.append(4)
print('list_append is:', list_append)
# append 会把整个对象当做一个元素
list_append.append([5,6])
print('list_append is:', list_append)

# 扩展
list_extend = [1,2,3]
# append会把[4,5]当做一个整体，而extend会把他拆开，再追加
list_extend.extend([4,5])
print('list_extend is:', list_extend)

# 通过索引访问列表元素
# 和字符串一样，索引从左到右，从0开始，到len(list1) - 1
# 索引从右到左，从-1开始，到 0 - len(list1) 结束
# list1 = [1, "hello", True, 3.14, 100]
print('list1[0]:', list1[0])
print('list1[-1]:', list1[-1])
print('list1[len(list1) - 1]:', list1[len(list1) - 1])
print('list1[0 - len(list1)]:', list1[0 - len(list1)])

# 遍历
for item in list1:
    print(item, end=' ')

print()
# 切片,左闭右开，支持步长，步长默认为1，负数步长则逆序
# list1 = [1, "hello", True, 3.14, 100]
print('list1[1:1]=', list1[1:1])  # 空切片,左闭右开，这个索引区间为[1,1),这个区间在数学里是空集，也就是这个索引区间不包含1这个索引，因此空切片
print('list1[-1:-3]=', list1[-1:-3]) # 空切片, -1正向不可达-3，因此空切片
print('list1[1::8]=', list1[1::8])   # 收集索引1,9,17,但仅索引1有效，所以输出hello
print('list1[1:3]=', list1[1:3])
print('list1[1:]=', list1[1:])
print('list1[:3]=', list1[:3])
print('list1[:]=', list1[:])
print('list1[::2]=', list1[::2])
print('list1[1::2]=', list1[1::2])
print('list1[-1::-1]=', list1[-1::-1])
print('list1[-3::-1]=', list1[-3::-1])
print('list1[-3:]=', list1[-3:])

# 插入
list_insert = [1,2,3]
# insert的index超过list的最大索引，不会报错，强制追加在最后一位
list_insert.insert(5, 6)
print('list_insert is:', list_insert)
# 在指定索引位置插入元素
list_insert.insert(3, 6)
print('list_insert is:', list_insert)
# 在指定位置插入[100, 1000]
list_insert.insert(2, [100,1000])
print('list_insert is:', list_insert)

# remove 按元素移除, 没有返回值
list_remove = [1,2,3]
remove_ele = list_remove.remove(2)  # None
print(f'list remove ele is {remove_ele}')
print('list_remove is:', list_remove)

# pop 弹出 返回弹出的元素
# pop 移除指定位置的元素，如果不指定位置，则移除列表最后一个元素
l_pop1 = [1,2,3]
pop_ele = l_pop1.pop()
print(f'pop ele is {pop_ele}')
print(f'pop ele l_pop1 is {l_pop1}')
print()

l_pop2 = [1,2,3]
first_ele = l_pop2.pop(0)
print(f'first_ele is {first_ele}')
print(f'pop ele l_pop2 is {l_pop2}')
print()

# del按索引移除, 没有返回值
l_del = [1,2,3]
del l_del[2]  # 删除索引位置2的元素
print(f'del ele l_del is {l_del}')
print()

# 可变
list2 = [1,2,3,4,5,6,7,8,9]
list2[0] = 10
print('list2=', list2)
list2[1:4] = [20, 30, 40]
print('list2=', list2)
list2[4:6] = [50,51,60,61]
print('list2=', list2)
list2[-3:] = [90,91,92]
print('list2=', list2)

list3 = [1,2]
list3[-2:-1] = [10,20]
print('list3=', list3)      # [10,20,2]
list3[-1:-3:-1] = [11,12]
print('list3=', list3)      # [10, 12, 11]
# -1是无法向右步进到-3的，是空切片，因此不会发生替换，而是插入
print('list3[-1:-3]=', list3[-1:-3])
list3[-1:-3] = [30,40]
print('list3=', list3)      # [10, 12, 30, 40, 11]


# 判断元素是否存在
list_con = [1, 2, 3]
print("1存在于list中", 1 in list_con)