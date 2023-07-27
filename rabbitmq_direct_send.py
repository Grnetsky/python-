import pika
import sys

credentials = pika.PlainCredentials("admin", "admin")
connect = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1", 5672, credentials=credentials))

channel = connect.channel()

channel.exchange_declare("direct_logs", exchange_type="direct")


severities = sys.argv[1] if len(sys.argv)>1 else "info"
message = ''.join(sys.argv[2]) or 'halloworld'

channel.basic_publish(exchange="direct_logs",
                      routing_key=severities,
                      body=message)
print("消息已发出")
channel.close()



