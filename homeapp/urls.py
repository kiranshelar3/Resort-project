from os import name
from django.contrib import admin
from django.urls import path
from homeapp import views
from homeapp.models import *



urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about , name='about'),
    path('services', views.services , name='service'),
    path('contact', views.contact , name='contact'),
    path('booKingfunction', views.booKingfunction , name='booKingfunction'),
    path('room_type_list', views.room_type_list, name='room_type_list'),
    path("addbookingsapi", views.addbookingsapi, name="addbookingsapi")




    
]
