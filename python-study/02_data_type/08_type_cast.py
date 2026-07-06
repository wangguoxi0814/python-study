# 类型转换示例

# 1. 隐式类型转换
# float + int -> float
num_int = 1
num_flo = 2.3

print("num_int type is :", type(num_int))
print("num_flo type is :", type(num_flo))

num_new = num_int + num_flo
print('number_new type is :', type(num_new))

# 2. 显式类型转换
num_int2 = 1
val_str = "2"

# 这里会报错，先注释, TypeError: unsupported operand type(s) for +: 'int' and 'str' , 不支持int和str相加，这个时候需要进行显式类型转换
# val_new = num_int2 + val_str
# print('val_new type is :', type(val_new))

val1_new = num_int2 + int(val_str)
print('val1_new type is :', type(val1_new))
print('val1_new value is :', val1_new)

str_new = str(num_int2) + val_str
print('str_new type is :', type(str_new))
print('str_new value is :', str_new)

num1 = 1
str1 = "2"

flo_num = float(num1) + float(str1)
print('flo_num type is :', type(flo_num))
print('flo_num value is :', flo_num)

bool_num = bool(num1) and bool(str1)
print('bool(num1)', bool(num1))
print('bool(str1)', bool(str1))
print('bool_num type is :', type(bool_num))
print('bool_num value is :', bool_num)

num2 = 0
str2 = ""

bool_num2 = bool(num2)
bool_str2 = bool(str2)
print('bool_num2 type is :', type(bool_num2))
print('bool_num2 value is :', bool_num2)
print('bool_str2 type is:', type(bool_str2))
print('bool_str2 is:', type(bool_str2))