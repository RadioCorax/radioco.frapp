from django.shortcuts import render
from .models import Station


def station_data(request):
    station = Station.get_solo()

    return render(request,
                  'frapp/station_data.xml',
                  context={'station': station},
                  content_type="application/xml")
