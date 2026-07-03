# list常用的其他API

# count 统计元素出现的次数
list1 = [2,4,6,8,2,9,8,7,7,7]
print('7出现次数：', list1.count(7))

# reverse 反转，对容器本身进行反转，不会生成返回新的容器
list2 = [1,2,3,4,5]
r_list = list2.reverse()    # None 因为reverse没有返回值
print('r_list is:', r_list)
print('reversed list2 is:', list2)


# sort 默认升序,通过reverse=True，指定降序，如果同时有数字和字符串，会报错
list3 = [7,6,4,5,2,2]
# list3.sort()          # 升序
list3.sort(reverse=True) # 降序
print('list3 is:', list3)

# 同时有数字和字符串，排序会报错：TypeError: '<' not supported between instances of 'str' and 'int'
# list4 = [1,2,3, "深圳"]
# list4.sort()
# print('list 4 is:', list4)