# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author: Ming Luo
# time: 2020/8/24 14:28


class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 去了" % self.name)

    # 必须返回一个字符串
    # 在Python中，使用print输出对象变量默认情况下，
    # 会输出这个变量引用的对象是由哪一个类创建的对象，以及在内存中的地址（16进制）
    # 如果在开发中，希望使用print输出对象变量时，能够打印自定义的内容
    # 就可以利用__str__这个内置方法了
    # 注意:__str__方法必须返回一个字符串
    def __str__(self):
        return "Tom 是猫"


tom = Cat("Tom")
print(tom)
