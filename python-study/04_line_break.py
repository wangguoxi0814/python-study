# 04_语句换行,用于将长语句分成多行
# python里通常一行写完一个语句，如果语句过长，可以换行写，但是换行处需要添加反斜杠\

# 示例1
item_one = 1
item_two = 2
item_three = 3
# 语句过长，换行书写
total = item_one + \
    item_two + \
    item_three

print("总数: " + str(total))

# 示例2
# 在[],{},()中，换行不用用反斜杠\
item_four = 4
item_five = 5
item_six = 6
item_seven = 7
item_eight = 8
item_nine = 9
item_ten = 10
# 不用反斜杠\，也可以换行
total = [item_one, item_two, item_three, item_four, item_five, 
item_six, item_seven, item_eight, item_nine, item_ten]
print("列表: " + str(total))

# 示例3
# 在三双引号中，换行不用用反斜杠\
# tips:这里三双引号给变量赋值，是作为字符串，而不是注释
total = """
这是一个多行字符串
可以包含多行内容
"""
print("多行字符串: " + total)

