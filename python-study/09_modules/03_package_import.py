# 包导入
# 一个目录就是一个包，一个包可以包含多个模块，并且有一个__init__.py文件，当然，python3.3+可以没有，但建议保留
# 在导入包时，会执行包的__init__.py文件
# 在__init__.py中，可以设置一些包的初始化逻辑
# __init__.py中的__all__控制from package import * 时导入的内容

import agents
# 需要在__init__中import模块才能使用这种方式
agents.agent.chat()
#
# from agents import agent
# from agents import rag
#
# from agents.agent import chat
# from agents.rag import rag

# 引入内容取决于__init__中的__all__，但不会递归导入子包内容
from agents import *

agent.chat()

# 下面引入的实际是know_base包的__init__，所以如果需要在这里使用rag模块的内容，则需要在know_base包的__init__中导入模块
# know_base.rag.similar_query()

# from agents.know_base import *
# rag.similar_query()

