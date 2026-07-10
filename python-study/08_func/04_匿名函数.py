# 匿名函数
# 1. 格式： lambda 参数: 表达式
# 2. 用途： 用来封装简单、一次性逻辑，提升代码简洁性
# 3. 限制：
#    * 所有内容必须在一行，且只能有一个表达式
#    * 无需写return，自动将表达式的值返回

def calculate(func, x, y):
    return func(x, y)


# 加法实现
result1 = calculate(lambda x, y: x + y, 30, 20)
print(f'result1={result1}')
# 减法实现
result2 = calculate(lambda x, y: x - y, 30, 20)
print(f'result2={result2}')
print('-' * 40)

# 无参写法
lam_func1 = lambda : print('无参匿名函数')
lam_func1()
print('-' * 40)

# 多表达式，编译报错
# lam_func2 = lambda x: x + 10, x -10

#
lam_func3 = lambda x: x or isinstance(x, str)