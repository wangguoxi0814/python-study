# with 
# 自动打开，自动关闭资源的语法
# with会调用类的__enter__方法，退出时调用__exit__方法
# with...as...接受到的对象是__enter__方法的返回值
# __exit__方法的参数：exc_type, exc_val, exc_tb
# exc_type: 异常类型
# exc_val: 异常值
# exc_tb: 异常追踪
# 返回值：True表示异常被处理，False表示异常未被处理，会将异常抛到外面，不会被捕获


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
