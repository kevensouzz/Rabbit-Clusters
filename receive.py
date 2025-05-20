#!/usr/bin/env python
import pika, os, sys

def main():
    rabbit_connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            port=5672,
            credentials=pika.PlainCredentials('user', 'password')
        )
    )
    rabbit_channel = rabbit_connection.channel()

    rabbit_channel.queue_declare(
        queue='my_queue',
        durable=True,
        arguments={"x-queue-type": "quorum"}
    )

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    rabbit_channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    rabbit_channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(" [*] Exiting...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)