# 函数注解
# 给函数入参和返回值的类型注解

# 示例1
def test1(a: int, b: int) -> int:
    return a * b


# 示例2: 参数如果给默认值，python会自动推断类型
def test2(a=0, b=0) -> int:
    return a + b


# test2('a', 'b')


# 示例3：多返回值类型注解
def test3(a: int, b: int) -> tuple[int, int, float]:
    k = a / b
    m = a // b
    j = a % b
    return m, j, k


x, y, z = test3(10, 3)
print(x, y, z)


# 示例4：动态位置参数
def test4(*args: int):
    print(args)


test4(1, 2)


def test5(**kwargs: int | str):
    print(kwargs)


test5(name='Peter', age=26, gender='男')
