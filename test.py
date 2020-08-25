# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/8/24 14:12
print("-"*20)
print("第一次加载:")
import firstpackage
print("-"*20)
print("第二次加载:")
import firstpackage
print("-"*20)

from firstpackage import hello

hello.foo()























