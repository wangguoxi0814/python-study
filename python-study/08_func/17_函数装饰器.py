# 函数装饰器
# 普通函数装饰器
# 带参函数装饰器。修饰方法，尽管目标方法不执行，执行逻辑也等价于 log(log_type)(target_func)
# 如果一个函数被多个装饰器修饰，就近原则

# 普通装饰器
def info(func):
    def wrapper(*args, **kwargs):
        print(f'[INFO] func start')
        res = func(*args, **kwargs)
        print(f'[INFO] func end')
        return res

    return wrapper


# @info
# def add(a, b):
#     return a + b
#
#
# # 加了@info，会经过装饰器，等价于下面的调用
# add(1, 2)
# # 装饰器原生逻辑
# info_result = info(add)
# r = info_result(3, 5)
# print(f'原生装饰器逻辑结果：{r}')


# 带参装饰器
def log(log_type: str):
    def log_wrapper(func):

        def wrapper(*args, **kwargs):
            print(f'{log_type}函数执行开始')
            res = func(*args, **kwargs)
            print(f'{log_type}函数执行结束')
            return res

        return wrapper

    return log_wrapper


@log("[INFO]")
def subtract(a, b):
    return a - b


# print(subtract(3, 2))

# 原生带参装饰器逻辑
# log_func = log('[WARNING]')
# wrapper = log_func(subtract)
# re = wrapper(8, 4)
# print(f'多参数装饰器原生逻辑执行结果：{re}')


# 多个装饰器执行链路等价于：info(log('[WARNING]')(multiply))
@info
@log('[WARNING]')
def multiply(a, b):
    return a * b


result = multiply(8, 8)
print(f'result: {result}')
