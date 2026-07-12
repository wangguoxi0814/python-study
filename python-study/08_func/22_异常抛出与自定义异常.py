# 异常抛出: raise
# 自定义异常，集成Exception或其子类，名字以Error结尾

class EmailFormatError(Exception):
    pass

# raise EmailFormatError('邮箱格式错误!')

# 自定义异常，加固定前缀
class IdcardError(Exception):

    def __init__(self, msg):
        super().__init__('【自定义异常】' + msg)

raise IdcardError('身份证识别异常!')