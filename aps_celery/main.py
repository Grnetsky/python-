# -*- coding: utf-8 -*-
# @Time    : 2022/2/23 18:36
# @Author  : Garnetsky
# @FileName: main.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
# 创建celery实例

import os
from celery import Celery
# 为celery的运行设置django环境
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hand_homework_script.settings')  # 准备配置
# 参数1： main 设置脚本路径（这个路径是相对于django项目路径的）就可以
app = Celery('aps_celery')

# 2 设置broker
# 通过加载配置文件设置broker
app.config_from_object('aps_celery.config')

# 3 rangcelery自动检测指定包的任务
app.autodiscover_tasks(['aps_celery.sms'])  # 此函数参数是列表，列表元素是tasks的路径 celery会自动在该路径检测tasks.py文件

# 在django项目路径下运行 celery -A celery_task.main worker -l INFO
# celery multi start w1 -A celery_task.main -l info 守护进程方式开启
