# as_completed 获取先完成任务的返回值  线程池进程池均适用
#           入参： Future序列
# 普通Future.result()是按任务提交顺序获取返回值
# 如果提交顺序A(10s) -> B(1s) -> C(2s)，通过Future获取返回值会被A卡住，即便B\C早已完成，而通过as_completed能先获取已完成任务的返回值
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
import os

def task(task_id, task_state):
    print(f'执行任务{task_id}, {task_state}, pid: {os.getpid()}')
    if task_id == 1001:
        time.sleep(5)
    elif task_id == 1002:
        time.sleep(2)
    else:
        time.sleep(0.5)
    return f'{task_id}执行完成'

if __name__ == '__main__':
    print('主进程执行开始')
    processExecutor = ProcessPoolExecutor(3)
    futures = [processExecutor.submit(task, i, 0) for i in range(1001, 1005)]

    result_list = []
    for f in as_completed(futures):
        result_list.append(f.result())

    # wait=True阻塞主进程，并等待所有任务完成, 无法再提交任务
    processExecutor.shutdown(wait=True)
    # 这样能保证结果输出顺序，又不会和任务执行打印交叉在一起
    # print(result_list)
    print(*result_list)
    # RuntimeError: cannot schedule new futures after shutdown
    # processExecutor.submit(task, 1005, 0)
    print('主进程执行结束')