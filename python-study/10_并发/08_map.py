# map方法
# 执行时提交任务执行，但结果是惰性生成器，遍历时才会获取，按任务提交顺序获取
# 入参：
#   task:        任务
#   *iterables:  任务参数
#   timeout:     取结果等待超时时间
#   chunksize:   默认为1，数据块大小，将任务按chunksize分为若干个chunk，一个chunk为一个批，交给一个进程串行执行，适合数量较多的小任务
# 返回值：
#  返回一个生成器

import time
from concurrent.futures import ProcessPoolExecutor
import os


def task(task_id, task_state):
    print(f'执行任务{task_id}, {task_state}, pid: {os.getpid()}')
    if task_id % 2 == 0:
        time.sleep(3)
    else:
        time.sleep(1)
    return f'{task_id}执行完成'

def process_chunk(chunk):
    # 在子进程里串行执行多个 task
    return [task(*args) for args in chunk]

if __name__ == '__main__':

    print('主进程执行开始')
    processExecutor = ProcessPoolExecutor(3)

    # 多个任务批量交给一个进程，实际上就是批量封装任务，作为一个任务函数交给进程
    #  map根据chunksize分数据块后，交给进程执行也是同样逻辑

    # chunk = list(zip([1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0]))
    # c = process_chunk
    # print(c)
    # fut = processExecutor.submit(process_chunk, chunk)
    # print(fut.result())

    f = processExecutor.map(task, [1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0])
    # f = processExecutor.map(task, [1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], chunksize= 3)
    # print(f)
    # for i in f:
    #     print(i)
    print('主进程执行结束')
