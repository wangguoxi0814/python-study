# 文件或文件夹操作

import os
# 1.判断文件或路径是否存在
# res = os.path.exists('D:/demo')
# res1 = os.path.exists('D:/demo/a.txt')
# print(res)
# print(res1)

# 2.判断是文件还是目录
# 为空也会返回False
# print(os.path.isdir('D:/demo'))
# print(os.path.isfile('D:/demo/a.txt'))

# 3.创建单级目录，当文件已存在会报：FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: 'D:/demo/aa'
# 如果创建多级目录，会因为上级目录不存在，而报：FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'D:/demo/bb/haha'
# os.mkdir('D:/demo/aa')
# os.mkdir('D:/demo/bb/haha')

# 4. 创建多级目录, 如果目录已存在，会异常
# os.makedirs('D:/demo/bb/haha')
# os.makedirs('D:/demo/bb/haha')


# 5. 删除目录, 只会删除为空的目录,如果目录不存在，或者非空，会异常 OSError: [WinError 145] 目录不是空的。: 'D:/demo'
# os.rmdir('D:/demo/bb/haha')
# os.rmdir('D:/demo')

# 6. 递归删除空目录, 会先删除指定目录，再回到上一层级删除
# 不是递归删除指定文件夹下所有空目录
# os.removedirs('D:/demo/aa')
# os.removedirs('D:/demo/bb/cc')

# 7. 扫描指定目录内文件/目录,不会递归深入
# 返回值是一个迭代器，迭代项每个都是DirEntry，该对象有方法区分为文件还是目录
# result = os.scandir('D:/demo')
# print(result)
# for i in result:
#     # print(i)
#     print(f'{"目录" if i.is_dir() else "文件"}: {i.name}')

# 8. 深度遍历
#  返回一个生成器, 每个元素都是一个元组(当前目录path，['子目录名1'...], [文件1...])
# result = os.walk('D:/demo')
# print(result)
# for i in result:
#     print(i)

# 9. 强制删除所有文件和目录，即便非空---危险操作
import shutil
shutil.rmtree('D:/demo')

