import pika, os, sys

hosts = [
    ("rabbit-1", 5672),
    ("rabbit-2", 5673),
    ("rabbit-3", 5674)
]

def main():
    for rHost, port in hosts:
        try:
            params = pika.ConnectionParameters(
                host="localhost",
                port=port,
                credentials=pika.PlainCredentials('user', 'password')
            )
            rabbit_connection = pika.BlockingConnection(params)
            break
        except pika.exceptions.AMQPConnectionError:
            continue
    else:
        raise Exception("Nothing RabbitMQ server is available")

    rabbit_channel = rabbit_connection.channel()

    rabbit_channel.queue_declare(queue='my_queue')

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