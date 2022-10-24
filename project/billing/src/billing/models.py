import uuid

from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False, null=False)


class Account(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    balance = models.IntegerField(default=0)


class Task(models.Model):
    title = models.CharField(max_length=132, null=False, blank=False)
    price = models.IntegerField()


class Payment(models.Model):
    STATUS_CHOICES = (
        ('PD', 'Paid'),
        ('PN', 'Pending'),
        ('ER', 'Error')
    )
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)


class Transaction(models.Model):
    TYPE = (
        ('DEB', 'Debit'),
        ('CD', 'Credit')
    )
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    operation_type = models.CharField(max_length=12, choices=TYPE)
    cash = models.IntegerField()
    payment = models.ForeignKey(Payment, on_delete=models.DO_NOTHING)
    datetime = models.DateTimeField(auto_now=True)


class BillingCycle(models.Model):
    STATUS_CHOICES = (
        ('ACTV', 'Active'),
        ('Clsd', 'Closed')
    )

    billing_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
