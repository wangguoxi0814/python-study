# 抽象类
# 1.必须要继承ABC，ABC会阻止抽象类实例化;
# 2.@abstractmethod声明抽象方法，编译器能识别未实现抽象方法的类并给出警告
# 3.pass占位
# 类继承抽象类必须要实现所有抽象方法
# 抽象类不能被实例化
from abc import ABC, abstractmethod


class Human(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass


class Man(Human):
    def speak(self):
        print(f'男人说Ta叫：{self.name},今年{self.age}岁')


class Woman(Human):
    def speak(self):
        print(f'女人说Ta叫：{self.name},今年{self.age}岁')


def speak(human: Human):
    human.speak()

# 抽象类不能被实例化:TypeError: Can't instantiate abstract class Human without an implementation for abstract method 'speak'
# h = Human('Peter', 27)
# print(h)

