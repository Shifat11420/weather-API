from django.contrib import admin
from weatherApp.models import WeatherData, WeatherLog, WeatherStatistics

# Register your models here.
admin.site.register(WeatherData)
admin.site.register(WeatherLog)
admin.site.register(WeatherStatistics)
