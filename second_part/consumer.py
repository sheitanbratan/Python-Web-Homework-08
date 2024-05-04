import pika

from contact_model import Contact

credentials = pika.PlainCredentials('guest',
                                    'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                               port=5672,
                                                               credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='email_queue')


def callback(ch, method, properties, body):
    body = body.decode('utf-8')
    print(f'[x] Received object id: {body}')
    contact_id = body
    contact = Contact.objects.get(id=contact_id)

    print(f'Sending a mail to {contact.email}')
    contact.mailed = True
    contact.save()
    print(f'Mail was successfully sent to {contact.fullname}')


channel.basic_consume(queue='email_queue',
                      on_message_callback=callback,
                      auto_ack=True)
print('[*] Waiting for messages')
channel.start_consuming()