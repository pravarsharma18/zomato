from django.contrib import admin
from .models import Restaurant, Dish, RestaurantRating, DishRating
# Register your models here.

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'vendor']

@admin.register(RestaurantRating)
class RestaurantRatingAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'rating','buyer']

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name','restaurant']

@admin.register(DishRating)
class DishRatingAdmin(admin.ModelAdmin):
    list_display = ['dish', 'rating']
