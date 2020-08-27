# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/8/27 9:31
# 类属性就是针对类对象定义的属性
# * 使用赋值语句在class关键字下方可以定义类属性
# * 类属性用于记录与这个类相关的特征

# 类方法就是针对类对象定义的方法
# * 在类方法内部可以直接访问类属性或者调用其他的类方法

# 基本语法
# @classmethod
# def 类方法名(cls):
#     pass

# 类方法需要用修饰器 @classmethod 来标识，告诉解释器这是一个类方法
# 类方法的第一个参数应该是cls
# * 由哪一个类调用的方法，方法内的cls就是哪一个类的引用
# * 这个参数和实例方法的第一个参数self类似
# * 提示使用其他名称也可以，不过习惯使用cls

# 在方法内部
# * 可以通过cls.访问类的属性
# * 也可以通过cls.调用其他的类方法


class Tool:

    # 使用赋值语句定义类属性，记录所有工具的数量
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % Tool.count)

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")

# 调用类方法
Tool.show_tool_count()

# 与类属性类似
# 在使用实例对象调用类方法的时候，同样遵循向上原则，如果实例自身有该方法
# 会优先调用自身的方法
