import pika

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()

channel.queue_declare(queue='hello')

def function(ch, method, properties, body):
    print('Received!:%r'%body)

channel.basic_consume(queue='hello', auto_ack=1, on_message_callback=function)

print('Waiting for messages. You know how to exit')
channel.start_consuming()

    