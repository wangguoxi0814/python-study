# 变量
# 变量是用来存储数据的，变量名是用来标识数据的，比如 val = 1,=号左边是变量名，右边是变量值
# 变量名必须以字母或下划线开头，不能以数字开头
# 变量名只能包含字母、数字和下划线
# 变量名不能包含空格
# 变量名不能包含特殊字符
# 变量名不能包含关键字
# 变量名不能包含空格
# 变量名不能包含特殊字符
# 变量名不能包含关键字
# 变量名不能包含空格
# 变量名不能包含特殊字符
# 变量名不能包含关键字
import keyword
print('Python所有关键字：', keyword.kwlist)

# 变量值类型: Number,String,bool,List,Tuple,Dictionary,Set
# 不可变：Number,String,Tuple
# 可变：List,Dictionary,Set
# 空值：None

# 变量声明
val = 1 
print('val:', val)

# 声明空置None
n = None
print('n:', n)

# 变量删除
# 变量删除的意义：
# 1. 在使用大数据量时，可以提前释放变量所占用的内存，腾出内存空间
# 2. 在明确变量不需要被使用后，del删除能够避免误使用


# del删除变量的引用，删除后，后续的代码不能再使用该变量
# 这里的val由于没有再被引用，会提前垃圾回收，释放变量所占用的内存
# del val # 注释掉，否则运行会报错
# print('val:', val)

# 删除后不会被垃圾回收的情况
# 这里a和b指向同一个对象，删除a后，b仍然可以访问该对象，因此不会被垃圾回收
a = 1
b = a
del a
print('b:', b)


# 同时给多个变量赋值
j,k,q = 1,2,3
print('j:', j)
print('k:', k)
print('q:', q)