# 验证协程的异步
# asyncio.create_task(work())
#   1. 把协程对象包装为事件循环任务
#   2. 把任务注册到事件循环

import asyncio
import time

async def work(n):
    print(f'==work{n} start')
    print(f'==work{n} running...')
    # 模拟IO操作，切换CPU
    await asyncio.sleep(2)
    print(f'==work{n} end')
    return f"work{n} result"

async def main_sync():
    start = time.time()
    res1 = await work(1)
    print(res1)
    res2 = await work(2)
    print(res2)
    res3 = await work(3)
    print(res3)
    print(f'同步耗时{time.time() - start}秒')

async def main_async():
    start = time.time()
    task1 =  asyncio.create_task(work(1))
    task2 =  asyncio.create_task(work(2))
    task3 =  asyncio.create_task(work(2))
    # 阻塞等待task1结果
    res1 = await task1
    print(res1)
    res1 = await task2
    print(res1)
    res3 = await task3
    print(res3)
    print(f'异步耗时{time.time() - start}秒')

async def main_async_pro():
    """
    异步优化，适配批量创建多个协程任务
    :return:
    """
    start = time.time()
    res_list = await asyncio.gather(*(work(i) for i in range(3)))
    print(res_list)
    print(f'异步耗时{time.time() - start}秒')


if __name__ == '__main__':
    # 同步
    # asyncio.run(main_sync())
    # 异步
    # asyncio.run(main_async())
    # 异步2
    asyncio.run(main_async_pro())