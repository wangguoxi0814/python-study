# 闭包
# 闭包组成：
# 1. 内层函数+被内层函数引用的外层变量
# 表现：__closure__（一个包含闭包单元（cell）的Tuple）

# 闭包产生条件：
# 1. 必须有内嵌函数，且内嵌函数必须使用外层函数变量

# 闭包生命周期和内层函数一致

# 闭包优点：
# 1. 装饰器的基础
# 2. 可以记住状态，不用写类，不用全局变量，就可实现轻量级的状态保存，每次调用都能够从上一个状态开始
# 3. 轻量级数据隐藏，变量外部不可见，仅内层函数可使用，防篡改
# 4. 固定配置，得到定制化函数(见beauty示例)

# 闭包缺点：
# 1. 如果引用大对象，长期不释放，增加内存占用
# 2. 它的固定配置，得到定制化函数往往不是最佳实践，类和实例方法实现会更加清晰


# 闭包组成
def test():
    num = 100
    print(f'num hex id: {hex(id(num))}')

    def inner():
        nonlocal num
        num += 1
        print(f'num: {num}')

    return inner

f = test()
# 闭包单元地址值和函数内部打印的地址值一致
print(f'closure: {f.__closure__}')
f()  # 101
f()  # 102
f()  # 103
# 之所以会累加，是因为每次内层函数调用，都是在闭包单元所记录的值上操作
# 这里会变化，因为int是不可变类型，函数内部打印的num是100的地址值，没+1，都会创建一个新的对象，到这里闭包单元记录的是103的地址值
print(f'closure: {f.__closure__}')
# 验证闭包单元记录的内容就是num, 函数内部打印的内存地址和closure记录的内存地址一致
print(f'闭包单元值：{f.__closure__[0].cell_contents}')


# beauty示例 : 文字美化
def beauty(char, n):
    def wrap_test(text):
        print(str(char * n), text, str(char * n), sep='')
    return wrap_test

b = beauty('*', 2)
b("Hello World")