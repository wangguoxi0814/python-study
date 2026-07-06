# 自定义迭代器，实现一个迭代器类，实现__iter__和__next__方法

class MyNumberItre: 
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a < 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

print("==========1==========")
myClass = MyNumberItre()
# 只有for循环和iter()会包装的迭代器会调用__iter__方法,直接调用next()，不会执行__iter__方法，因此会报AttributeError: 'MyNumberItre' object has no attribute 'a'
# print(next(myClass))
for i in myClass:
    print(i, end=' ')
print()



print("==========2==========")
myClass2 = iter(myClass)
print(next(myClass2))
print(next(myClass2))