import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CHOICES = (
        ('MNGR', 'Manager'),
        ('DEV', 'Developer'),
        ('ACC', 'ACCOUNTER',)
    )
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=32, choices=CHOICES)
