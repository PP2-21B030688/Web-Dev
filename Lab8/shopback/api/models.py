from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()
    category_name = models.CharField(max_length = 255)

class Categories(models.Model):
    name = models.CharField(max_length = 255);