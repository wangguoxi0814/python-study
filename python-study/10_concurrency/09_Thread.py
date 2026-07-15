# 多线程
# 多线程不必须在main方法中运行，子线程不会重复执行当前模块代码，因此内存是共享的

# Thread参数:
#   group:                分组，默认为None，且只能为None
#   target:               执行函数
#   name:                 线程名称，不传由Python自动分配
#   args:                 target函数位置参数入参，类型元组
#   kwargs:               target函数关键字参数入参，类型字典
#   daemon:               是否为守护线程，bool类型

# 线程锁
# 1. Lock： 不可重入锁， RLock: 可重入锁。 API相同：
#       a. lock.acquire()上锁、lock.release()释放锁
#       b. 最佳实践： with lock

# join()
# p.join()会让当前线程等待p线程执行完再执行，p.join(timeout)可以指定等待时间
# join只能操作已经start的线程

# terminate()
# p.terminate() 强制终止p线程，不会执行target方法的finally块；
# 异步执行，调用不代表立即终止线程，通过p.is_alive()查看时可能为True，需要配合p.join()才能获取真实线程状态

# 守护线程
# 1. 守护线程中不能再创建子线程
# 2. 守护线程在主线程执行完就销毁
#       示例： 主线程开辟了p1(守护线程)， p2(非守护线程)
#              1. 主线程执行完毕，进入销毁流程时，会先杀掉守护线程，再判断是否还有子线程存活，如果有，则会等待子线程执行完毕再销毁，也就是这个时候主线程和普通子线程还存活，但守护线程已经被杀死了
# 适用场景：后台监控、统计、采样任务等


import os
import time
from threading import Thread, get_native_id

# 在子线程中同样会执行
print(__name__)

def speak():
    for i in range(0, 10):
        print(f'speak pid:{os.getpid()}, tid: {get_native_id()}')
        time.sleep(1)

def study():
    for i in range(0, 10):
        print(f'study pid:{os.getpid()}, tid: {get_native_id()}')
        time.sleep(1)


# 多线程必须在main方法中运行，因为子线程在执行时，同样会执行当前模块，如果没有main方法，创建子线程的代码会无限执行，导致异常
p1 = Thread(target=speak)
p2 = Thread(target=study)

# 获取线程名字
print(p1.name)
print(p2.name)

p1.start()
p2.start()