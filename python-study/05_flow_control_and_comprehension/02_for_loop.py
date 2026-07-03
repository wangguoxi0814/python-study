# 循环语句

# for循环
# 打印10次，从0-9
for i in range(10):
    print(i, end=' ')
print("===========1=======")

for i in range(1, 10):
    print(i, end=' ')
else:
    print("for正常循环结束")
print("==========2==========")

# break 跳出循环，不会进入else
for i in range(1, 10):
    print(i, end=' ')
    if (i == 5):
        break
else:
    print("for正常循环结束")
print("=========3===========")

# continue 跳过当前循环，继续下一次循环，会进入else
for i in range(1, 10):
    if (i == 5):
        continue
    print(i, end=' ')
else:
    print("for正常循环结束")
print("==========4==========")

# 遍历列表同时获取值和索引
l = [1,2,3]
for i, v in enumerate[int](l):
    print(f'索引{i}的值是{v}')