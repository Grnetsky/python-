# -*- coding: utf-8 -*-
# @Time    : 2022/3/19 10:37
# @Author  : Garnetsky
# @FileName: 观察者（发布订阅模式）.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
import threading
# class Publisher(object):
#     a = 1
#     def __init__(self, name, age):
#         self.name = name
#         self.agg = age
#         self.a += 1
#         Publisher.x()
#
#     @classmethod
#     def x(cls):
#         cls.a+=1
#         print(cls.a)
#
# a1 = Publisher("123",123)
# a2 = Publisher("123",412)
import time


def say():
    print("hhhh")

class Pulisher(object):
    eventList = {}
    def __init__(self):
        pass
    def publish(self,key):
        for i in self.eventList[key]:
            i()
    def subcrime(self,key,fn):
        self.eventList[key].append(fn)


class Subceimer(object):
    def __init__(self):
        pass
    def subcrime(self,event,callback):
        pass

p = Pulisher()
p.subcrime(say)


time.sleep(3)
p.publish()

