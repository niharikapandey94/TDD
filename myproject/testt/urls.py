from django.contrib import admin


from django.urls import path
from .views import WeatherDetailView, WeatherListView

urlpatterns = [
     path('',  WeatherListView.as_view(), name='weather_list'),
    path('weather/<str:city>/', WeatherDetailView.as_view(), name='weather_detail'),
    path('weather/', WeatherListView.as_view(), name='weather_list'),
]
