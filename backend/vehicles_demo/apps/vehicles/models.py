from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)

class Vehicles(models.Model):
    vin = models.CharField(max_length=500)
    reg_no = models.CharField(max_length=500)
    online = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, related_name='vehicles', on_delete=models.CASCADE)