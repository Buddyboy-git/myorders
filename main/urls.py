from tokenize import Name
from urllib import request
from django.http import HttpResponse
from django.urls import path, re_path, include
from .views import HomePageView
from . import views

urlpatterns = [
    path('home', views.HomePageView, name="home"),
    #path("", homePageView, name="home"),
    re_path(r'^hw/$', views.helloworld, name='helloworld'),
    re_path(r'^order_input/$', views.order_input, name='order_input'),
    re_path(r'^time/$', views.today_is, name='time'),
    re_path(r'^$', views.index, name='index'),
]