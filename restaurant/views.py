from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Restaurant, Category, RestaurantCategory, Cuisine, Order
from .serializers import RestaurantSerializer, CuisineSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
@csrf_exempt
def get_restaurant(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
    except ObjectDoesNotExist as e:
        return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@csrf_exempt
def get_restaurant_cuisine(request, restaurant_id, category_id):
    try:
        cuisine = Cuisine.objects.get(restaurant=restaurant_id, category=category_id)
        serializer = CuisineSerializer(cuisine)
        return Response(serializer.data)
    except ObjectDoesNotExist as e:
        return Response({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
@csrf_exempt
def order(request, restaurant_pk, cuisine_pk):
    payload = request.data
    try:
        cuisine = Cuisine.objects.get(pk=cuisine_pk)
        restaurant = Restaurant.objects.get(pk=restaurant_pk)
        order = Order.objects.create(
            cuisine=cuisine,
            quantity=payload["quantity"],
            price=payload["price"],
            table_no=payload["table_no"],
            restaurant=restaurant
        )
        serializer = OrderSerializer(order)
        return Response('success', status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    # except Exception:
    #     return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
    #                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #
