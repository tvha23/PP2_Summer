import pika
import sys #for sys.argv

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

channel.exchange_declare(exchange='recitations', exchange_type='fanout')

message=str()
for i in sys.argv[1:]:
    message+=i+' '


channel.basic_publish(exchange='recitations', routing_key='', body=message)
print(f'Sent!:{str(message)}')
connection.close()