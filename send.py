import pika

# establish a connection to RabbitMQ server
rabbit_connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', credentials=pika.PlainCredentials('user', 'password')))
rabbit_channel = rabbit_connection.channel()

# declare a queue
# rabbit_channel.queue_declare(queue='my_queue', durable=True, arguments={"x-queue-type": "quorum"})

# post a message to the queue previously declared
rabbit_channel.basic_publish(exchange='', routing_key='my_queue', body='Hello World!')

rabbit_connection.close()