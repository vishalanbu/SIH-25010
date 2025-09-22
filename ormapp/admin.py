from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'brand', 'model', 'year', 'fuel_type', 'mileage', 'color')

admin.site.register(Car, CarAdmin)