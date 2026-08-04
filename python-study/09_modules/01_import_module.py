# 模块导入5种方式
# 一个.py文件就是一个模块
# __all__和__name__
# __all__:     一个字符串元组，指定模块可以被外部模块导入的内容
# __name__:    如果外部导入模块，该值为模块名；如果做为主模块运行，该模块是__main__

# 第一种方式, 使用需要使用模块名去发起调用，且会导入模块所有内容，过于冗余
import modules.order
import modules.pay

# 第二种方式,起别名,但是会导入模块所有内容，通过别名发起调用
import modules.order as order
import modules.pay as pay

# 第三种方式, 按需导入,如果多个模块中如果存在同名的，会有冲突，可通过别名绕过
# 如果冲突，后引入的会覆盖前引入的
from modules.order import create_order, cancel_order
# from modules.pay import create_order
# 如果模块__all__中不包含所导出内容，导出会被警告
from modules.pay import create_order as pay_co

create_order()
pay_co()

# 第四种方式， *导入所有，官方不推荐，会导致引入混乱和冲突
from modules.order import *

