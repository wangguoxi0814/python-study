# 包导入
# 在导入包时，会执行包的__init__.py文件
# 在__init__.py中，可以设置一些包的初始化逻辑
# 在__init__.py中，
# __init__.py中的__all__导出可以导出包、模块、函数、变量

# import agents
# # 需要在__init__中import模块才能使用这种方式
# agents.agent.chat()
#
# from agents import agent
# from agents import rag
#
# from agents.agent import chat
# from agents.rag import rag

# 引入内容取决于__init__中的__all__，但不会递归导入子包内容
from agents import *

agent.chat()
# 这里引入的实际是know_base包的__init__，所以如果需要在这里使用rag模块的内容，则需要在know_base包的__init__中导入模块
# know_base.rag.similar_query()

from agents.know_base import *
rag.similar_query()

