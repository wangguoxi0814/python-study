# Python通过MRO解决菱形继承问题，核心规则如下：
# 1. 子类永远在父类前面
# 2. 一个类只能在MRO序列中出现一次
# 3. 保持继承时左右书写的顺序
# 菱形问题：比如Person有Student和Worker两个子类，类InternationStudent继承Student和Woker，就形成了一个菱形


class Person:
    def __init__(self):
        print("Person init")

class S1(Person):
    def __init__(self):
        super().__init__()
        print("S1 init")

class S2(Person):
    def __init__(self):
        super().__init__()
        print("S2 init")

class P(S1, S2):
    def __init__(self):
        super().__init__()

p = P()