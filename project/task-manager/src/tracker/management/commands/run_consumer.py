from django.core.management.base import BaseCommand
from django.conf import settings

# import pickle
import json
import uuid

from kafka import KafkaConsumer

from tracker.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        consumer = KafkaConsumer('users-events-stream', bootstrap_servers=settings.BROKER_SERVER)

        for message in consumer:
            deserialized_data = json.loads(message.value)
            action = deserialized_data.get('action')
            if action == 'create/update':
                public_id = deserialized_data['user_info'].get('public_id')
                converted_uuid = uuid.UUID(public_id)
                obj, created = User.objects.update_or_create(
                        public_id=converted_uuid,
                        defaults={
                            'username': deserialized_data['user_info'].get('username'),
                            'first_name': deserialized_data['user_info'].get('first_name'),
                            'last_name': deserialized_data['user_info'].get('last_name'),
                            'role': deserialized_data['user_info'].get('role'),
                        }
                                                        )
            elif action == 'delete':
                public_id = deserialized_data['user_info'].get('public_id')
                converted_uuid = uuid.UUID(public_id)
                try:
                    target_user = User.objects.filter(public_id=converted_uuid)
                    target_user.delete()
                except Exception as e:
                    print(e)
            else:
                print('smth went wrong - very useful info:)')