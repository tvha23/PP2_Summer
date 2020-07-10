import pika
#This is for connecting to the local server
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
#This is for declaring new queue with name hello for publishing messages
channel.queue_declare(queue='hello')
#Basic publish method for publishing message
message='Hello Jello, WYD? I\'m good'
channel.basic_publish(exchange='',  routing_key='hello', body=message)
#If operation is succesful print sent and message itself
print(f'Sent!:{message}')
#After that we should close the connection to make sure messages are delivered 
connection.close()
