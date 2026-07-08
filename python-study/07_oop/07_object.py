# object 所有类的父类

# 判断是否是其子类 issubclass()
# 判断是否是其实例 isinstance()   这里不仅可以传实例，也可以传类名，因为类本身是type()这个元类创建的实例

class Person:
    pass


print(issubclass(Person, object))
print(issubclass(int, object))
print(issubclass(bool, object))
print(issubclass(list, object))
print(issubclass(tuple, object))
print(issubclass(dict, object))
print(issubclass(set, object))
print(issubclass(float, object))

print('==========================')
p = Person()
print(isinstance(Person, object))
print(isinstance(p, object))
print(isinstance(True, object))
print(isinstance(1, object))
print(isinstance(1.2, object))
print(isinstance({1, 2, 3}, object))
print(isinstance((1, 2, 3), object))
print(isinstance([1, 2, 3], object))
print(isinstance({'a': 1, 'b': 2, 'c': 3}, object))
print(isinstance(None, object))

print('=====================')
p.name = 'Peter'
print(p.__dict__)  # 返回实例信息
print(dir(p))  # 返回从object继承的信息和实例自身的信息
