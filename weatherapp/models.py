from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length=50, default="")
    country_name = models.CharField(max_length=50, default="")
    temperature = models.IntegerField()
    description = models.CharField(max_length=100, default="")
    wind_speed = models.IntegerField()
    cloudiness = models.IntegerField()
    humidity = models.IntegerField()
    