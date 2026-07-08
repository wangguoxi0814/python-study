# 魔法方法, 以__xxx__命名的特殊方法，不需要手动调用，在特定场景下，自动执行
# 1. __str__      调用str(obj)和print(obj)时执行，返回字符串
# 2. __len__      调用len(obj)时执行，反正整形
# 3. __lt__       调用 ob1 < ob2 时执行，返回布尔
# 4. __gt__       调用 ob1 > ob2 时执行，返回布尔
# 5. __eq__       调用 ob1 == ob2 时执行，返回布尔
# 6. __getattr__  访问不存在的变量时执行, 返回字符串

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name={self.name},age={self.age}'

    def __len__(self):
        return len(self.__dict__)

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.__dict__ == self.__dict__

    def __getattr__(self, item):
        return f'{item}不存在'


p = Person('Peter', 26)
print(p)
ps = str(p)
print(ps)
print(f'len:{len(p)}')

mp = Person('Mary', 24)
print(p < mp)

print(p.address)



