# -*- coding: utf-8 -*-
# @Time    : 2022/2/12 10:56
# @Author  : Garnetsky
# @FileName: sch.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
from apscheduler.schedulers.blocking import BlockingScheduler

sch = BlockingScheduler(timezone="Asia/Shanghai")


def fun():
    print("123")


sch.add_job(fun,'cron', hour=11,minute=16,end_date='2022-12-19')
sch.start()
