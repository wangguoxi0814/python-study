# 多进程
# Process参数:
#   group:                分组，默认为None，且只能为None，为了和threading.Thread做兼容
#   target:               执行函数
#   name:                 进程名称，不传由Python自动分配，比如：Process-1, Process-2. Process.name获取或者current_process().name
#   args:                 target函数位置参数入参，类型元组
#   kwargs:               target函数关键字参数入参，类型字典
#   daemon:               是否为守护进程，bool类型

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