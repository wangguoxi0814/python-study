# Pipe 管道
# 特点：支持双工，单工
# 参数：
#    duplex: bool, 是否双工， 默认True
from multiprocessing import Pipe
# con1和con2可读写
# con1, con2 = Pipe()
# con1.send('ja')
# print(con2.recv())

# con1只可读，con2只可写
con1, con2 = Pipe(duplex=False)
# con2.send('ja')
# print(con1.recv())

