# 变量类型注解，限制变量的类型，或者容器内部元素的类型

s: str = "Hello"
print(s)
s = 1  # 警告
print(s)

# 容器, list, set同样写法
l: list[int] = [1, 2, 3]
ls: list[int | str] = [1, 'Hello']

# dict
d: dict[str, int] = {'US': 90, 'CN': 99}
m: dict[str | int, int] = {'US': 90, 'CN': 99, 100: 100}

# tuple tuple的类型注解要和元素数量一致
# 指定个数
t: tuple[int] = (1,)
t1: tuple[int, int, int] = (1, 2, 3)
# 多个
t2: tuple[int, ...] = (1, 2, 3, 4)
t3: tuple[int | str, ...] = (1, 2, "Hello", 3)
