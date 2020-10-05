from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Restaurant(models.Model):
    MY_CHOICES = (('Italian', 'Italian'),
        ('Fast Food', 'Fast Food'),
        ('Japanese', 'Japanese'),
        ('Pizza', 'Pizza'),
        ('Multi Cuisine', 'Multi Cuisine'))

    name = models.CharField(max_length=20)
    type = MultiSelectField(choices=MY_CHOICES)
    time = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    location = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(Category, related_name='category_name')

    def __str__(self):
        return self.name

# if extra data is required between resturant and category
class RestaurantCategory(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant.name

class Cuisine(models.Model):
    MY_CHOICES = (('Veg', 'Veg'),
                  ('Non Veg', 'non_veg'),
                  ('Chicken', 'chicken'),
                  ('Mutton', 'mutton'),
                  ('Buff', 'buff'),
                  ('Pork', 'pork'))
    name = models.CharField(max_length=30)
    type = MultiSelectField(choices=MY_CHOICES)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    cuisine = models.ForeignKey(Cuisine, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.IntegerField()
    table_no = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cuisine

