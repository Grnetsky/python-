# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 09:39
# @Author  : Garnetsky
# @FileName: a.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
import time


class Content():
    def __init__(self):
        self.a = 'hh'
        self.b = 'xx'

data = Content()
while 1:
    time.sleep(1)
    print(data.a)

