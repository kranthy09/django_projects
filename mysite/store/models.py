from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    started_at = models.DateField()
    hq_location = models.TextField()


class Mobile(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    ram = models.IntegerField()
    price_in_inr = models.IntegerField()
