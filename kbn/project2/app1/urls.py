from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('add/result',views.result,name='result'),
]
