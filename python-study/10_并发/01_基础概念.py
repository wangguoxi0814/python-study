# 并发与并行

# 同步与异步

# 进程与线程

# 进程与子进程
import os
# 当前python启动的pid
print(os.getpid())
# 当前python启动的parent pid， 也就是idea， idea进程也有父进程，可以通过如下命令查看
# wmic process get Name,ParentProcessId, ProcessId
print(os.getppid())