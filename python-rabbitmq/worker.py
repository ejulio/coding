import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

QUEUE = 'task_queue'
channel.queue_declare(queue=QUEUE, durable=True) # creates the queue


def callback(ch, method, properties, body):
    print("[x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

#maximum number os messages per consumer while working
channel.basic_qos(prefetch_count=1) 
channel.basic_consume(callback,
                      queue=QUEUE)

print("[*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()