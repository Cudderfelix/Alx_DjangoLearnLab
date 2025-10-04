from django.db import models

# Create your models here.
class Subscribers(models.Model):
    email = models.EmailFiled(unique=True)
    name = models.CharField(max_length=100)
    subscription_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('cancelled', 'Cancelled')
    ], default='active')

    def __str__(self):
        return self.email: