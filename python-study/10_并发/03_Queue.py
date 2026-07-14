# Queue
# 特点：FIFO；阻塞；跨进程共享
# Common API:
# 1. put():         放入, 如果已满，等待
#                         block:   决定是否阻塞，如果已满，直接异常
#                         timeout: 指定等待时间，等待时间过，如果还是已满，异常
# 2. get():         取出，如果已空，等待
#                         block:   决定是否阻塞，如果已满，直接异常
#                         timeout: 指定等待时间，等待时间过，如果还是已满，异常
# 3. empty():       判断是否为空
# 4. full():        判断是否已满
# 5. put_nowait():  放入且不等待，如果已满，直接异常
# 6. get_nowait():  放入且不等待，如果已满，直接异常
import time
# 多进程共享Queue
from multiprocessing import Queue, Process
import random

def consume(queue: Queue):
    for i in range(20):
        val = queue.get()
        print(f'成功消费：{val}')


def produce(queue: Queue):
    for i in range(20):
        product = random.randint(0, 100)
        s = f'产品，型号-{product}'
        queue.put(s)
        print(f'成功生产 {s}')
        time.sleep(1)


if __name__ == '__main__':
    q = Queue()
    consumer = Process(target=consume, name='consumer 1', args=(q,))
    producer = Process(target=produce, name='producer 1', args=(q,))

    consumer.start()
    producer.start()