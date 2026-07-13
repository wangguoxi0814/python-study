# 文件操作常见方法

# 文件类型：纯文本文件，二进制文件
# 二进制文件读取不需要设定字符集

# open()打开文件
# 参数：
#   file: 第一个位置参数
#   mode: 第二个位置参数，模式，包括r\w\x\a\b\t\+
#      r: 默认，读取文件
#      w: 写入文件
#      x: 排他性创建，如果文件已存在，则创建失败
#      a: 追加写入
#      b: 二进制模式
#      t: 文本模式（默认）
#      +: 打开用于更新
#   encoding: 第四个位置参数，字符集
# 返回值：
#   file: 文件对象，可迭代(迭代每次只读取一行，内存友好), 会耗尽

# 路径正斜杠或双反斜杠
# region
# f = open('../../docs/withdemo.txt', 'r', encoding='utf-8')
# # str.strip() 去除指定字符。默认去除首尾空格和/n
# for line in f:
#     print(line.strip())
# f.close()
# endregion

# read
# 1. 默认读取文件所有内容。如果文件体积过大，性能消耗严重，可以通过size参数指定每次读取的最大字符或字节数
# 2. read像游标，能继续读取，文件末尾读取''

# f1 = open('../../docs/withdemo.txt', 'r', encoding='utf-8')
# t1 = f1.read(2)
# t2 = f1.read(3)
# t3 = f1.read(4)
# print(f'{t1}, {t2}, {t3}')
# f1.close()

# readline() 按行读取，“游标读取”
# 参数：limit: 默认读取整行，limit指定每次读取最大字符或字节数
# f2 = open('../../docs/withdemo.txt', 'r', encoding='utf-8')
# # t1 = f2.readline()
# # t2 = f2.readline()
# t1 = f2.readline(2)
# t2 = f2.readline(2)
# print(t1)
# print(t2)

# readlines() 默认读取文件所有行
# 参数: hint: ，hint可以限制读取字符或字节上限
# 逻辑：
#   1、首先会读取整行，如果字符数>hint，则停止读取；如果字符串<=hint,继续读取
# 返回值：list列表，元素为每一行内容
f3 = open('../../docs/withdemo.txt', 'r', encoding='utf-8')
# t3 = f3.readlines()
t3 = f3.readlines(10)
print(t3)
