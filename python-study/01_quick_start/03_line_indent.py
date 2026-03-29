# 行缩进，用于控制代码的结构和逻辑，但不会被Python解释器执行

# 缩进是Python中非常重要的概念，用于控制代码的结构和逻辑

# 正确示例
if True:
    print("True")
else:
    print("False")


# 错误示例
"""
运行报错信息：
IndentationError: unindent does not match any outer indentation level 
意思为：缩进不匹配任何外层缩进级别
说明：if语句没有正确缩进，同一个代码块内，所有代码行必须保持相同的缩进级别，否则会报错

"""
# if True:
#     print("One")
#   print("Two")
# else:
#     print("False")
