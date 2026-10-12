#!/usr/bin/env python
# Lesson 3. Publish/Subscribe - log receiver.
import pika
import sys
import os


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()

    # Объявляем тот же fanout exchange
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    # Создаём эксклюзивную очередь (удаляется после отключения)
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # Привязываем очередь к exchange
    channel.queue_bind(exchange='logs', queue=queue_name)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(f" [x] {body.decode()}")

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)