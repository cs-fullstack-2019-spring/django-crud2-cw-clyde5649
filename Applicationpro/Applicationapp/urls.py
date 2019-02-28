from django.urls import path

# PATH TO FOR THE APP
from . import views
path('', views.index, name='index'),
path('name',views.name,name='name'),

