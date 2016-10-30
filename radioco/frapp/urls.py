from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.station_data, name='index'),
]
