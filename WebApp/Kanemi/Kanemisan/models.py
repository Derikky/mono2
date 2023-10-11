from django.db import models

class Things(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
