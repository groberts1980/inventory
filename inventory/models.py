
from django.db import models

class Category(models.Model):
    category = CharField(max_length=50)

    def __str__(self):
        return self.category

class Item(models.Model):
    item_id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    category = ForeignKey(Category, on_delete=models.CASCADE)
    quantity = IntegerField(default=0)

    def __str__(self):
        return self.name
