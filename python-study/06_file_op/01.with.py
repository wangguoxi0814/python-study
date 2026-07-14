# with 
# 自动打开，自动关闭资源的语法
# with会调用实例的__enter__方法，退出时调用__exit__方法，即便with中的代码块发送异常，也会调用__exit__方法
# with...as...接受到的对象是__enter__方法的返回值
# __exit__方法的参数：exc_type, exc_val, exc_tb
# exc_type: 异常类型
# exc_val: 异常值
# exc_tb: 异常追踪
# 返回值：True表示异常被处理，False表示异常未被处理，会将异常抛到外面，不会被捕获

# with可以跟多个open，比如复制文件时，一个文件读取流，一个文件写入流
# with open(...) as f1, open(...) as f2:

with open('../../docs/withdemo.txt', 'r') as f:
    for line in f:
        print(line)

import time
class Timer:
    def __enter__(self):
        self.startTime = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.endTime = time.time()
        self.total = self.endTime - self.startTime
        print(f"Time taken: {self.total} seconds")
        return False
        

def newTimer():
    timer = Timer()
    return timer

with newTimer() as timer:
    print('timer is : ', timer)
    time.sleep(1)

print("2")
with Timer() as timer:
    print(timer)
    time.sleep(1)


# 异常处理情况
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __enter__(self):
        print('enter...')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit...')
        if exc_type:
            print(f'exe_type={exc_type}')
            print(f'exc_val={exc_val}')
            print(f'exc_tb={exc_tb}')
        # 返回True表示错误被处理，错误信息不会抛出去，False表示未处理，会抛出去
        return True

    def study(self):
        print(f'我是{self.name}, 今年{self.age}岁，我爱学习')

with Person('Peter', 18) as p:
    p.study()
    p.relax()