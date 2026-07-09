# 函数本身也是一个类
# 函数参数是引用传递
# 函数可以赋值给另外的变量
# 函数可以添加属性
# 函数可以作为参数传入
# 函数可以作为返回值

def fun1():
    print('have fun...')

print(type(fun1))


# 方法参数是引用传递，但由于int不可变，在方法内部修改变量时，会重新开辟一个变量，赋值给p，因此对外部的a没有影响
a = 100
def update(p):
    print(f'修改前p: {p}')
    p = 10
    print(f'修改后p: {p}')
print(f'方法执行前a:{a}')
update(a)
print(f'方法执行后a:{a}')

# 在方法内部修改时，会修改l这块内存区域的内容，因此l会受到影响
l = [1,2,3]
def update_list(l):
    print(f'修改前l:{l}')
    l[2] = 100
    print(f'修改后l:{l}')
update_list(l)
print(f'方法调用后l:{l}')

# 函数可以赋值给变量
def val_fun():
    print('val fun...')
fun_a = val_fun
fun_a()

val_fun.desc = '简单打印'
print(f'val_fun desc: {val_fun.desc}')
print(f'val_fun doc: {val_fun.__doc__}')


def func_caller(func):
    print('函数回调开始')
    func()
    print('函数回调结束')

func_caller(val_fun)

def func_generate():
    print('构建函数开始')
    def add(a, b):
        return a + b
    return add

calc_func = func_generate()
result = calc_func(1, 2)
print(f'result: {result}')

