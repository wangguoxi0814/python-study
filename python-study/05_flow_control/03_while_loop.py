# 循环语句
# python没有do...while循环
# while循环
x = 1
while x < 10:
    print('haha')
    x += 1

# while...else...
y = 1
while y < 10: 
    print(y, end=' ')
    y += 1
else: 
    print('while正常循环结束')

print("break 跳出循环，不会进入else")
# break 跳出循环，不会进入else
y = 1
while y < 10: 
    print(y, end=' ')
    if (y == 5):
        break
    y += 1
else: 
    print('while正常循环结束')