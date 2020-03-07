import models

class Item(forms.Modelform):
    name     = CharField(required=True, max_length=50)
    category = CharField(required=True, max_length=50)
    caliber  = CharField(required=True, max_length=8)
    quantity = IntegerField(required=False, default=0)
