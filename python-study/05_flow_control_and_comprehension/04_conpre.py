# 推导式，可以从一个数据序列构建另外一个新数据序列的结构体


print("1. list推导式")
list = [i for i in range(10)]
print(type(list))
print(list)

list2 = [i for i in list if i % 2 == 0]
print(list2)

print("2. dict推导式")
new_dict = {i: i*2 for i in range(10)}
print(type(new_dict))
print(new_dict)

 
listdemo = ['Google', 'Tecent', 'ByteDance']
new_dict2 = {key: len(key) for key in listdemo}
print(new_dict2)

