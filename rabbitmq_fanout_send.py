import pika
from pika import ConnectionParameters

credentials = pika.PlainCredentials('admin', 'admin')  # 远程连接时的用户名和密码
# cconnect = pika.BlockingConnection(pika,ConnectionParameters('127.0.0.1',credentials=credentials))
# 链接rabbitmq服务器
connect = pika.BlockingConnection(ConnectionParameters('127.0.0.1', 5672, credentials=credentials), )

# 设置通道
channel = connect.channel()

# 声明转发器 （fanout模式不需要声明队列）
channel.exchange_declare(exchange="logx", exchange_type="fanout")

# 发布消息
channel.basic_publish(exchange="logx", body="halloworld",routing_key="1",
                      properties=pika.BasicProperties(delivery_mode=2))
# 管饱通道
connect.close()
