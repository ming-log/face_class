# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/8/26 15:36
#
# Python中针对类提供了一个内置属性__mro__可以查看方法搜索路径
# MROs method resolution order, 主要用于在多继承时判断方法、属性的调用路径


class A:
    def test(self):
        print("A test")

    def demo(self):
        print("A demo")


class B:
    def test(self):
        print("B test")

    def demo(self):
        print("B demo")


class C(A, B):
    pass


c = C()
c.test()
c.demo()


# 安装元组的顺序按照MRO从左到右顺序查找
# 如果找到就直接执行，不再搜索
# 如果在最后一个基类还没有找到方法就会报错
print(C.__mro__)
# object 是 Python为所有对象提供的基类，提供有一些内置的属性和方法，可以使用dir函数查看
