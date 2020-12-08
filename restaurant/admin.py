from django.contrib import admin
from django.contrib.auth.models import Group    
from .models import Restaurant, Category, Cuisine, Order, RestaurantCategory


admin.site.site_header = 'Menu'
admin.site.site_title = 'Menu'
admin.site.index_title = 'Menu Admin Panel'

admin.site.unregister(Group)
admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Order)
admin.site.register(RestaurantCategory)
