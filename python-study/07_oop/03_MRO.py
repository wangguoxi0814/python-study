# MRO链
# Python通过MRO解决菱形继承问题，MRO核心规则如下：
# 1. 子类永远在父类前面
# 2. 一个类只能在MRO序列中出现一次
# 3. 保持继承时左右书写的顺序
# 菱形继承：比如Person有Student和Worker两个子类，类InternationStudent继承Student和Woker，就形成了一个菱形
# 菱形继承主要问题：
# 1. 方法/属性歧义：如Student和Woker都实现了同一个方法，那么InternationStudent调用这个方法时，到底应该调用Student还是Worker的。
#    这个情况下，Python查找方法的顺序为：先在实例自身查找，然后再按照MRO链顺序查找，因此MRO成功解决了这个问题
# 2. 重复初始化：顶层类Person会被重复初始化
# 3. 状态不一致：Person类由于会被重复初始化，那如果后续的初始化值和第一次不相同，就会出现初始化值覆盖问题，导致状态不一致。
#    一个类在MRO序列中只会出现一次，super()也是把控制权交给MRO链中的下一个类执行, 即解决了重复初始化，自然也解决了这个问题

class A:
    def __init__(self):
        print("init A")

class B(A):
    def __init__(self):
        super().__init__()
        print("init B")

    def speak(self):
        print('B......')

class C(A):
    def __init__(self):
        super().__init__()
        print("init C")

    def speak(self):
        print('C....')

class D(B, C):
    def __init__(self):
        super().__init__()
        print("init D")

d = D()
d.speak()
# 输出顺序: init A -> init C -> init B -> init D
# A 只初始化一次
print(D.__mro__)
# 在super()调用时，按照MRO链走，而MRO链是 D -> B -> C -> A
# 1. 在D.__init__时super().__init__会按照链到达B.__init__
# 2. 在B.__init__中super().__init__会按照链到达C.__init__
# 3. 在C.__init__中super().__init__会按照链到达A.__init__
# 4. 所以输出顺序: init A -> init C -> init B -> init D


# 示例2
class P():
    def __init__(self):
        #
        # super().__init__()
        print('init P')

class M(P):
    def __init__(self):
        super().__init__()
        print('inti M')

class N:
    def __init__(self):
        super().__init__()
        print('init N')

class Y(M, N):
    def __init__(self):
        super().__init__()
        print('init Y')

Y()
# MRO链：Y, M, P, N
# 所以执行顺序是: init P -> inti M -> init Y (这里并不会输出init N,因为在Y中并没有执行super().__init__，因此在MRO链中，执行到P就结束了)
# 所以，在多继承里，super()并不像单继承那样是调用自己的父类，而是基于MRO这条生产线的协作式多继承，super()是指自己这部分做完了，交给下一个节点执行
# 如果想要输出N，需要再P.__init__中加上super().__init__