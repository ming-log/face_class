# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/8/25 10:28


class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("%s 没有子弹了..." % self.model)
            return
        self.bullet_count -= 1
        print("%s 突突突... %d" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self, num):
        if self.gun is None:
            print("%s 士兵没有枪" % self.name)
            return

        print("冲啊... %s" % self.name)

        self.gun.add_bullet(num)
        while num >= 0:
            self.gun.shoot()
            num -= 1


ak47 = Gun("AK47")              # 创建AK47枪对象
xu_san_duo = Soldier("许三多")  # 创建许三多军人对象
xu_san_duo.gun = ak47           # 把AK47枪给许三多军人
xu_san_duo.fire(50)               # 许三多装填50发子弹进行开火

# is 与 == 之间的区别
# is 判断的是两个变量间的内存地址是否一致
# == 判断的是两个变量间的值是否相等
# e.g.
# a = [1, 2, 3]
# print(id(a))
# b = [1, 2]
# print(id(b))
# b.append(3)
# print(id(b))
# print(a == b)
# print(a is b)
