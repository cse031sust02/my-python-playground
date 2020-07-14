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

# In RabbitMQ a message can never be sent directly to the queue,
# it always needs to go through an exchange
channel.basic_publish(exchange='',
                      routing_key='demo_queue',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
