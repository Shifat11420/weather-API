# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import WeatherData, WeatherLog, WeatherStatistics
from rest_framework.response import Response


class WeatherDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeatherData
        fields = ["id", 'stationID', 'date', 'year', 'month', 'day',
                  'maxTemperature', 'minTemperature', 'precipitation_mm']
        read_only_fields = fields


class WeatherLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeatherLog
        fields = ["id", 'stationID', 'startTime', 'endTime', 'numberOfRecords']
        read_only_fields = fields


class WeatherStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeatherStatistics
        fields = ["id", 'stationID', 'year', 'avgMaxTemperature', 'avgMinTemperature',
                  'totalPrecipitation_cm']
