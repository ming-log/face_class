# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/8/25 10:57
# 应用场景：
# 在实际开发中，对象的某些属性或方法可能只希望在对象的内部被使用，而不希望在外部被访问到
# 私有属性就是对象不希望公开的属性
# 私有方法就是对象不希望公开的方法
# 定义方式：
# 在定义属性或方法的时候，在属性名或者方法名前增加两个下划线，定义的就是私有属性或方法


class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiao_fang = Women("小芳")
# 私有属性，在外界不能够被直接访问
print(xiao_fang.__age)
# 但是引用对象内部的方法是可以访问的
xiao_fang.secret()
# 私有方法，同样在外界不能够被直接访问
xiao_fang.__secret()

# 伪私有属性和私有方法
# 在日常开发中，不要使用这种方式，访问对象的私有属性或私有方法
# python解释器在给属性、方法命名时，实际是对名称做了一些特殊处理，使得外界无法访问到
# 处理方式：在名称前面加上 _类名 => _类名__名称
# 即采用以下方式可以对对象的私有属性和私有方法进行访问
print(xiao_fang._Women__age)
xiao_fang._Women__secret()
