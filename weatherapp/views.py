from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import City
import requests
import json

def get_weather_data(city_name):
    url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=516304d358b3bbc6673863b646f893be&units=metric".format(city_name)

    ro=requests.get(url)
    dataAsJson=ro.text
    dataAsDict=json.loads(dataAsJson)

    weather_data = {
        "city_name":city_name,
        "country_name":dataAsDict["sys"]["country"],
        "temperature":dataAsDict["main"]["temp"],
        "description":dataAsDict["weather"][0]["description"],
        "wind_speed":dataAsDict["wind"]["speed"]*18/5,
        "cloudiness":dataAsDict["clouds"]["all"],
        "humidity":dataAsDict["main"]["humidity"]
    }

    return weather_data

def index(request):
    if request.method == "POST":
        city_name = request.POST["city_name"].capitalize()
        try:
            weather_data = get_weather_data(city_name)
        except:
            return render(request, "index.html", {"error":True, "all_cities":City.objects.order_by("-id")})
        new_city = City(city_name=weather_data["city_name"], country_name=weather_data["country_name"], temperature=weather_data["temperature"], description=weather_data["description"])
        new_city.save() 

    return render(request, "index.html", {"all_cities":City.objects.order_by("-id")}) 

def clearall(request):
    if request.method == "POST":
        for city in City.objects.all():
            city.delete()
        return redirect("/")