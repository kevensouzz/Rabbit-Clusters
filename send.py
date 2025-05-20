import pika

hosts = [
    ("rabbit-1", 5672),
    ("rabbit-2", 5673),
    ("rabbit-3", 5674)
]

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

rabbit_channel.basic_publish(exchange='', routing_key='my_queue', body='Hello World!')

rabbit_connection.close()