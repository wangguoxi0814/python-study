# getter&setter方法
# 需要使用装饰器：
# 1. @property  表示getter方法,命名通常和变量名的字母部分保持一致
# 2. @属性名.setter 表示 setter方法
# 扩展： deleter方法
# 装饰器 @属性名.deleter, 通过del 实例.属性触发

# 解读
# 1. @property相当于设置一个和方法名相同的属性， 假设方法名为age1，此时的产物：age1 = property(getter)   # 只有 getter 的age1
# 2. @属性名.setter中的属性名需要和@property设置的属性名保持一致，但方法名可以随意（但规范为和@property保持一致），假设方法名为age
# ,产物为：age = age1.setter(age), 因此age拥有getter和setter,此时类存在2个属性，分别是age1和age
# 3. @属性名.deleter这个时候的属性名可以使用age和age1.因为这2个变量都存在
# 4. 因此只有getter、setter、deleter方法名都保持一致，才能消除这种多个变量都存在的杂乱情况
# 5. setter和deleter必须写在getter后面

class Person:

    def __init__(self, name, age, idcard):
        self.name = name
        self._age = age
        self.__idcard = idcard

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        print('age setter 触发')
        self._age = value

    @age.deleter
    def age(self):
        print('age deleter触发')
        del self._age

p = Person('peter', 27, '')
print(p.age)
p.age = 18
print(p.age)
print(p.__dict__)
del p.age
# 删除后，如果再调用getter方法，会异常,因为属性已经不存在了
# print(p.age)
print(p.__dict__)