# 协程
# 一种微线程，用户态的上下文管理，性能开销小

# async修饰的方法就是一个协程方法，返回一个协程对象
# 调用协程方法不会执行方法,需要通过asyncio.run(work())执行
# run做的事：
#      1. 创建一个事件循环
#      2. 将收到的携程对象，包装成一个task，交给事件循环
#      3. 启动事件循环
#      4. 阻塞当前线程，知道任务结束，返回结果

import asyncio

async def work():
    print('haha1')
    print('haha2')
    print('haha3')
    return "meili"

result = asyncio.run(work())
print(result)