from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    customer_id=models.AutoField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=200)
    customer_email=models.CharField(max_length=100)
    customer_address=models.CharField(max_length=100)
    customer_phone=models.CharField(max_length=10)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table="customer"
    def __str__(self):
        return self.username

class FailedLoginAttempt(models.Model):
    username = models.CharField(max_length=100)
    attempts = models.IntegerField(default=0)
    last_attempt = models.DateTimeField(auto_now=True)
        
