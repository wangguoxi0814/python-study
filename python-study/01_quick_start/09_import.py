# import导入模块，用于导入其他文件中的代码
# 简单来说，当我们要用别人写的代码，就需要通过import导入才能使用
# import导入取决于sys.path路径
# sys.path的结构是
## 1. 当前工作目录（cd到的目录）
## 2. 执行的文件所在目录
## 3. 标准库
## 4. ... 其他
## 当你写from orm.utils import utils时，
## 就会依次按照sys.path的路径去加载（{sys.path}/orm/utils）,如果当找不到模块时，要着重分析下sys.path和包名

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