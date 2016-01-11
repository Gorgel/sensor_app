from django.conf.urls import patterns, url
from plotter import views

urlpatterns = patterns('',
                      url(r'^$', views.index, name='index'))
