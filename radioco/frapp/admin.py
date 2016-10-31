from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import CableTransmitter, StreamTransmitter, UKWTransmitter
from .models import Station, Studio


class StudioAdmin(admin.StackedInline):
    model = Studio
    extra = 0

class CableTransmitterAdmin(admin.TabularInline):
    model = CableTransmitter
    extra = 1

class UKWTransmitterAdmin(admin.StackedInline):
    model = UKWTransmitter
    extra = 0

class StreamTransmitterAdmin(admin.TabularInline):
    model = StreamTransmitter
    extra = 1

@admin.register(Station)
class StationAdmin(SingletonModelAdmin):
    inlines = [
        StudioAdmin,
        UKWTransmitterAdmin,
        CableTransmitterAdmin,
        StreamTransmitterAdmin ]
