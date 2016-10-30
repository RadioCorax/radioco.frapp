from django.core import serializers
from django.shortcuts import render
from .models import Station

def station_data(request):
    station = Station.get_solo()
    return render(
        request, 'frapp/station_data.xml',
        context=dict(station=station),
        content_type='application/xml')
