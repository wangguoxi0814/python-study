# 文档字符串
# 文档字符串是用来描述模块、类、函数、方法等内容的字符串，通常用于解释代码的作用、参数、返回值等
# 文档字符串使用三引号（''' 或 """）来定义，通常位于模块、类、函数、方法的第一个位置

# 获取方式：
# 1. 使用__doc__属性
# 2. 使用help()函数,会多输出函数所在的模块，函数声明
# 3. 使用inspect模块


## 示例：类文档字符串


class RateLimiter:
    """Token-bucket rate limiter.

    This limiter allows up to `capacity` tokens and refills at `rate` tokens/second.

    Args:
        capacity: Maximum number of tokens.
        rate: Refill rate (tokens per second).

    Attributes:
        capacity: Maximum number of tokens.
        rate: Refill rate (tokens per second).

    Raises:
        ValueError: If capacity or rate is not positive.
    """

    def __init__(self, capacity: int, rate: float) -> None:
        if capacity <= 0 or rate <= 0:
            raise ValueError("capacity and rate must be positive")
        self.capacity = capacity
        self.rate = rate


# 获取类文档字符串
print('===============__doc__===========')
print(RateLimiter.__doc__)

print('===========================help()===========================')
print(help(RateLimiter))

print('===========================inspect.getdoc()===========================')
import inspect
print(inspect.getdoc(RateLimiter))