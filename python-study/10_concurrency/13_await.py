# await
# 只有当await后面跟着IO任务时，会把当前任务挂起，会把CPU控制权交给事件循环，完成CPU的切换，最大化CPU利用率
# await只能在async方法中使用，后面只能接可等待对象
# Common await obj:
#          1. Coroutine
#          2. Future
#          3. Task
import asyncio

async def work():
    print('==work start')
    print('==work running...')
    # 模拟IO操作
    await asyncio.sleep(2)
    print('==work end')
    return "work result"

async def main():
    print('main start')
    print('main running...')
    res = await work()
    print(f'main get result: <{res}>')
    print('main end')
    return "main result"

res = asyncio.run(main())
print(res)
