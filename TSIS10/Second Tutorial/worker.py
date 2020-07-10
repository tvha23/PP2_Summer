import pika
import time#For time.sleep() method
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()

#channel.queue_declare(queue='hello',)
channel.queue_declare(queue='task_queue', durable=True)


def function(ch, method, properties, body):
    print('Received!:%r'%body)
    time.sleep(body.count(b'.'))
    print(f'{str(body)} is Done!')
    ch.basic_ack(delivery_tag=method.delivery_tag)
    
#For give workers   task if only they finished previous 
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='task_queue', on_message_callback=function)

print('Waiting for messages. You know how to exit')
channel.start_consuming()

    