# 集成Process类，创建进程
from multiprocessing import Process

class StudyProcess(Process):

    def __init__(self, **kwargs):
        # Process参数传入
        super().__init__(**kwargs)

    def run(self):
        print('进程任务执行')

if __name__ == '__main__':
    p1 = StudyProcess()
    p1.start()