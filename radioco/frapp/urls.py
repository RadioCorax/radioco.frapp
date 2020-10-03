from django.urls import path

from radioco.frapp import views
from radioco.frapp.config import FRAppConfig


app_name = FRAppConfig.name


urlpatterns = [
    path('', views.station_data, name='index'),
]
