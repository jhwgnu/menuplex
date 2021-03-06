from django.contrib import admin
from board.models import School, Restaurant, Meal
# Register your models here.

class MealAdmin(admin.ModelAdmin):
    def get_school_name(self, meal):
        return meal.school

    def get_restaurant_name(self, meal):
        return meal.restaurant

    get_school_name.short_description = '학교명'
    get_restaurant_name.short_description = '식당명'

    list_display = ['get_school_name', 'get_restaurant_name','meal_name','id']
    list_display_links = ['meal_name']
    list_filter = ['school']

class RestaurantAdmin(admin.ModelAdmin):
    def get_school_name(self, restaurant):
        return restaurant.school

    def get_rest_name(self, restaurant):
        return restaurant.rest_name

    get_school_name.short_description = '학교명'
    get_rest_name.short_description = '식당명'

    list_display = ['get_school_name', 'get_rest_name', 'id']
    list_display_links = ['get_rest_name']
    list_filter = ['school']


admin.site.register(School)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Meal, MealAdmin)
