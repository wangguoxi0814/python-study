# bool类型(布尔类型)
# 布尔类型：只有True和False两个值,默认值为False
isBird = True
isFish = False
print('isBird:', isBird)
print('isFish:', isFish)

# 类型查看
print('type(isBird) = ', type(isBird))
# bool类型是int类型的子类
print('bool is int subclass: ', issubclass(bool, int))
print('bool is int instance:', isinstance(True, int))

# 运算
# 布尔类型可以进行与、或、非运算
# 与运算，只有两个都为True，结果才为True，否则为False
print('True and False = ', True and False)
# 或运算，只要有一个为True，结果就为True，否则为False
print('True or False = ', True or False)
# 非运算，True变为False，False变为True
print('not True = ', not True)
print('not False = ', not False)
# 算术运算, True可以被当作1，False可以被当作0
print('Ture == 1 : ', True == 1)
print('False == 0 : ', False == 0)
print('True + 1 = ', True + 1)
print('False + 1 = ', False + 1)
print('True + Flase = ', True + False)

