import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

QUEUE = 'hello'
channel.queue_declare(queue=QUEUE) # creates the queue

channel.basic_publish(exchange='',
                      routing_key=QUEUE,
                      body='Hello world!')

print("[x] Sent 'Hello World!'")

connection.close()