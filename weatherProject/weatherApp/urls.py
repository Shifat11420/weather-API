from django.urls import include, path
from rest_framework import routers
from . import views


from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Weather API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)

router = routers.DefaultRouter()

router.register(r'api/weather/stats',
                views.WeatherStatisticsViewSet, 'stats')
router.register(r'api/weather/log', views.WeatherLogViewSet)
router.register(r'api/weather', views.WeatherDataViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('weather/calc/', views.WeatheranalysisView.as_view(), name='calc'),
    path('weather/ingestdata/', views.WeatheringestView.as_view(), name='ingest'),
    path('api/v1/swagger/schema/', schema_view.with_ui('swagger',
                                                       cache_timeout=0), name="swagger-schema"),
]

urlpatterns += router.urls
