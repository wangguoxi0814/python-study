# 方法，是一个功能集合
# 一个方法有方法体、参数、返回值、异常
# 方法参数默认必填，设置默认值后变为非必填
# 调用方法时，传参方式分为位置传参和关键字传参
# 方法可以限制参数的传参方式，限制符为：/ 和 *
    # /前面的参数只允许位置参数
    # *后面的参数只允许关键字参数
    # / 不能在*的后面，因为这样夹在他们中间的参数到底是位置参数还是关键字参数呢？矛盾。
    # 在保证/必须在*之前的规则，因此夹在他们中间的参数允许位置参数和关键字参数
    # 示例： def func2(name, /, age, *, gender)
    # 这里的name只允许位置参数, age即允许位置参数，也允许关键字参数；gender只允许关键字参数
# 方法支持可变参数
# 方法默认的返回值为None，
# 方法的返回值可以有多个
# 一个方法可以被调用

# 定义一个简单方法
def print_num():
    print('print_num num=', 1)
    print()

# 函数调用
print_num()

# 定义一个有参数的方法
def func2(name):
    print(f'func2 name={name}')
    print()
func2("Peter")

# 多个参数,默认都是必填
def func3(name, age, gender):
    print(f'func3 name={name},age={age},gender={gender}')
    print()
# 调用时要严格遵守顺序,且不能跳过某个位置的参数，这是位置参数入参方法
func3("Peter", 18, '男')
# 同时支持关键字参数入参，可以不遵守顺序，也可以跳过参数
func3("Perter", gender="男", age="18")
# 关键字参数必须放在最后，这种方式就是错的
# func3("Perter", gender="男", "18")

# 给方法参数设置默认值
def func4(name, age, gender='男'):
    print(f'func4 name={name},age={age},gender={gender}')
    print()

func4("张三", 18)


# 限定传参方式
def func5(name, /, age, *, gender):
    print(f'func4 name={name},age={age},gender={gender}')

func5("Peter", 18, gender="男")
func5("Lucy", age=18, gender="女")
# gender是关键字参数，不能当做顺序参数,会异常
# func5("Peter", 18, "男")

# 可变参数, 可以不传，也可以穿多个，多个参数不用容器封装
# *标识可变顺序参数，会将传入的多个参数自动打包为tuple
# **标识可变关键字参数, 会将传入的多个参数自动打包为dict
def func6(*args, **kwargs):
    print(f'args type is {type(args)}')  #tuple
    print(f'kwargs type is {type(kwargs)}') # dict
    print(f'args is {args}')
    print(f'kwargs is {kwargs}')
    print()

func6()
func6('Peter', 'Lucy', 'Marry', city='深圳', province='广东', country='中国')


# 方法返回值，方法的执行结果
# 关键字return返回，同时函数结束运行
def func7():
    return 1
    # return后程序就结束，因此return后面不能再声明内容了
    # print()
a = func7()
print(f'func 7 return result is {a}')
print()

# 多个返回值，用逗号隔开
def func_demo():
    return 1, 'Peter'
seq, name = func_demo()
print(f'seq={seq}, name={name}')
print()

# 抛出异常，方法执行结束
# 异常用于显示告知调用方异常情况
def get_user_by_user_id(user_id):
    if user_id is None:
        raise ValueError('user_id is None')
    print(f'user_id={user_id}')
get_user_by_user_id(1) # 正常执行
get_user_by_user_id(None)