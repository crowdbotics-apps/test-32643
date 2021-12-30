from django.conf import settings
from django.db import models


class Product(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    price = models.FloatField()


# Create your models here.
