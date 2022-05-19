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


class Task(models.Model):
    STATUS_CHOICES = (
        ('OP', 'Open'),
        ('DN', 'Done')
    )
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField()
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    assigned_on = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
