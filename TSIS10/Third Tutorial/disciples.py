import pika

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

channel.exchange_declare(exchange='recitations', exchange_type='fanout')


result=channel.queue_declare(queue='',exclusive=1)

channel.queue_bind(exchange='recitations', queue=result.method.queue)
print('Waiting for messages')

def function(ch, method, properties, body):
    print('Received:%r'%body)

channel.basic_consume(queue=result.method.queue, on_message_callback=function, auto_ack=True)

channel.start_consuming()

















