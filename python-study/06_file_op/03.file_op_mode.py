# open()打开文件
# 参数：
#   file: 第一个位置参数
#   mode: 第二个位置参数，模式，包括r\w\x\a\b\t\+
#      主模式: 互斥
#           r: 默认，读取文件
#           w: 写入文件
#           x: 排他性创建，如果文件已存在，则创建失败
#           a: 追加写入
#      修饰符：不能单独使用，修饰主模式
#           b: 二进制模式
#           t: 文本模式（默认）
#           +: 打开用于更新
#   encoding: 第四个位置参数，字符集
# 返回值：
#   file: 文件对象，可迭代(迭代每次只读取一行，内存友好), 会耗尽

# seek(offset, whence)
#     offset: 偏移量(字节数，即便是纯文本文件，一个中文字符在UTF-8编码中通常占3个字节)
# print('中'.encode('utf-8'))
# print(len('中'.encode('utf-8')))
#     whence: 参考位置
#           0: 文件开头（默认）
#           1: 当前位置
#           2: 文件结尾

# flush()：将文件内容从缓冲区刷新到磁盘
# 缓冲区只有3种情况会刷新到磁盘：
#   1. 缓冲区满
#   2. 文件关闭时
#   3. 手动flush

# rw  主模式互斥：ValueError: must have exactly one of create/read/write/append mode
# with open('a.txt', 'rw', encoding="utf-8") as f:
#     f.write('Hello')

# wt+, 因为有了+,可读可写,可以随意修改内容
# with open('a.txt', 'wt+', encoding="utf-8") as f:
#     f.write('Hello')
#     # 读取不到，因为write后，指针到了文件末尾，可以通过seek重置指针位置
#     f.seek(0, 0)
#     r = f.read()
#     print(r)


# # rt+, 因为有了+,可读可写,可以随意修改内容
# with open('a.txt', 'rt+', encoding="utf-8") as f:
#     r = f.read()
#     # 读取完后指针到了文件末尾，写入时会追加内容
#     f.write('Hello')
#     print(r)


# xt+, 如果文件存在，会异常

#at+
# with open('a.txt', 'at+', encoding="utf-8") as f:
#     # at+本身就是追加内容，初始化时指针在文件末尾，无法读取到内容
#     r = f.read()
#     f.write('Hello')
#     print(r)

