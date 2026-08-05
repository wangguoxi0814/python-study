# 包导入
# __init__.py的作用：
# - 只有有__init__.py的目录才是包，否则只是一个包（普通文件夹），当然，python3.3+可以没有，但建议保留
# - 导入包时会执行包的__init__.py文件，可以做一些初始化操作
# - __init__.py中的__all__控制from package import * 时导入的内容（__all__只控制import *导入的内容）
#       - __all__缺省时，import * 导入所有非_开头的模块
# - __init__.py中可以导入其他的模块，外部使用这个包时，可以import __init__中引入的所有模块

# 一个目录就是一个包，一个包可以包含多个模块，并且有一个__init__.py文件

# agents即便没有__init__.py也可以当作模块导入
import agents
# 需要在__init__中import agent 模块才能通过包名调用模块
# agents.agent.chat()
# print(agents)

#
# from agents import agent
# print(agent)
# from agents import rag
# print(rag)
# from agents import know_base
# print(know_base)

#
# from agents.agent import chat
# from agents.rag import rag

# 引入内容取决于__init__中的__all__，但不会递归导入子包内容
# from agents import *
# agent.chat()
# 下面引入的实际是know_base包的__init__，所以如果需要在这里使用rag模块的内容，则需要在know_base包的__init__中导入模块
# know_base.rag.similar_query()

# 这里__all__缺省，会导入所有非_开头的内容
from agents.know_base import *
rag.similar_query()

