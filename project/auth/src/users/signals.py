import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from users.models import User


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception

@receiver(post_save, sender=User)
def produce_create_update_user_event(sender, instance, created, **kwargs):
    user = instance
    data = {
        'action': 'create/update',
        'user_info': {
            'public_id': str(user.public_id),
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'role': user.role,
        }
    }
    print(data)
    producer = KafkaProducer(bootstrap_servers=settings.BROKER_SERVER)
    serialized_data = json.dumps(data).encode('utf-8')
    producer.send('users-events-stream', serialized_data).add_callback(on_send_success).add_errback(on_send_error)

@receiver(post_delete, sender=User)
def produce_delete_event(sender, instance, **kwargs):
    user = instance
    data = {
        'action': 'delete',
        'user_info': {
            'public_id': str(user.public_id)
        }
    }
    producer = KafkaProducer(bootstrap_servers=settings.BROKER_SERVER)
    serialized_data = json.dumps(data).encode('utf-8')
    producer.send('users-events-stream', serialized_data).add_callback(on_send_success).add_errback(on_send_error)
