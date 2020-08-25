# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author: Ming Luo
# time: 2020/8/25 11:30


class Animal:
    def __init__(self):
        pass

    def eat(self):
        print("吃饱了")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


wangcai = Animal()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
print("-" * 100)


class Dog(Animal):
    # 改写父类的方法构成新类,但是不影响父类
    def run(self):
        print("哒哒哒")

    def dark(self):
        print("汪汪汪")


dog = Dog()
dog.eat()
dog.drink()
dog.run()
dog.sleep()
dog.dark()
print("-"*100)


class Cat(Animal):
    def catch(self):
        print("catch")


cat = Cat()
cat.eat()
cat.run()
cat.drink()
cat.sleep()
cat.catch()
print("-"*100)


# # 继承的传递性
# class XiaoTianQuan(Dog):
#     def fly(self):
# #         print("飞")
#
#
# xiaotianquan = XiaoTianQuan()
# xiaotianquan.eat()
# xiaotianquan.drink()
# xiaotianquan.run()
# xiaotianquan.sleep()
# xiaotianquan.dark()
# xiaotianquan.fly()
# print('-'*100)


# 继承的传递性
class XiaoTianQuan(Dog):
    def fly(self):
        print("飞")

    def dark(self):
        # 1. 针对子类特有的需求，编写代码
        print("神一样的叫唤...")
        # 2. 使用super().调用原本在父类中封装的方法
        # 指调用XiaoTianQuan这个类的父类的run()方法
        super(XiaoTianQuan, self).run()

        # 父类名.方法(self)
        # Dog.dark(self)
        # 注意：如果使用子类调用方法，会出现递归调用 - 死循环！
        # XiaoTianQuan.dark(self)
        # 3. 增加其他子类的代码
        print("#$%^&%$#$%^&*")

xiaotianquan = XiaoTianQuan()
xiaotianquan.dark()



