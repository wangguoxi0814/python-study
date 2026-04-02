# python-study
python study

# 编辑器
- 编辑器选择：`PyCharm`、`Cursor`、`VsCode`
- `Cursor`/`VsCode`自动保存：点击左上角`File->Auto Save`
- `Cursor`/`VsCode`的`Code Runner`插件运行在终端配置：打开`File->Preferences->VsCode Settings`(快捷键`Ctrl+,`)，搜索`code-runner.runInTerminal`后，勾选`Whether to run code in intergrated Terminal`，否则插件默认运行后只展示输出，无法监听用户键盘输入
- `Cursor`/`VsCode`文件窗口多行显示：打开的文件很多时，上方的文件标签超出部分会无法直观看到，开发文件标签多行显示，能更直观的看到所有文件标签。打开`Settings`,搜索`workbench.editor.wrapTabs`后勾选
- `Cursor`/`VsCode`预览MD无法渲染任务列表问题，安装`MarkDown All in One`插件


# GitHub问题
- 克隆和推送方式建议使用SSH，比HTTPS更稳定（HTTPS可能会存在开了VPN也无法推送问题）
- SSH配置
    - 本地电脑生成秘钥对：`ssh-keygen -t ed25519 -C "你的邮箱"`
    - 复制`id_ed25519.pub`里的公钥，在GitHub的Settings-SSH and GPG keys中`New SSH key`，将复制的公钥填写到`key`栏目中
    - 使用SSH克隆`git clone git@github.com:wangguoxi0814/python-study.git`
    - 或者通过HTTPS克隆`git clone https://github.com/wangguoxi0814/python-study.git`后，再将秘钥配置好后，将本地的push和fetch的URL改为SSH连接，`git remote set-url origin git@github.com:wangguoxi0814/python-study.git`,在用`git remote -v`验证，显示SSH连接则表示成功

# 规范说明
1. 该项目旨在学习python，文件命名以数字开头表示学习顺序以引导学习，但实际开发中，文件命名应严格遵循PEP8规范，全小写和下划线分隔单词。  
- 正确示例：
    - `hello_python.py` 
    - `data_type_stu.py`   
- 错误示例：
    - `01_hello_python.py`

# 乱码问题
- Windos系统Cursor/VS Code点击Run Code输出中文乱码问题，文件编码字符集和输出解码字符集不一致，以文件编码为UTF-8为例
    - 确认自己的文件是否为UTF-8编码，编辑器右下方可以看到，如果不是，则需要将文件编码修改为`UTF-8`
    - 打开设置，搜索`Code-runner: Executor Map`，点击`Edit in settings.json`，增加如下内容：  
        ```json
        "code-runner.executorMap": {
            "python": "python -u -X utf8"
        }
        ```