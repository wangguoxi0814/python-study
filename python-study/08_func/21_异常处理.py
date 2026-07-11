# 异常处理

# try:                    尝试捕获代码块
# except:                 捕获异常
# else:                   没有异常执行
# finally:                无论有没有异常都执行

# 常见异常：
# NameError:              找不到变量
# ZeroDivisionError:      除0异常
# KeyError:               获取字典不存在的key
# ValueError:             值错误
# TypeError:              类型错误
# IndexError:             索引越界
# Exception:              大多数可捕获异常的父类

# ZeroDivisionError
# a = 10
# b = 0
# print(f'{a / b}')

# TypeError
# print('*' * '*')


l = [1, 2, 3]
# ValueError
# l.index(99)
# IndexError
# k = l[4]


try:
    a = 1 / 0
except Exception as e:
    print(f'e: {e}')
    print(f'e.args: {e.args}')
    print(f'异常文件: {e.__traceback__.tb_frame.f_code.co_filename}')
    print(f'异常行数: {e.__traceback__.tb_lineno}')
    import traceback
    print(f'format_exc: {traceback.format_exc()}')
else:
    print('success')
finally:
    print('close resource')
