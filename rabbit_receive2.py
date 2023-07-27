import pika
from pika import ConnectionParameters

credentials = pika.PlainCredentials('admin','admin')  # 远程连接时的用户名和密码
# cconnect = pika.BlockingConnection(pika,ConnectionParameters('127.0.0.1',credentials=credentials))
# 链接rabbitmq服务器
connect = pika.BlockingConnection(ConnectionParameters('127.0.0.1',5672,credentials=credentials),)
# 设置通道
channel = connect.channel()
# 声明消息队列
channel.queue_declare("hallo")

def call_back(ch,method,pro,body):
    print("已消费"+("-"*100))
    print(method)

channel.basic_consume(on_message_callback=call_back,
                    auto_ack=True,
                      queue="hallo"
                    )
channel.start_consuming()