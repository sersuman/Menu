from django.contrib import admin
from .models import Restaurant, Category, Cuisine, Order, RestaurantCategory


admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Order)
admin.site.register(RestaurantCategory)
