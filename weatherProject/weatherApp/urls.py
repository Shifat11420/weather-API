from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

router.register(r'api/weather', views.WeatherDataViewSet)
router.register(r'api/weatherlog', views.WeatherLogViewSet)
router.register(r'api/weather/stats/',
                views.WeatherStatisticsViewSet, 'stats')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('weather/calc/', views.WeatheranalysisView.as_view(), name='calc'),
    path('weather/ingectdata/', views.WeatheringectView.as_view(), name='ingect'),
]
