#!/usr/bin/env python
# Lesson 3. Publish/Subscribe - log emitter.
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

# Объявляем fanout exchange - все сообщения идут во ВСЕ очереди
channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
)
print(f" [x] Sent {message}")

connection.close()