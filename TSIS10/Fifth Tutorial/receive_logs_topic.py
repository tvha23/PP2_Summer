import pika
import sys

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result= channel.queue_declare('', exclusive=1)

binding_keys = sys.argv[1:]

if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

print('Waiting for logs.')

def function(ch, method, properties, body):
    print("Receivde! %r:%r" % (method.routing_key, body))

channel.basic_consume(queue=result.method.queue, on_message_callback=function, auto_ack=True)

channel.start_consuming()

