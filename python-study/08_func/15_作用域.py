# 四种作用域
# Built-in > Global > Enclosing > Local
# Built-in:     包含print、len、max这些，我们在任何地方都可以使用
# Global:       当前Python文件，在enclosing\local作用域使用这个变量时，需要关键字global
# Enclosing:    外层函数作用域（相对于嵌套函数来说）
# Local:        方法内部作用域, 在这个作用域使用Enclosing作用域变量并且修改时，需要关键字nonlocal(读取变量不需要)

# 问题：
# 1. global 指定的变量不存在会怎样？                        --> 报错：NameError: name 'b' is not defined
# 2. 方法多层嵌套unlocal使用的变量是最外层的，还是仅仅上一层？   --> 仅上一层，实质为就近原则,当上一层没有时，会再上一层

a = 100

def test():
    global a
    a = 200
    b = 1
    c = 20
    def inner1():
        nonlocal b
        # c = -1
        def inner2():
            nonlocal c
            c += 1
            print(f'inner2 print c: {c}')
        inner2()
        b += 1
        print(f'inner1 print b: {b}')
        print(f'inner1 print c: {c}')

    inner1()
    print(f'test print a: {a}')
    print(f'test print b: {b}')
    print(f'test print c: {c}')

test()
print(f'a: {a}')
