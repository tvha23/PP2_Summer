import pika
import sys

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

channel.exchange_declare(exchange='direct_logs',exchange_type='direct')

severity=sys.argv[1] if len(sys.argv) > 1 else 'info'

message=str()
for i in sys.argv[2:]:
    message+=i+' '

channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message )
print('Sent %r:%r'%(severity, message))
