from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Station, Studio


class StudioAdmin(admin.TabularInline):
    model = Studio


class StationAdmin(SingletonModelAdmin):
    inlines = [StudioAdmin,]


admin.site.register(Station, StationAdmin)
