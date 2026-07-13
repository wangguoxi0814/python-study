# 自定义迭代器实现斐波那契
class Fibonacci:

    def __init__(self, num):
        if num < 1:
            raise ValueError('num非法， 不能小于1')
        self.num = num

    def __iter__(self):
        self.val = 0
        self.step = 1
        self.count = 0
        return self

    def __next__(self):
        if self.count >= self.num:
            raise StopIteration
        f = self.val
        self.val, self.step = self.step, self.val + self.step
        self.count += 1
        return f


fib = Fibonacci(10)
for i in fib:
    print(i, end=' ')
else:
    print()
