# enumerate() 同时返回元素和索引
# zip()  一一合并2个可迭代对象的元素，返回zip可迭代对象，可通过list()转为list，结果的长度为合并对象最小长度， 最终结果的元素为Tuple

l = ['Hello', 'Python', 'World']
for index, item in enumerate(l):
    print(f'{item}索引是:{index}')

# 合并2个list
names = ['Peter', 'Lucy', 'Mary']
scores = [90, 80, 89]
result = zip(names, scores)
print(f'{list(result)}')

# 两个不同可迭代对象也可以合并
menu = {'西红柿炒鸡蛋', '辣椒炒肉拌面', '白切鸡'}
prices = [23, 25, 45]
zr = zip(menu, prices)
print(f'{list(zr)}')

# 合并dict的key
menu_dict = {'凡人修仙传': 23, '斗破苍穹': 25, '不良人': 45}
prices_list = [23, 25, 45]
zr = zip(menu_dict, prices_list)
print(f'{list(zr)}')

# 长度不一致的合并, 最终长度为3，和合并对象最小长度一致
short_list = ['American', 'China', 'British']
latitude_list = [112, 80, 99, 45]
sl_zip = zip(short_list, latitude_list)
print(f'{list(sl_zip)}')