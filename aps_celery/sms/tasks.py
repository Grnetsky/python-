# 文件名必须为 tasks.py

# 1这个函数必须让celery实例的task装饰器装饰
# 2需要celery自动检测指定包的任务
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.extend([BASE_DIR,])
from aps_celery.main import app




#  生产者
@app.task
def celery_send_sms_code():
    print("发送邮件")


# 将消息推进消息队列  函数名.delay(函数参数 )s
