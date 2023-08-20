from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views import View
import json

# The weather data dictionary
weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

class WeatherDetailView(View):
    def get(self, request, city):
        if city in weather_data:
            return JsonResponse(weather_data[city])
        else:
            return HttpResponseNotFound()

    def put(self, request, city):
        if city in weather_data:
            try:
                updated_data = json.loads(request.body)
                weather_data[city].update(updated_data)
                return JsonResponse(updated_data)
            except json.JSONDecodeError:
                return HttpResponseBadRequest()
        else:
            return HttpResponseNotFound()

    def delete(self, request, city):
        if city in weather_data:
            del weather_data[city]
            return JsonResponse({}, status=204)
        else:
            return HttpResponseNotFound()

class WeatherListView(View):
    def post(self, request):
        try:
            new_data = json.loads(request.body)
            city = new_data.get('city')
            if city and city not in weather_data:
                weather_data[city] = {'temperature': new_data.get('temperature'), 'weather': new_data.get('weather')}
                return JsonResponse(new_data, status=201)
            else:
                return HttpResponseBadRequest()
        except json.JSONDecodeError:
            return HttpResponseBadRequest()

