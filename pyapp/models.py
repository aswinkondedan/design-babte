from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=100)
    contact=models.BigIntegerField()
    email=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    user_type=models.BooleanField(default=False)

