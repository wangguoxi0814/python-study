# 类装饰器
# 类装饰器需要实现__call__方法，且必须返回一个函数
# 带参的类装饰器通过__init__接受参数，比函数装饰器更简洁
# 类装饰器使用必须带括号：@xxx()

class Tool:

    def __init__(self, name='', desc=''):
        self.name = name
        self.desc = desc

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'{self.name}工具执行 - {self.desc}')
            return func(*args, **kwargs)

        return wrapper


class Log:
    def __init__(self, log_level):
        self.log_level = log_level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'{self.log_level}日志记录开始')
            res = func(*args, **kwargs)
            print(f'{self.log_level}日志记录结束')
            return res

        return wrapper


@Tool(name="查询天气", desc="外部实时天气API调用")
def get_weather():
    return "Hello！"


print(f'get_weather: {get_weather()}')


@Log(log_level='[INFO]')
@Tool(name='快递通知', desc='快递实时通知')
def delivery():
    return "快递投递"


print(f'delivery: {delivery()}')
