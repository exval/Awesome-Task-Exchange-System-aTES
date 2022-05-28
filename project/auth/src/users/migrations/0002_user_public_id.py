# Generated by Django 3.2 on 2022-05-12 09:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='public_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
