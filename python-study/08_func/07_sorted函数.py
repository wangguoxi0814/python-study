# sorted函数, 对指定数据排序，默认升序,和filter和map不同的是，sorted会直接返回排序结果,不影响原始数据
# sorted(data, key, reversed)
#  data:     可迭代对象
#  key:      排序依据，适用于复杂结构元素
#  reversed：是否翻转

# 普通排序
l = [2, 1, 6, 4, 8]
sr = sorted(l)
print(f'排序原始数据：{l}')
print(f'升序结果：{sr}')
srd = sorted(l, reverse=True)
print(f'降序结果：{srd}')

# 字符出排序，默认按照字典码排
sl = ['Python', 'Go', 'Java']
ssl = sorted(sl, key=len)
print(f'长度升序结果：{ssl}')

# key的使用
dict_l = [
    {"name": "Peter", "age": 19, "gender": "女"},
    {"name": "Lucy", "age": 17, "gender": "女"},
    {"name": "Mary", "age": 18, "gender": "女"},
    {"name": "Curry", "age": 33, "gender": "女"}
]
ps = sorted(dict_l, key=lambda ele: ele['age'], reverse=True)
print(f'年龄降序结果：{ps}')

# 复杂对象
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __gt__(self, other):
        return self.age > other.age

    def __str__(self):
        return f'(name={self.name}, age={self.age}, gender={self.gender})'

pl = [
    Person('Peter', 19, "男"),
    Person('Lucy', 29, "女"),
    Person('Mary', 19, "女"),
    Person('Gan', 23, "男")
]
# 如果不指定key，会报TypeError: '<' not supported between instances of 'Person' and 'Person'
# 解决方法
# 1. sorted增加key指定排序依据
# 2. Person实现魔法方法__lt__或者__gt__

# 升序or降序，取决于__lt__或者__gt__实现逻辑
# Peter 和 Mary 年龄都是 19 时，两者比较都不为「更小」，排序视为相等；Timsort 稳定，保留原列表顺序，所以 Peter 在 Mary 前面。
pla = sorted(pl)
def print_sorted(plist):
    for p in plist:
        print(p, end=',')
    else:
        print()
print('升序===========================')
print_sorted(pla)

# 如果只实现了__lt__，猜想降序会报错 XXXX 猜想错误
# 所以无论升序，降序，只需要实现__lt__即可
pld = sorted(pl, reverse=True)
print('降序===========================')
print_sorted(pld)