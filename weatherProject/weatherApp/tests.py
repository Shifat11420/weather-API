from rest_framework.test import APITestCase
from .models import WeatherData, WeatherLog, WeatherStatistics


class TestWeatherData(APITestCase):
    url = "/api/weather/"

    def setUp(self):
        WeatherData.objects.create(stationID="USC0001", date="2020-04-20", year=2020,
                                   month=4, day=20, maxTemperature=-111, minTemperature=-217, precipitation_mm=94)

    def test_get_weather(self):

        response = self.client.get(self.url)
        result = response.json()
        print(result)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result['results'], list)
        self.assertEqual(result['results'][0]["stationID"], "USC0001")


class TestWeatherLog(APITestCase):
    url = "/api/weather/log/"

    def setUp(self):
        WeatherLog.objects.create(stationID="USC0001", startTime="1679539015.4599073",
                                  endTime="1679539016.694612",
                                  numberOfRecords=10000)

    def test_get_weatherlog(self):

        response = self.client.get(self.url)
        result = response.json()
        print(result)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result['results'], list)
        self.assertEqual(result['results'][0]["numberOfRecords"], 10000)


class TestWeatherStatistics(APITestCase):
    url = "/api/weather/stats/"

    def setUp(self):
        WeatherStatistics.objects.create(stationID="USC0001", year=2020,
                                         avgMaxTemperature=15.0,
                                         avgMinTemperature=4.0,
                                         totalPrecipitation_cm=99.99)

    def test_get_weatherlog(self):

        response = self.client.get(self.url)
        result = response.json()
        print(result)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result['results'], list)
        self.assertEqual(result['results'][0]["avgMinTemperature"], 4.0)
