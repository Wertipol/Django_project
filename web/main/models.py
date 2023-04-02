from django.db import models


class SalesOrders(models.Model):
    amount = models.IntegerField()
    name = models.CharField(max_length=255)
