from django.urls import path
from . import views

urlpatterns = [
    path('restaurant/<int:pk>', views.get_restaurant, name='get-restaurant'),
    path('restaurant/cuisine/<int:restaurant_id>/<int:category_id>', views.get_restaurant_cuisine, name='get-restaurant-cuisine'),
    path('order/<int:restaurant_pk>/<int:cuisine_pk>', views.order, name='order'),
]