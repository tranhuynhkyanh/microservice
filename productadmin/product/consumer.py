import json

import pika

from productadmin.product.models import Product

params = pika.URLParameters('your_rabbitmq_url')

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='product_admin')


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_like':
        product = Product.objects.get(id=data['id'])
        product.add_likes()
        print('Product like', product.likes)


channel.basic_consume(queue='product_admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()