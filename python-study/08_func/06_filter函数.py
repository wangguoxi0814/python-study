# filter函数
# filter(func, data) func为过滤逻辑，data为可迭代对象，如果func为None，默认过滤掉所有为False的数据
# 返回一个迭代器
# 延迟执行，只有在需要时，才会计算

l = [1, 0, "", "Hello", "Python"]
# 过滤掉数字
f = filter(lambda ele: isinstance(ele, str), l)
print(f'过滤后的原始数据：{l}')
print(f'过滤后的结果：{list(f)}')

# 默认过滤掉为False的数据
f1 = filter(None, l)
print(f'f1:{list(f1)}')

# 过滤掉数字和为False的数据
f2 = filter(lambda ele: isinstance(ele, str) and ele, l)
print(f'f2:{list(f2)}')