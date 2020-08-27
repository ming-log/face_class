# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author: Ming Luo
# time: 2020/8/27 13:58

# 设计模式
# * 设计模式是前人工作的总结和提炼，通常，被人们广泛流传的设计模式都是针对某一特定问题的成熟解决方案
# * 使用设计模式是为了可重用代码，让代码更容易被他人理解、保证代码可靠性

# 单例设计模式
# * 目的 -- 让类创建的对象，在系统中只有唯一的一个实例
# * 每一次执行 类名() 返回的对象，内存地址是相同的

# 单例设计模式应用场景
# * 音乐播放 对象
# * 回收站 对象
# * 打印机 对象
# * ...

# __new__: 1.为对象分配初始空间   2.返回对象的引用
# python 解释器获得对象的引用后，将引用作为第一个参数，传递给__init__方法
# 重写 __new__ 方法的代码非常固定！
# 重写__new__方法一定要return super().__new__(cls)
# 否则python 解释器得不到分配了空间的对象引用，就不会调用对象的初始化方法
# 注意：__new__是一个静态方法，在调用时需要主动传递cls参数


class MusicPlayer:
    def __init__(self):
        print("播放器初始化")

    def __new__(cls, *args, **kwargs):
        # 1.创建对象时,new方法会被自动调用
        print("创建对象，分配空间")

        # 2.为对象分配空间,并返回
        return super().__new__(cls)


player = MusicPlayer()
print(player)

player1 = MusicPlayer()
print(player1)
