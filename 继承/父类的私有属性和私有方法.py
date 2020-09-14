# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/8/25 14:32

# 1. 子类对象不能再自己的方法内部，直接访问父类的私有属性或私有方法
# 2. 子类对象可以通过父类的公有方法间接访问到私有属性或私有方法
# 私有属性、方法 是对象的隐私，不对外公开，外界以及子类都不能直接访问
# 私有属性、方法 通常用于做一些内部的事情


class A:
    def __init__(self):
        self.num1 = 1
        self.__num2 = 2
        self._num3 = 3

    def test1(self):
        self.__test2()
        print("test 1 : %d %d" % (self.num1, self.__num2))

    def __test2(self):
        print("私有方法 test 2: %d %d" % (self.num1, self.__num2))


class B(A):
    def demo(self):
        print(self._num3)
        print("class B")


b = B()
# 在外界不能直接访问私有属性和私有方法
b._num3
b.__num2
b.__test2()

b._A__test2()
print(b._A__num2)
# 但是可以通过父类的公有方法间接访问父类的私有属性和私有方法
b.test1()
