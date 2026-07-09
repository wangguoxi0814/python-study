# 一个函数可以有多个返回值，比如return a, b
# 打包(pack):
#   返回值：多个返回值会自动打包为tuple。
#   入参：*args,**kwargs会自动将位置参数和关键字参数打包为tuple和dict
# 拆包(unpack):
#   返回值：接收时可自动拆分为多个变量,而不用操作tuple
#   入参：func(*[1,2,3])将序列拆分为位置参数;func(**{'a':1})将字典拆分为关键字参数

# 多返回值
def get_stats():
    return 0, 1, 2


a = get_stats()
print(f'a| type: {a}')
# 拆包
created, submitted, checked = get_stats()
print(f'created:{created}, submitted:{submitted}, checked:{checked}')
print('-' * 30)


def func1(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


# 打包
func1('Peter', 18, gender='男', addr='广东')

# 解包
basic_info = ['Peter', 18]
other_info = {'gender': '男', 'addr': '广东'}
func1(*basic_info, **other_info)
