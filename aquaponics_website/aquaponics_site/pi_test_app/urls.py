from django.conf.urls import url

from . import views

app_name = 'aquaponics_app'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.update_pin, name='index'),
    # ex: /test_pi/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
]
