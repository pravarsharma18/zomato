from django.db.models import Avg, FloatField
from django.db import models

from accounts.models import Buyer, Vendor
from base.constants import Round, Type

class RestaurantQuerySet(models.QuerySet):
    def rating(self):
        qs = self.annotate(ratings=Round(Avg('rating__rating')))
        return qs
    
    def top_rating(self):
        qs = self.rating().filter(ratings__gte=2.5)
        return qs

class RestaurantManager(models.Manager):
    def get_queryset(self):
        return RestaurantQuerySet(self.model, using=self._db)

    def rating(self):
        return self.get_queryset().rating()

    def top_rating(self):
        return self.get_queryset().top_rating()

class Restaurant(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True, blank=True)
    location = models.URLField()
    active = models.BooleanField(default=True)
    open_time = models.TimeField()
    close_time = models.TimeField()
    temporary_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RestaurantManager()

class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=255)
    type = models.CharField(choices=Type.choices(), max_length=10)
    base_price = models.IntegerField()
    thumbnail = models.ImageField(upload_to='dishes_thumbnail/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RestaurantRating(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='rating')
    rating = models.FloatField()
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='restra_rating')

class DishRating(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='rating')
    rating = models.FloatField()
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='dish_rating')