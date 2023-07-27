# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 22:46
# @Author  : Garnetsky
# @FileName: 状态模式.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top

# 状态模式又叫对象的行为模式

from abc import abstractmethod, ABCMeta


class Water:

    def __init__(self):
        self.__temperature = 0

