# import导入模块，用于导入其他文件中的代码
# 简单来说，当我们要用别人写的代码，就需要通过import导入才能使用

# 导入python标准库中的sys模块
import sys
# 打印python文件搜索的路径
print("sys.path:", sys.path)

# 只导入模块的某个函数
from random import randint
print("生成随机数1：", randint(1, 100))

# 为导入模块起别名
# 起别名作用：
# 1. 简化模块名，尤其对于一些模块名很长的模块，能大大降低代码量,提高可读性
# 2. 解决冲突：当从不同模块导入的函数名相同时，可以起别名避免冲突
from os import path as p
from sys import path as s
print('os.path:', p)
print('sys.path:', s)