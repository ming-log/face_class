# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author: Ming Luo
# time: 2020/8/24 13:15

# dir(): 查看对象的所有方法和属性
# __xxx__:对象内置方法和属性


class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)

    # __del__函数在对象结束时调用的函数
    # 一般在整个代码运行结束时，对象才会被回收，此时才会调用__del__函数
    # 当使用del关键字强制删除对象时，也会在del运行完毕后调用__del__函数
    def __del__(self):
        print("%s 去了" % self.name)


tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除一个对象
del tom
print("-"*50)
