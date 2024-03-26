from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact=models.CharField(max_length=10)
    password = models.CharField(max_length=20)

