# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/8/26 16:02

# 多态不同的子类对象调用相同的父类方法，产生不同的执行结果
# 多态可以增加代码的灵活度
# 以继承和重写父类方法为前提
# 是调用方法的技巧，不会影响到类的内部设计

import abc


class Animals(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        pass


class People(Animals):
    def talk(self):
        print('People is talking')


class Cat(Animals):
    def talk(self):
        print('Cat is miaomiao')


class Dog(Animals):
    def talk(self):
        print('Dog is wangwang')


cat1 = Cat()
dog1 = Dog()
peo1 = People()
# peo、dog、pig都是动物,只要是动物肯定有talk方法
# 于是我们可以不用考虑它们三者的具体是什么类型,而直接使用
peo1.talk()
dog1.talk()
peo1.talk()


# 定义一个统一的接口来访问
def func(obj):
    obj.talk()


func(cat1)


class Pig(Animals):  # 属于动物的另外一种形态：猪
    def talk(self):
        print('Pig is huohuo')


pig = Pig()


# 统一接口，对于使用者来说，自己的代码根本无需改动
def func(obj):
    obj.talk()


func(pig)  # 甚至连调用方式都无需改变，就能调用出pig的talk功能
