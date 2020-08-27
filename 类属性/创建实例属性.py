# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/8/27 9:28


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

# 2.使用对象名+类属性创建实例属性
tool1.count = 99
print("tool1 count: %s" % tool1.count)
# print: 3
# 采用上方赋值语句是给实例对象添加的实例属性
print("Tool count: %s" % Tool.count)
# 不影响类属性值
