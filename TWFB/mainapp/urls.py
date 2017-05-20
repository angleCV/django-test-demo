from django.conf.urls import *
from . import views

app_name = 'mainapp'
urlpatterns = [
    url(r'^$', views.home, name='index_base'),
    url(r'^zblist$', views.zbList, name="zbList"),
    url(r'^h$', views.history, name='history'),
    url(r'^actanble$', views.test_ajax, name='test_ajax'),
]