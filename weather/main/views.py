import requests
from django.shortcuts import render
from .models import Weather

API_KEY = 'Your_OpenWeatherMap_API_Key_Here'

def index(request):
    weather = None
    error = None
    recent_searches = Weather.objects.all().order_by('-id')[:5]

    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        lat  = request.POST.get('lat', '').strip()
        lon  = request.POST.get('lon', '').strip()

        try:
            if lat and lon:
                # Request came from "Use my location" button
                url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
            elif city:
                # Request came from city search form
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            else:
                error = "Please enter a city name."
                return render(request, 'index.html', {'weather': weather, 'error': error, 'recent_searches': recent_searches})

            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather = {
                    'city':        data['name'],
                    'temperature': data['main']['temp'],
                    'humidity':    data['main']['humidity'],
                    'description': data['weather'][0]['description'],
                }
                Weather(
                    city=weather['city'],
                    temperature=weather['temperature'],
                    humidity=weather['humidity'],
                    description=weather['description'],
                ).save()
                # Refresh recent searches to include the new entry
                recent_searches = Weather.objects.all().order_by('-id')[:5]
            else:
                error = data.get('message', 'Unable to fetch weather data.')

        except Exception as e:
            error = str(e)

    return render(request, 'index.html', {'weather': weather, 'error': error, 'recent_searches': recent_searches})