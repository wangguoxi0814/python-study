# 05_数字类型，用来表示数字。数字类型是数据类型的一个大类，另外还包括字符串、布尔类型
# 数字类型包括整数、浮点数、复数
# 整数：用来表示整数，如1,2,3,4,5,6,7,8,9,10
# 浮点数：用来表示小数，如1.2,3.4,5.6,7.8,9.0
# 复数：用来表示复数，如1+2j,3+4j,5+6j,7+8j,9+10j

# 整数类型：int
# python3中只有int一种整数类型，不再有python2的long类型
print('整数类型：int')
i = 1
print('i:', i)
k = -100
print('k:', k)

# 算术运算
# 加法
print('i + k = ', i + k)
# 减法
print('i - k = ', i - k)
# 乘法
print('i * k = ', i * k)
# 除法(返回浮点数float)
print('i / k = ', i / k)
x = 9
y = 3
num = x / y
print('x / y = ', num)
print('type(num) = ', type(num))
# 取整除(向下取整,得到整数int)
j = 7
k = 3
print('(1)j // k = ', j // k)
i = -7
num = i // k
print('(2)i // k = ', num)
print('type(num) = ', type(num))
# 取模(取余数)
a = 3
b = 7
print('a % b = ', a % b)
# 幂
m = 2
n = 3
print('m ** n = ', m ** n)


print('==============================')
print('浮点数类型：float')
# 浮点数类型：float
# 浮点类型标识小数，在python中没有double类型，只有float类型
f = 1.23
print('f:', f)
f2 = 1.23e3      # 1.23 * 10^3 科学计数法
print('f2:', f2)
f3 = 1.23e-3      # 1.23 * 10^-3 科学计数法
print('f3:', f3)
f4 = -1.23
print('f4:', f4)

print('==============================')
print('复数类型：complex')
# 复数类型：complex，支持加减乘除
# 格式： a + bj,其中a是实部，b是虚部，j是虚数单位, a和b都是浮点数float
c = 1.23j
print('c:', c)
c2 = 1.23e3j
print('c2:', c2)
c3 = 1.23e-3j
print('c3:', c3)
c4 = -1.23j
print('c4:', c4)
c5 = c + c2
print('c5:', c5)

# 使用complex函数创建复数 1 + 2j
c6 = complex(1, 2)
print('c6:', c6)

# 获取复数的实部和虚部
print('c6.real = ', c6.real)
print('c6.imag = ', c6.imag)
print('type(c6.real) = ', type(c6.real))
print('type(c6.imag) = ', type(c6.imag))