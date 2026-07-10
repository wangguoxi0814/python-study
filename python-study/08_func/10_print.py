# print 函数详解
# print(data, sep='', end= '', flush='', file='')
# sep: 分隔符，一次性打印多个时的分隔符
# end: 结束符。默认为换行符
# flush: 是否立即刷新。bool类型参数
# file: 所打印文件
import time

# sep & file
with open('print_output.txt', 'w',  encoding="utf-8") as f:
    print('Hello', 'Python', 'I', 'Give', 'Up', 'Java', sep=' ', file=f)


# end不做展示

# flush
# 这里在IDEA中会延迟打印每个dot，但是在cmd中会把每个结果缓存起来，最后一次性打印出来，失去延迟效果,就可以通过flush实时刷新到控制台，实现延迟
# import time
# print('加载中', end='', flush=True)
# for i in range(5):
#     print('.', end='', flush=True)
#     time.sleep(1)
# print('加载完成!')

# 进度条
# \r是回车符，把光标重置到行首，但不换行
# \n换行符
for i in range(1, 101):
    print(f'\r已加载:{i}%', end='')
    time.sleep(0.01)


