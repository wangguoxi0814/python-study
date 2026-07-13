# yield生成器推导式
nums = [1, 2, 3, 4]
y = (x * 10 for x in nums)
# y此时就是一个生成器
for i in y:
    print(i)

print('-' * 40)

y1 = (x * 10 for x in nums if x % 2 == 0)
for i1 in y1:
    print(i1)