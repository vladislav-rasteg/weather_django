from django.shortcuts import render
import json
import urllib.request
import requests
from app.models import WeatherRequest

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='
            + city + '&appid=2a4ff86f9aaa70041ec8e82db64abf56').read()
        list_of_data = json.loads(source)

        print(str(list_of_data))

        data = {
            "city": city,
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                            + str(list_of_data['coord']['lat']),
            "temp": str(round(list_of_data['main']['temp']-273.15)) + ' °С',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "weather": str(list_of_data['weather'][0]['main']),
            "icon": "http://openweathermap.org/img/w/" + str(list_of_data['weather'][0]['icon']) + ".png",
        }

        weath_req = WeatherRequest(
            req_city = data['city'],
            req_temp = data['temp'],
            req_weather = data['weather'],
        )
        weath_req.save()

        print(data)

    else:
        data = {}
    return render(request, "index.html", data)

def requests(request):
    requests = WeatherRequest.objects.all()
    data = {'requests': requests}
    return render(request, 'requests.html', context=data)