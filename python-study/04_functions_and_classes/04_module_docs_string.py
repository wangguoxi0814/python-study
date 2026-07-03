#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文档字符串
# 文档字符串是用来描述模块、类、函数、方法等内容的字符串，通常用于解释代码的作用、参数、返回值等
# 文档字符串使用三引号（''' 或 """）来定义，通常位于模块、类、函数、方法的第一个位置

# 获取方式：
# 1. 使用__doc__属性
# 2. 使用help()函数,会多输出函数所在的模块，函数声明
# 3. 使用inspect模块

# 模块文档字符位置
# 1. 如果有Shebang/编码声明，则放在.py第一行
# 2. 紧随其后的就是模块文档字符串
# 3. 然后才是import、常量、函数、类等代码

# 模块文档字符串示例

"""Utilities for parsing log files.

This module provides helpers to parse logs and compute statistics.
"""

from __future__ import annotations


# 读取模块docstring
print('===========================__doc__===========================')
print(__doc__)

print('===========================help()===========================')
print(help(__name__))

print('===========================inspect.getdoc()===========================')
import inspect
print(inspect.getdoc(__name__))

# 在模块外部则需要导入当前模块才能读取，同样通过__doc__属性或者help()函数获取
# 注意：因为导入模块可能会有副作用，外部查看docstring时，可以通过ast模块的get_docstring()函数获取
import ast
from pathlib import Path
path = Path(__file__)
tree = ast.parse(path.read_text(encoding='utf-8'))
print('===========================ast.get_docstring()===========================')
print(ast.get_docstring(tree))








