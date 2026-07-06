import types

# 类
# 类的创建
# 初始化方法
# 实例方法
# 实例方法重写
    #  types.MethodType重写方法绑定self
# 类方法   @classmethod   类调用，但实例也可以调用，但极不推荐 第一个参数是cls
# 静态方法  @staticmethod  类调用，但实例也可以调用，但极不推荐 没有cls，self参数

class Person:

    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def speak(self):
        print(f'{self.name}正在说话中。。。')

    # 类方法, 实例工厂
    @classmethod
    def create(cls, name, age):
        return cls(name, age)

    @staticmethod
    def mask_idcard(idcard):
        return idcard[:6] + "*******" + idcard[-4:]

# 创建实例
p1 = Person("Peter", 20)
p1.speak()
# 查看实例结构
print(f'Person dict: {p1.__dict__}')
# 实例重写方法
def speak():
    print('Peter说英语')
p1.speak = speak
p1.speak()

# 如果重写方法，要使用self，标准做法通过types.MethodType绑定实例
def run(self):
    print(f'{self.name}在奔跑')
p1.run = types.MethodType(run, p1)
p1.run()

# 查看实例结构
print(f'p1 dict: {p1.__dict__}')

# 调用类工程方法创建实例
p2 = Person.create("Henry", 19)
print(f'p2: {p2.__dict__}')

# 查看类的结构
print(f'Person dict: {Person.__dict__}')


mask_id = Person.mask_idcard("430902199908145537")
print(f'mask_id :{mask_id}')