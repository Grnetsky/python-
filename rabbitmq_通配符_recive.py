# -*- coding: utf-8 -*-
# @Time    : 2022/2/16 19:12
# @Author  : Garnetsky
# @FileName: rabbitmq_通配符_recive.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
import pika
from pika import ConnectionParameters

credentials = pika.PlainCredentials('admin', 'admin')  # 远程连接时的用户名和密码
# cconnect = pika.BlockingConnection(pika,ConnectionParameters('127.0.0.1',credentials=credentials))
# 链接rabbitmq服务器
connect = pika.BlockingConnection(ConnectionParameters('127.0.0.1', 5672, credentials=credentials), )

# 设置通道
channel = connect.channel()

# 声明转发器 （fanout模式不需要声明队列）
channel.exchange_declare(exchange="logx",exchange_type="topic")
# 声明队列
result = channel.queue_declare(exclusive=True,queue='')  # exclusive 排他 保证唯一队列名字 并会是此queue断开后自动删除queue 指定queue为空值
queuename= result.method.queue
# 发布消息
channel.queue_bind(exchange="logx",queue=queuename,
                   routing_key="#.weather"
                   )  # 将自己随机生成的queue绑定到交换机上
# 管饱通道

def call_back(ch,method,pro,body):
    print("已消费"+("-"*100))
    print(body)
    print(5)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(on_message_callback=call_back,
                      queue=queuename,
                      auto_ack=False,
                    )
channel.start_consuming()