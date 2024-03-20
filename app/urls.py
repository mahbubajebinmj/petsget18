
from django.urls import path

from . import views

urlpatterns = [
    path('', 'index'),
    #path('log', views.login),
]