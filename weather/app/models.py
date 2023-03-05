from django.db import models

class WeatherRequest(models.Model):
    req_city = models.CharField(max_length=100)
    req_temp = models.CharField(max_length=100)
    req_weather = models.CharField(max_length=100)