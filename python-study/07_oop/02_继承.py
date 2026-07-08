# 类的继承(多继承)
# 可以继承父类的实例、静态、类方法
# 可以继承类属性，实例属性
# 不会继承__私有方法
# Python可以多继承,多继承时，如果子类不重写__init__，在实例化时调用最左边
# Python通过MRO解决菱形继承问题，见下一节


class Person:

    planet = "地球"
    max_age = 130

    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def speak(self):
        print(f'{self.name}正在说话中。。。')

    # 类方法, 实例工厂
    @classmethod
    def create(cls, name, age, grade):
        return cls(name, age, grade)

    @staticmethod
    def mask_idcard(idcard):
        return idcard[:6] + "*******" + idcard[-4:]


class Student(Person):

    def __init__(self, name, age, grade):
        Person.__init__(self, name, age)
        self.grade = grade

    def go_school(self):
        print(f'{self.name}上学，努力学习，成为{self.grade}年级第一')


print(f'Student dict: {Student.__dict__}')
print(f'Student extend planet: {Student.planet}')
print(f'Student extend max_age: {Student.max_age}')

s1 = Student("Peter", 25, '硕士三')
print(f's1:{s1.__dict__}')
print(f's1 type: {type(s1)}')
s1.speak()

student_mask = Student.mask_idcard("42212132121321321")
print(f'student_mask:{student_mask}')

s2 = Student.create("Kevi", 22, '大学四')
print(f's2 dict: {s2.__dict__}')
print(f's2 type: {type(s2)}')

class ClassCommon:

    def __init__(self, school):
        self.school = school

class Pupil(Student, ClassCommon):
    pass


pupil1 = Pupil('Peter', 12, '小学6')
print(pupil1.__dict__)
print(Pupil.__mro__)