from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)  
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    fuel_type = models.CharField(max_length=20)
    mileage = models.IntegerField()
    color = models.CharField(max_length=30)
    price=models.DecimalField (max_digits=10, decimal_places=2)
class CarAdmin(admin.ModelAdmin):
     list_display = ('car_id', 'brand', 'model', 'year','fuel_type', 'mileage', 'color')
  
    



     

