import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

QUEUE = 'task_queue'
channel.queue_declare(queue=QUEUE, durable=True) # creates the queue

message = ' '.join(sys.argv[1:]) or 'Hello World!'
channel.basic_publish(exchange='',
                      routing_key=QUEUE,
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2 # make message persistent
                      ))

print("[x] Sent %r" % message)

connection.close()