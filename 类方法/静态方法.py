# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/8/27 9:42

# 在开发时，如果需要在类中封装一个方法，这个方法:
# * 既不需要访问实例属性或者调用实例方法
# * 也不需要访问类属性或者调用类方法

# 这个时候，可以把这个方法封装成一个静态方法

# 语法如下:
# @staticmethod
# def 静态方法名():
#     pass

# 静态方法需要调用修饰器 @staticmethod 来标识，告诉解释器这是一个静态方法
# 通过类名，调用静态方法


class Dog:
    @staticmethod
    def run():
        print("小狗要跑")


# 通过类名，调用静态对象 - 不需要创建对象
Dog.run()
