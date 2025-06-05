from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='hmpage'),
    path('about', views.about, name='abtpage'),
]