from django.utils import timezone

from django.db import models

class MyData(models.Model):
    date = models.DateField(default=timezone.now)
    trade_code = models.CharField(max_length=255)
    high = models.FloatField(default= 0)
    low = models.FloatField(default= 0)
    open = models.FloatField(default= 0)
    close = models.FloatField(default= 0)
    volume = models.IntegerField()