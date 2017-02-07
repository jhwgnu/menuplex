from django.db import models

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=200)
    school_url = models.CharField(max_length=200)
    school_logo = models.ImageField()
    school_short = models.CharField(max_length = 10, default = '', primary_key=True)

    def __str__(self):
        return self.school_name

class Restaurant(models.Model):
    school = models.ForeignKey(School)
    rest_name = models.CharField(max_length=200)

    def __str__(self):
        return self.rest_name

class Meal(models.Model):
    school = models.ForeignKey(School)
    restaurant = models.ForeignKey(Restaurant)
    meal_name = models.CharField(max_length=200)
    meal_time = models.CharField(max_length=100, choices=(
        ('조식','조식'),
        ('중식','중식'),
        ('석식','석식'),
        ('상시','상시'),
    ))
    price = models.IntegerField()

    def __str__(self):
        return self.meal_name
