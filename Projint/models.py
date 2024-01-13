from django.utils import timezone

from django.db import models

class MyData(models.Model):
    date = models.CharField(max_length=255)
    trade_code = models.CharField(max_length=255)
    high = models.CharField(max_length=255)
    low = models.CharField(max_length=255)
    open = models.CharField(max_length=255)
    close = models.CharField(max_length=255)
    volume = models.CharField(max_length=255)