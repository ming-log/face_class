# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/8/27 9:14

# 类属性就是给类对象中定义的属性
# 通常用来记录与这个类相关的特征
# 类属性不会用于记录具体对象的特征

# 类属性，注意与类对象的属性区分开来
# 类属性是所有实例化后的对象的公有属性，用来记录类自身的变化


class Tool:

    # 使用赋值语句定义类属性，记录所有工具的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


# 1.创建工具对象
tool1 = Tool("镰刀")
tool2 = Tool("锄头")
tool3 = Tool("斧子")

tool1.count   # 可以利用实例化后的对象调用类属性
Tool.count    # 也可以直接利用类对象进行调用
