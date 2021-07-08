from django.db import models

# Create your models here.

class RandomNumbers(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    number3 = models.IntegerField()
    number4 = models.IntegerField()
    number5 = models.IntegerField()
    ip = models.GenericIPAddressField()