# Generated by Django 3.2 on 2022-05-19 15:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='public_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]