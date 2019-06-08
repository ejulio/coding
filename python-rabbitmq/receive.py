import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

QUEUE = 'hello'
channel.queue_declare(queue=QUEUE) # creates the queue


def callback(ch, method, properties, body):
    print("[x] Received %r" % body)


channel.basic_consume(callback,
                      queue=QUEUE,
                      no_ack=True)

print("[*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()