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

# list中的元素全是字符串，则按照字典排序
# 字典排序规则：
# 1. 字母比较ASCII码，中文比价Unicode码
# 2. 按序比较字符，如果第1个字符相同，则比较第二个字符。什么时候“分出胜负”，什么时候就结束。
# 3. 短字符串和长字符串比较，如果直到短字符串结束都没分出“胜负”，则可以理解短字符串后续总是拿空字符和长字符串的字符比较，即恒小于

al1 = ['bc', 'acd']
al1.sort()
print('al1 after sorting is:', al1)
# ord函数可以查看字母的ASCII码
print('a ord is', ord('a'))
print('b ord is', ord('b'))

al = ['ac', 'ab']
al.sort()
print('al after sorting is:', al)

bl = ['bcdef', 'bcd']
bl.sort()
print('bl after sorting is:', bl)

city_list = ['北京', '北海', '深圳']
city_list.sort()
print('city_list after sort is:', city_list)
# 这里是根据unicode编码排序， 可以通过ord查看中文的unicode码
print('北 ord is', ord('北'))
print('深 ord is', ord('深'))
print('京 ord is', ord('京'))
print('海 ord is', ord('海'))

# 同时有数字和字符串，排序会报错：TypeError: '<' not supported between instances of 'str' and 'int'
# list4 = [1,2,3, "深圳"]
# list4.sort()
# print('list 4 is:', list4)