import pika
import sys

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

channel.exchange_declare(exchange='direct_logs',exchange_type='direct')

result=channel.queue_declare(queue='',exclusive=1)

severities=sys.argv[1:]

if not severities:
    sys.stderr.write('Usage: %s [something] [info] [warning] [error]\n'%sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=result.method.queue, routing_key=severity)

print('Waiting for logs')

def function(ch,method,properties,body):
    print('Received: %r:%r'%(method.routing_key, body))

channel.basic_consume(queue=result.method.queue, on_message_callback=function, auto_ack=1)

channel.start_consuming()

