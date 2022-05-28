from django.core.management.base import BaseCommand
from django.conf import settings

# import pickle
import json
import uuid

from kafka import KafkaConsumer

from tracker.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        consumer = KafkaConsumer('users-stream', bootstrap_servers=settings.BROKER_SERVER)

        for message in consumer:
            deserialized_data = json.loads(message.value)
            # action = deserialized_data.get('action')
            if message.key == b'create':
                public_id = deserialized_data['user_info'].get('public_id')
                converted_uuid = uuid.UUID(public_id)
                created = User.objects.create(public_id=converted_uuid,
                                              username=deserialized_data['user_info'].get('username'),
                                              first_name=deserialized_data['user_info'].get('first_name'),
                                              last_name=deserialized_data['user_info'].get('last_name'),
                                              role=deserialized_data['user_info'].get('role'))
                print('created')
            elif message.key == b'update':
                public_id = deserialized_data['user_info'].get('public_id')
                converted_uuid = uuid.UUID(public_id)
                try:
                    user = User.objects.get(public_id=public_id)
                    user.username = deserialized_data['user_info'].get('username')
                    user.first_name = deserialized_data['user_info'].get('first_name')
                    user.last_name = deserialized_data['user_info'].get('last_name')
                    user.role = deserialized_data['user_info'].get('role')
                    user.save()
                    print('updated')
                except User.DoesNotExist:
                    print(f'User with public_id {public_id} does not exist')
            elif message.key == b'delete':
                public_id = deserialized_data['user_info'].get('public_id')
                converted_uuid = uuid.UUID(public_id)
                try:
                    target_user = User.objects.filter(public_id=converted_uuid)
                    target_user.delete()
                except Exception as e:
                    print(e)
            else:
                print('smth went wrong - very useful info:)')
