
from django.db import models

class Category(models.Model):
    category = CharField(max_length=50)

    def __str__(self):
        return self.category

class Item(models.Model):
    item_id  = AutoField(primary_key=True)
    name     = CharField(max_length=50, null=False)
    serial   = CharField(max_length=15, null=False)
    caliber  = CharField(max_length=8, null=True)
    quantity = IntegerField(default=0, null=True)

    category = ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
