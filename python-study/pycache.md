# **`__pycache__`**
   - `__pycache__` 是 Python 自动生成的字节码缓存目录，加速程序启动
   - 文件名格式示例：`main.cpython-311.pyc`（cpython-311 表示 Python 版本，不同python版本不能共用pycache文件）

### IDEA/PyCharm不显示__pycache__原因
    > 弄清楚原因即可，不建议打开pycache文件的展示.
    > pycharm忽略文件可以减少文件索引，提升pycharm性能和减少视觉“噪音”
   - IDEA/PyCharm 默认将其配置为「排除目录」（Excluded），自动隐藏
   - 如需显示：在Project试图中的右上角三个点展开 → Appearance → 勾选 "Excluded Files", 此时可能还是无法显示，进入到设置-Editor-File Types中，可以看到Ignored Files and Folders里面PyCharm会默认忽略pycache
   - 改了代码但行为没变时，手动清除 `__pycache__` 强制重新编译