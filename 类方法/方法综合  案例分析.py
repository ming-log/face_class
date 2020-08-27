# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/8/27 9:52
# 需求
# 1.设计一个Game类
# 2.属性:
#   * 定义一个类属性top_score 记录游戏的历史最高分
#   * 定义一个实例属性 player_name 记录当前游戏的玩家姓名
# 3.方法
#   * 静态方法 show_help显示游戏帮助信息
#   * 类方法 show_top_score 显示历史最高分
#   * 实例方法start_game 开始当前玩家的游戏
# 4.主程序步骤
#   * 查看帮助信息
#   * 查看历史最高分
#   * 创建游戏对象，开始游戏
import random


class Game:
    top_score = 0

    @staticmethod
    def show_help():
        print("帮助文档:******")

    @classmethod
    def show_top_score(cls):
        print("当前历史最高分为:%s" % Game.top_score)

    def __init__(self, player_name):
        self.player_name = player_name

    def start_game(self):
        print("玩家 %s 开始游戏" % self.player_name)
        score = random.randint(0, 100)
        print("玩家 %s 得分:%s" % (self.player_name, score))
        if score > Game.top_score:
            Game.top_score = score


Game.show_help()
Game.show_top_score()
game = Game("log")
game.start_game()

# 案例小结
# 1.案例方法 -- 方法内部需要访问实例属性
# * 实例方法内部可以使用类名.访问类属性
# 2.类方法 -- 方法内部只需要访问类属性
# 3.静态方法 -- 方法内部，不需要访问实例属性和类属性

# 提问
# 如果方法内部即需要访问实例属性，又要访问类属性，应该定义成什么方法？
# 答案
# 应该定义实例方法
# 因为，类只有一个，在实例方法内部可以使用类名，访问类属性
