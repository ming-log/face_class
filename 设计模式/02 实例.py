# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/8/27 14:22

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
    # 记录第一个被创建对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.instance


# 创建多个对象
player = MusicPlayer()
print(player)

player1 = MusicPlayer()
print(player1)

print("%x" % id(MusicPlayer))

# 只执行一次初始化工作
# 在每次使用类名()创建对象时，python的解释器都会自动调用两个方法：
# * __new__:分配空间
# * __init__:对象初始化
# 上方对__new__方法改造后，每次都会得到第一次被创建对象的引用
# 但是:初始化方法还会被再次调用


# 需求
# 让初始化动作只被执行一次

# 解决办法
# 1.定义一个类属性 init_flag 标记是否执行过初始化动作，初始值为False
# 2.在__init__方法中，判断init_flag，如果为False就执行初始化动作
# 3.然后将init_flag 设置为True
# 4.这样，再次自动调用__init__方法时，初始化动作就不会被再次执行了


class MusicPlayer:
    # 标记是否执行过初始化动作
    init_flag = False

    # 记录第一个被创建对象的引用
    instance = None

    def __init__(self):
        if not MusicPlayer.init_flag:
            print('初始化播放器')
            MusicPlayer.init_flag = True

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.instance


player = MusicPlayer()
print(player)

player1 = MusicPlayer()
print(player1)
