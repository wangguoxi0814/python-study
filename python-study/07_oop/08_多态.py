# 多态，父类参数可以接受子类实例，并触发同样的行为
# 在方法参数中加上类型注解，也不会强制要求传入这个类型，编译器只会警告
# Python有一个编程范式要鸭子多条，不要求入参具有继承关系，只要有相同的行为即可
class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'人说Ta叫：{self.name},今年{self.age}岁')

class Man(Human):

    def speak(self):
        print(f'男人说Ta叫：{self.name},今年{self.age}岁')

class Woman(Human):

    def speak(self):
        print(f'女人说Ta叫：{self.name},今年{self.age}岁')

def speak(human: Human):
    human.speak()

h = Human('Hope', 28)
speak(h)
m = Man('Peter', 26)
speak(m)
w = Woman('Mary',20)
speak(w)

class Cat:
    def speak(self):
        print('喵喵喵')

def talk(obj):
    obj.speak()

# 鸭子多态,入参可以是毫无关系的类，只要有相同行为即可
c = Cat()
talk(h)
talk(m)
talk(w)
talk(c)