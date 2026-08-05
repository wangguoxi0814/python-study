# TODO List

## 20260805星期三深圳
- [ ] 在[03_package_import.py](./09_modules/03_package_import.py)中导入agents模块是，如果在agents的`__init__`中有`from know_base import rag`就会报`ModuleNotFoundError: No module named 'know_base'`，结合[09_import.py](./01_quick_start/09_import.py)中说明的导入模块路径加载梳理一下，目前报错应该是会从顶层模块中加载，但不应该优先从当前文件加载吗？