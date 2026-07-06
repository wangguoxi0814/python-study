# yield生成器
# 生成器是一种特殊的迭代器，可以生成一个序列，每次调用next()方法时，生成器会返回一个值，直到生成器结束
# yield有点类似DEBUG的断点，执行到yield时，会暂停，并返回一个值，下次调用next()方法时，会从上次暂停的地方继续执行
# 如果yield所在方法执行结束，还调用next()会出现StopIteration异常
print("=============1==============")


def count_down(f):
    while f >= 0:
        yield f
        f -= 1


count = count_down(10)
print(count)  # generator
# for i in count:
#     print(i, end=' ')
# print()
i1 = next(count)
print(i1)
i2 = next(count)
print(i2)
i3 = next(count)
print(i3)
i4 = next(count)
print(i4)
i5 = next(count)
print(i5)

print("=============2==============")


# 生成器可以用于生成一个无限的序列，比如斐波那契数列
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter >= n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(100)
# i = 0
# while i<10:
#     i = i + 1
#     print(f'第{i}个fib number：{next(f)}')


for i in f:
    print(i, end=' ')
print()

# 生成器可以用于生成一个有限的序列，比如一个列表
print("=============3==============")


def myGenerator():
    yield 1
    yield 2
    yield 3


g = myGenerator()
print(next(g))
print(next(g))



