# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import WeatherData, WeatherLog, WeatherStatistics


class WeatherDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['stationID', 'date', 'year', 'month', 'day',
                  'maxTemperature', 'minTemperature', 'precipitation_mm']
        read_only_fields = fields


class WeatherLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeatherLog
        fields = ['stationID', 'startTime', 'endTime', 'numberOfRecords']
        read_only_fields = fields


class WeatherStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeatherStatistics
        fields = ['stationID', 'year', 'avgMaxTemperature', 'avgMinTemperature',
                  'totalPrecipitation_cm']
