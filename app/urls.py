
from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    #path('', views.index),
    path('log', views.login),
    
    
=======
    path('', 'index'),
    #path('log', views.login),
>>>>>>> 1baf8065ac4f3616ce0644d08045d47b515619ff
]