# -*- coding: utf-8 -*-
# @Time    : 2022/2/23 18:39
# @Author  : Garnetsky
# @FileName: serve.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
import datetime
import time

import pytz
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from sms.tasks import celery_send_sms_code
import apscheduler
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.blocking import BlockingScheduler

REDIS = {
    'host': '127.0.0.1',
    'port': '6379',
    'db': 14,
    'password': ''
}

jobstores = {
    'redis': RedisJobStore(**REDIS),
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}



scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, timezone=pytz.timezone("Asia/Shanghai"))
scheduler.add_job(celery_send_sms_code.delay, "date", run_date=datetime.datetime(2022, 2, 23, hour=21, minute=31),
                  timezone=pytz.timezone("Asia/Shanghai"))
scheduler.start()