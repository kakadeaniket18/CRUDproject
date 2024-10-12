from django.db import models

# Create your models here.
class Msg(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    message=models.CharField(max_length=400)