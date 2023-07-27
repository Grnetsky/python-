import pika
import sys

import pika
import sys

credentials = pika.PlainCredentials("admin", "admin")
connect = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1", 5672, credentials=credentials))

channel = connect.channel()
channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

result = channel.queue_declare(exclusive=True, queue="",)
queue_name = result.method.queue
serverites = sys.argv[1:]

def call_back(ch,method,properties,body):
    print(method.routing_key,body)

for serverity in serverites:
    channel.queue_bind(queue=queue_name,
                       exchange="direct_logs",
                       routing_key=serverity
                       )
channel.basic_consume(on_message_callback=call_back,queue=queue_name)
channel.start_consuming()