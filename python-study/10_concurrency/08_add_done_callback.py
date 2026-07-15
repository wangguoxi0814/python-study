# add_done_callback ： 任务完成回调方法 线程池进程池均适用
# 通过回调也可以实现as_completed按任务完成顺序获取返回值的效果
# 回调方法入参必须是Future
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

    result_list = []


    def finished(future):
        result_list.append(future.result())


    for i in range(1001, 1005):
        f = processExecutor.submit(task, i, 0)
        f.add_done_callback(finished)

        # wait=True阻塞主进程，并等待所有任务完成, 无法再提交任务
    processExecutor.shutdown(wait=True)
    # 这样能保证结果输出顺序，又不会和任务执行打印交叉在一起
    # print(result_list)
    print(*result_list)
    # RuntimeError: cannot schedule new futures after shutdown
    # processExecutor.submit(task, 1005, 0)
    print('主进程执行结束')
