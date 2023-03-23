from django.db import models


class WeatherData(models.Model):
    """
    Model for storing all the weather data
    """
    stationID = models.CharField(max_length=20)
    date = models.DateField()
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    maxTemperature = models.IntegerField()
    minTemperature = models.IntegerField()
    precipitation_mm = models.IntegerField()

    def __str__(self):
        return str(self.stationID)+" "+str(self.date)


class WeatherLog(models.Model):
    """
    Model for storing all the weather data logs, for each file/station
    """
    stationID = models.CharField(max_length=20)
    startTime = models.CharField(max_length=50)
    endTime = models.CharField(max_length=50)
    numberOfRecords = models.IntegerField()

    def __str__(self):
        return str(self.stationID)+" "+str(self.numberOfRecords)


class WeatherStatistics(models.Model):
    """
    Model for storing all the weather calculation for each file/station, for each year
    """
    stationID = models.CharField(max_length=20)
    year = models.IntegerField()
    avgMaxTemperature = models.FloatField(null=True, blank=True, default=None)
    avgMinTemperature = models.FloatField(null=True, blank=True, default=None)
    totalPrecipitation_cm = models.FloatField(
        null=True, blank=True, default=None)

    def __str__(self):
        return str(self.stationID)+" "+str(self.year)
