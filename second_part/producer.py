import pika
from faker import Faker

from contact_model import Contact


credentials = pika.PlainCredentials('guest',
                                    'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                               port=5672,
                                                               credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

fake = Faker()
for _ in range(10):
    fullname = fake.name()
    email = fake.email()

    contact = Contact(
        fullname=fullname,
        email=email
    )
    contact.save()

    channel.basic_publish(exchange='',
                          routing_key='email_queue',
                          body=str(contact.id))
    print('Message was successfully sent')

connection.close()