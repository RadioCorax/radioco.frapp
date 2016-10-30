from django.conf.urls import include, url

urlpatterns = [
    url(r'^station-data/', include(
        'radioco.frapp.urls', namespace='frapp')),
]
