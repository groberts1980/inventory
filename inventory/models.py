
from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=50, unique=False, blank=False, null=False)

    def __str__(self):
        return self.category

class Item(models.Model):
    item_id  = models.AutoField(primary_key=True)
    name     = models.CharField(max_length=50, null=False)
    serial   = models.CharField(max_length=15, null=False)
    caliber  = models.CharField(max_length=8, null=True)
    quantity = models.IntegerField(default=0, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
