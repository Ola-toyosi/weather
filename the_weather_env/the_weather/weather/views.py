from django.shortcuts import render
import requests
from .models import City


# Create your views here.

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=YOUR_APP_KEY'

    cities = City.objects.all()  # return all cities in the database

    weather_data = []

    for city in cities:
        city_weather = requests.get(
            url.format(city)).json()  # request the API data and convert the JSON to Python data types

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        print(weather)

        weather_data.append(weather)  # add the data for the current city into the list

    context = {'weather_data': weather_data}

    return render(request, 'weather/index.html', context)  # returns the index.html template
