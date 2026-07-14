# 多进程
# 多进程必须在main方法中运行，因为子进程在执行时，同样会执行当前模块，如果没有main方法，创建子进程的代码会无限执行，导致异常
#  猜想：进程之间内存不共享应该就是由这种机制保证的，同一个global变量在多个进程互不干扰
#  跨进程的数据只有通过Process传递的参数和队列

# Process参数:
#   group:                分组，默认为None，且只能为None，为了和threading.Thread做兼容
#   target:               执行函数
#   name:                 进程名称，不传由Python自动分配，比如：Process-1, Process-2. Process.name获取或者current_process().name
#   args:                 target函数位置参数入参，类型元组
#   kwargs:               target函数关键字参数入参，类型字典
#   daemon:               是否为守护进程，bool类型

# 进程锁
# 1. Lock： 不可重入锁， RLock: 可重入锁。 API相同：
#       a. lock.acquire()上锁、lock.release()释放锁
#       b. 最佳实践： with lock

# join()
# p.join()会让当前进程等待p进程执行完再执行，p.join(timeout)可以指定等待时间
# join只能操作已经start的进程

# terminate()
# p.terminate() 强制终止p进程，不会执行target方法的finally块；
# 同样也是异步执行，调用不代表立即终止进程，通过p.is_alive()查看时可能为True，需要配合p.join()才能获取真实进程状态

# 守护进程
# 1. 守护进程中不能再创建子进程
# 2. 守护进程在主进程执行完就销毁
#       示例： 主进程开辟了p1(守护进程)， p2(非守护线程)
#              1. 主进程执行完毕，进入销毁流程时，会先杀掉守护进程，再判断是否还有子进程存活，如果有，则会等待子进程执行完毕再销毁，也就是这个时候主进程和普通子进程还存活，但守护线程已经被杀死了
# 适用场景：后台监控、统计、采样任务等


import os
import time
from multiprocessing import Process, current_process

# 在子进程中同样会执行
print(__name__)

def speak():
    print(f'speak进程name: {current_process().name}')
    for i in range(0, 10):
        print(f'speak pid:{os.getpid()}, ppid: {os.getppid()}')
        time.sleep(1)

def study():
    for i in range(0, 10):
        print(f'study pid:{os.getpid()}, ppid: {os.getppid()}')
        time.sleep(1)


if __name__ == '__main__':

    # 多进程必须在main方法中运行，因为子进程在执行时，同样会执行当前模块，如果没有main方法，创建子进程的代码会无限执行，导致异常
    p1 = Process(target=speak)
    p2 = Process(target=study)

    # 获取进程名字
    print(p1.name)
    print(p2.name)

    p1.start()
    p2.start()