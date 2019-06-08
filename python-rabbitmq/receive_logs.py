import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
# delete when the connection is closed
result = channel.queue_declare(exclusive=True)
channel.queue_bind(exchange='logs',
                   queue=result.method.queue)


def callback(ch, method, properties, body):
    print("[x] Received %r" % body)

#maximum number os messages per consumer while working
channel.basic_qos(prefetch_count=1) 
channel.basic_consume(callback,
                      queue=result.method.queue,
                      no_ack=True)

print("[*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()