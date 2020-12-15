# class Cat:
#     """"模拟猫的类"""
#
#     def __init__(self, name, age):
#         """初始化猫的属性name,age"""
#         self.name = name
#         self.age = age
#
#     def sit_down(self):
#         """模拟猫的叫声"""
#         print(self.name + ' is howl "miao~"')
#
#     def roll_over(self):
#         print(self.name + " is rolling.")
#
#
# my_cat = Cat('Eric', 2)
# my_cat.sit_down()
# my_cat.roll_over()


# def square(num):
#     n = num * num
#     return n
#
#
# prompt = 'Please input a number: '
# a = input(prompt)
# b = square(int(a))
# print(str(a) + '的平方为' + str(b))


class Students:
    """创建一个学生成绩的类"""
    def __init__(self, name, init_math, init_english):
        """初始化学生的成绩"""
        self.name = name
        self.math = init_math
        self.english = init_english

    def set_math(self, new_grade):
        self.math = new_grade

    def set_english(self, new_grade):
        self.english = new_grade

    def print_grade(self):
        print(self.name + '的数学成绩为' + str(self.math) + ', 英语成绩为' + str(self.english))


Eric = Students('Eric', 98, 92)
Eric.set_math(95)
Eric.print_grade()
