# max和min也支持key作为排序依据

l = [2, 1, 6, 4, 8]
sr = max(l)
print(f'排序原始数据：{l}')
print(f'最大元素：{sr}')

# max排序字符串，默认取ASCII码最大值
sl = ['Python', 'Go', 'Java']
ssl = max(sl, key=len)
print(f'长度最长元素：{ssl}')

# max 和min key的使用
dict_l = [
    {"name": "Peter", "age": 19, "gender": "女"},
    {"name": "Lucy", "age": 17, "gender": "女"},
    {"name": "Mary", "age": 18, "gender": "女"},
    {"name": "Curry", "age": 33, "gender": "女"}
]
p_max = max(dict_l, key=lambda ele: ele['age'])
print(f'年龄最大的人：{p_max}')
p_min = min(dict_l, key=lambda ele: ele['age'])
print(f'年龄最小的人：{p_min}')


# 复杂对象
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __lt__(self, other):
        return self.age < other.age

    def __str__(self):
        return f'(name={self.name}, age={self.age}, gender={self.gender})'

pl = [
    Person('Peter', 19, "男"),
    Person('Lucy', 29, "女"),
    Person('Mary', 19, "女"),
    Person('Gan', 23, "男")
]

# max操作复杂对象时，也会按照__lt__和__gt__的实现方式来取值
# tips: max并不能始终取最大值，这个如果在实现了魔法方法情况下，完全取决于魔法方法逻辑
# 比如：
# def __lt__(self, other):
#     return self.age < other.age
# max和min就分别取了真的最大和最小值
# 如果
# def __lt__(self, other):
#     return self.age > other.age
# max 和 min 分别是取了最小和最大值（互相颠倒）
pla = max(pl)
print(f'最大年龄的人: {pla}')

pld = min(pl)
print(f'最小年龄的人: {pld}')
