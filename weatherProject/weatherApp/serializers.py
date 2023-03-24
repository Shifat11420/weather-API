# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import WeatherData, WeatherLog, WeatherStatistics
from rest_framework.response import Response


class WeatherDataSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer class for weather data
    """
    class Meta:
        model = WeatherData
        fields = ["id", 'stationID', 'date', 'year', 'month', 'day',
                  'maxTemperature', 'minTemperature', 'precipitation_mm']


class WeatherLogSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer class for weather data log
    """
    class Meta:
        model = WeatherLog
        fields = ["id", 'stationID', 'startTime', 'endTime', 'numberOfRecords']


class WeatherStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer class for weather data statistics
    """
    class Meta:
        model = WeatherStatistics
        fields = ["id", 'stationID', 'year', 'avgMaxTemperature', 'avgMinTemperature',
                  'totalPrecipitation_cm']
