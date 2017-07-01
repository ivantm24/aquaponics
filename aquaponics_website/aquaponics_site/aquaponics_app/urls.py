from django.conf.urls import url

from . import views

app_name = 'aquaponics_app'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^feeder/$', views.fishFeederController),
    # ex: /feeder/2
    url(r'^feeder/(?P<duty_cycle>[0-9]+)$', views.fishFeederController, name='feeder'),
    # ex: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
]
