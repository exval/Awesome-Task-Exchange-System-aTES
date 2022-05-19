import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from tracker.models import Task


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception


@receiver(post_save, sender=Task)
def task_created_or_updated(sender, instance, created, **kwargs):
	task = instance
	data = {
		'action': 'created/update',
		'user_info': {
			'public_id': str(task.public_id),
			'title': task.title,
			'description': task.description,
			'assigned_on': task.assigned_on,
			'status': task.status,
		}
	}
	producer = KafkaProducer(bootstrap_servers=settings.BROKER_SERVER)
	serialized_data = json.dumps(data).encode('utf-8')
	producer.send('tasks-stream', serialized_data).add_callback(on_send_success).add_errback(on_send_error)