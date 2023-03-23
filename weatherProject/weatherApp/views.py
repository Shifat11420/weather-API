import os
import time
from datetime import datetime

from django.db.models import Avg, Q, Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView  # , Response

from weatherProject.settings import DATAFILES_FOLDER

from .models import WeatherData, WeatherLog, WeatherStatistics
from .serializers import (WeatherDataSerializer, WeatherLogSerializer,
                          WeatherStatisticsSerializer)
from rest_framework import status


class WeatherDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all weather data to be viewed or edited.
    """
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['stationID', 'date']
    search_fields = ['stationID', 'date']
    ordering_fields = ['stationID', 'date']


class WeatherLogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows log information for weather datafiles to be viewed or edited.
    """
    queryset = WeatherLog.objects.all()
    serializer_class = WeatherLogSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['stationID']
    search_fields = ['stationID']
    ordering_fields = ['stationID']


class WeatherStatisticsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all calculated weather data results to be viewed or edited.
    """
    queryset = WeatherStatistics.objects.all()
    serializer_class = WeatherStatisticsSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['stationID', 'year']
    search_fields = ['stationID', 'year']
    ordering_fields = ['stationID', 'year']


class WeatheranalysisView(APIView):
    """
    Generates weather/stats. The calculations are performed and saved in the database (WeatherStatistics).
    """
    @ classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, format=None):

        queryset = WeatherData.objects.values(
            'stationID', 'year').distinct().exclude(
            maxTemperature=-9999).exclude(
            minTemperature=-9999).exclude(
            precipitation_mm=-9999).annotate(
            avgmaxTemp=Avg('maxTemperature'),
            avgminTemp=Avg('minTemperature'),
            totalPrecip=Sum('precipitation_mm'))

        dataList = []
        for item in queryset.iterator():
            # average temperatures are divided by 10
            # to convert from "in tenth degree Celsius" to "degree Celsius" and
            # total precipitation is divided by 10 to convert from "Millimeters"
            # to "Centimeters"
            # values roounded upto 3 decimal places

            data = {"stationID": item['stationID'],
                    "year": item['year'],
                    "avgMaxTemperature": round((item['avgmaxTemp']/10), 3),
                    "avgMinTemperature": round((item['avgminTemp']/10), 3),
                    "totalPrecipitation_cm": round((item['totalPrecip']/10), 3)}
            dataList.append(WeatherStatistics(**data))
        WeatherStatistics.objects.bulk_create(dataList, ignore_conflicts=True)
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)


class WeatheringectView(APIView):
    """
    Ingest the data into the database (WeatherData). Logs are also calculated and saved in the database (WeatherLog).
    """
    @ classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, format=None):
        path = os.path.join(DATAFILES_FOLDER, "data\wx_data")
        os.chdir(path)
        datalogList = []
        for file in os.listdir():
            filename = file.split(".txt")
            if file.endswith('.txt'):
                file_path = f"{path}/{file}"
                with open(file_path, 'r') as file:
                    startTimeL = time.time()
                    count = 0
                    dataList = []
                    for line in file.readlines():
                        count += 1
                        line = line.strip()
                        fieldvalue = line.split("\t")
                        dateL = datetime.strptime(
                            fieldvalue[0], '%Y%m%d').strftime('%Y-%m-%d')
                        yearL = int(fieldvalue[0][0:4])
                        monthL = int(fieldvalue[0][4:6])
                        dayL = int(fieldvalue[0][6:8])
                        maxTempL = int(fieldvalue[1])
                        minTempL = int(fieldvalue[2])
                        precipitationL = int(fieldvalue[3])

                        data = {"stationID": filename[0],
                                "date": dateL,
                                "year": yearL,
                                "month": monthL,
                                "day": dayL,
                                "maxTemperature": maxTempL,
                                "minTemperature": minTempL,
                                "precipitation_mm": precipitationL}
                        dataList.append(WeatherData(**data))
                    WeatherData.objects.bulk_create(
                        dataList, ignore_conflicts=True)

                    datalog = {"stationID": filename[0],
                               "startTime": str(startTimeL),
                               "endTime": str(time.time()),
                               "numberOfRecords": count}
                    datalogList.append(WeatherLog(**datalog))
        WeatherLog.objects.bulk_create(
            datalogList, ignore_conflicts=True)
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)
