# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/8/27 9:21

# 在python中属性的获取存在一个向上查找机制


class Tool:

    # 使用赋值语句定义类属性，记录所有工具的数量
    count = 0

    def __init__(self, name):
        self.name = name
        self.count = 100
        # 让类属性的值+1
        Tool.count += 1


# 1.创建工具对象
tool1 = Tool("镰刀")
tool2 = Tool("锄头")
tool3 = Tool("斧子")

tool1.count
# 当对象自身有相同的属性时，会优先调用自身的属性，
# 只有当对象自身没有调用的属性时才会调用类的对象
