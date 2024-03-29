# mqtt_rabbitmq_integration/consumer.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='FILE_METADATA')

def callback(ch, method, properties, body):
    print("Received message:", body)

channel.basic_consume(queue='FILE_METADATA', on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()
