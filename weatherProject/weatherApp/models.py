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
    maxTemperature = models.IntegerField()     # data in tenth of deg C
    minTemperature = models.IntegerField()     # data in tenth of deg C
    precipitation_mm = models.IntegerField()   # data in tenth of mm

    class Meta:
        """
        For duplicate check on data entry UniqueConstraint() is used for unique fields stationID and date
        """
        constraints = [
            models.UniqueConstraint(fields=['stationID', 'date'],
                                    name='unique_stationID_date')
        ]

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

    class Meta:
        """
        For duplicate check on data entry UniqueConstraint() is used for unique field stationID
        """
        constraints = [
            models.UniqueConstraint(fields=['stationID'],
                                    name='unique_stationID')
        ]

    def __str__(self):
        return str(self.stationID)+" "+str(self.numberOfRecords)


class WeatherStatistics(models.Model):
    """
    Model for storing all the weather calculation for each file/station, for each year
    """
    stationID = models.CharField(max_length=20)
    year = models.IntegerField()
    avgMaxTemperature = models.FloatField(
        null=True, blank=True, default=None)    # data in degree celcious
    avgMinTemperature = models.FloatField(
        null=True, blank=True, default=None)    # data in degree celcious
    totalPrecipitation_cm = models.FloatField(
        null=True, blank=True, default=None)    # data in centimeters

    class Meta:
        """
        For duplicate check on data entry UniqueConstraint() is used for unique fields stationID and year
        """
        constraints = [
            models.UniqueConstraint(fields=['stationID', 'year'],
                                    name='unique_stationID_year')
        ]

    def __str__(self):
        return str(self.stationID)+" "+str(self.year)
