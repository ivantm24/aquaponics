from django.conf.urls import url

from . import views

app_name = 'aquaponics_app'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^feeder/$', views.fishFeederController),
    # ex: /feeder/2
    url(r'^feeder/(?P<duty_cycle>[0-9]+)$', views.fishFeederController, name='feeder'),

    url(r'^pump/$', views.pumpController),
    # ex: /feeder/2
    url(r'^pump/(?P<value>[0-9]+)$', views.pumpController, name='pump'),
    
]
