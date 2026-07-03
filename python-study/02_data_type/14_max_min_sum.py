# 容器的一些内置函数
# 1. sorted()
# 2. reversed()
# 3. len()
# 4. max() / min() / sum()
# 5. all()
# 6. any()
# 7. enumerate()


# max() 返回容器中的最大元素
# min() 返回容器中最小元素

# list
rl = [1, 2, 3, 4, 5]
print('rl max ele is:', max(rl))
print('rl min ele is:', min(rl))
print('rl sum is:', sum(rl))
print()

rl1 = [1, 2, 3, 4, [4, 5]]
# 即含有数字，又含有list的集合使用max、min会异常，无法使用大于或小于比较int和list的大小
# print('rl1 max ele is:', max(rl1))
# print('rl1 min ele is:', min(rl1))
# 也无法使用sum， TypeError: unsupported operand type(s) for +: 'int' and 'list'
# print('rl1 sum is:', sum(rl1))
print()

# set
rs = {2, 3, 4, 5}
print('rs max ele is:', max(rs))
print('rs min ele is:', min(rs))
print('rs sum is', sum(rs))
print()

rt = (1, 2, 3, 4, 5)
print('rt max ele is:', max(rt))
print('rt min ele is:', min(rt))
print('rt sum is', sum(rt))
print()

dd = {1: "shanghai", 2: "beijing", 3: "shenzhen"}
print('dd max ele is:', max(dd))
print('dd min ele is:', min(dd))
print('dd sum is', sum(dd))
print()

d1 = {"shanghai": 1, "beijing": 2, "shenzhen": 3}
print('d1 max ele is:', max(d1))
print('d1 min ele is:', min(d1))
# key是字符串，无法求和 TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print('d1 sum is', sum(d1))
print()

str1 = 'HelloAIAgent'
print('str1 max ele is:', max(str1))
print('str1 min ele is:', min(str1))
# 字符串，无法求和 TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print('str1 sum is', sum(str1))
print()

r = range(1, 10)
print('r max ele is:', max(r))
print('r min ele is:', min(r))
print('r sum is:', sum(r))
print()
