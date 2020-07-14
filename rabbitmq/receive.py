"""
"Hello World" Tutorial using RabbitMQ
src : https://www.rabbitmq.com/tutorials/tutorial-one-python.html

a producer (sender) that sends a single message, and a consumer (receiver) that
receives messages and prints them out. It's a "Hello World" of messaging.

(P) ----> [][][][][] ---> (C)
Producer sends messages to the queue.
The consumer receives messages from that queue.
"""

import pika

# establish a connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create a new queue called demo_queue
channel.queue_declare(queue='demo_queue')

# Creating a queue using queue_declare is idempotent ‒
# only one will be created no matter how many times we run the command
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


#  we need to tell which particular callback function should receive messages
channel.basic_consume(queue='demo_queue',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
