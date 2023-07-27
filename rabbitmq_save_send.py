import pika
from pika import ConnectionParameters

credentials = pika.PlainCredentials('admin','admin')  # 远程连接时的用户名和密码
# cconnect = pika.BlockingConnection(pika,ConnectionParameters('127.0.0.1',credentials=credentials))
# 链接rabbitmq服务器
connect = pika.BlockingConnection(ConnectionParameters('127.0.0.1',5672,credentials=credentials),)

# 设置通道
channel = connect.channel()
# 声明消息队列
channel.queue_declare("hallo",durable=True)

# 发布消息
channel.basic_publish(exchange="", routing_key="hallo", body="halloworld",
                      properties=pika.BasicProperties(delivery_mode=2))
# 关闭通道
connect.close()

