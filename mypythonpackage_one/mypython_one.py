'''
包含一个学生类
一个函数
一个打印语句
'''


class Student():
    def __init__(self, name="娜娜", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("my name is {0},我{1}岁".format(self.name, self.age))


def sayHello():
    print("欢迎来到图灵学院！")


if __name__ == '__main__':
    print("我是模块one")
