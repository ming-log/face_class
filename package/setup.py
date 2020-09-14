# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/8/28 11:52

from distutils.core import setup

setup(name="lm",  # 包名
      version="1.0",  # 版本
      description="lm's send and receive",    # 描述信息
      long_description="complete information",  # 完整描述信息
      author="ming luo",  # 作者
      author_email="736704198@qq.com",  # 作者邮箱
      url="www.lm.com",  # 主页
      py_modules=["lm.send_message",
                   "lm.receive_message"])   # 要发布的模块

# 终端使用python解释器执行
# python setup.py build
# 会自动建立build文件夹
# python setup.py sdist
# 会自动建立dist文件夹，文件夹下的压缩文件就是打包好的包
# 然后发送给别人用 pip install+相应的模块压缩包就可以加载到python系统目录
# 删除采用  pip uninstall+相应的模块名就可以卸载
