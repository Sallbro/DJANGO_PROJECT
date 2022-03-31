from django.db import models

# Create your models here.

class users(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    dateofbirth=models.CharField(max_length=20)
    phoneno=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
