# python三种访问权限，通过变量_数量来区分
# (0个_)xx表示公开变量，可见范围：类内部，子类，其他无关类
# (1个_)_xx表示受保护的变量，可见范围：类内部，子类, 当然在其他地方也可以直接使用，但编译器会警告
# (2个_)__xx表示私有变量，可见范围：类内部。原理，同构__dict__可以看到，私有变量名会被重写为：类名__xx

class Person:

    def __init__(self, name, age, idcard):
        self.name = name
        self._age = age
        self.__idcard = idcard

    def delivery(self):
        print(f'填写快递单，名字{self.name},今年{self._age},身份证号：{self.__idcard}')

class Man(Person):

    def speak(self):
        # 子类继承不到私有变量，或者说私有变量在子类不可见，因此如果在这里使用私有变量，会报：'Man' object has no attribute '_Man__iddcard'
        # print(f'我叫{self.name}, 今年{self._age}岁，可以看下我身份证号：{self.__iddcard}')
        print(f'我叫{self.name}, 今年{self._age}岁')


m = Man('Peter', 26, 543243243243242)
print(f'age： {m._age}')  # 编译器警告
m.speak()
m.delivery()