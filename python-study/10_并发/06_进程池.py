# 进程池
# Python里有2种进程池，分别是Pool和ProcessPoolExecutor
# Pool since python2.6          API : pool.close() pool.join()
# ProcessPoolExecutor since python3.2, 更符合现代软件工程设计
# API：
# ProcessPoolExecutor(nums) : nums指定进程池进程数
# 1. submit(task, *args)
#             返回Future，future.result()获取结果,会阻塞直至进程产生结果
# 2. shutdown(): 不再接受任务，等待任务执行完毕，销毁进程池
#              wait=True，阻塞主进程，等待所有子进程完成所有任务
import time
from concurrent.futures import ProcessPoolExecutor
import os

def task(task_id, task_state):
    print(f'执行任务{task_id}, {task_state}, pid: {os.getpid()}')
    time.sleep(1)
    return f'{task_id}执行完成'

if __name__ == '__main__':
    print('主进程执行开始')
    processExecutor = ProcessPoolExecutor(3)
    f1 = processExecutor.submit(task, 1001, 0)
    f2 = processExecutor.submit(task, 1002, 0)
    f3 = processExecutor.submit(task, 1003, 0)
    f4 = processExecutor.submit(task, 1004, 0)
    # Future获取结果会阻塞直至进程任务完成
    print(f1.result())
    print(f2.result())
    print(f3.result())
    print(f4.result())
    # 阻塞主进程，并等待所有任务完成, 无法再提交任务
    processExecutor.shutdown(wait=True)

    # RuntimeError: cannot schedule new futures after shutdown
    # processExecutor.submit(task, 1005, 0)
    print('主进程执行结束')