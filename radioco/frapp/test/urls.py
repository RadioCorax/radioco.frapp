from django.urls import include, path

urlpatterns = [
    path('station-data/', include('radioco.frapp.urls', namespace='frapp')),
]
