from django.urls import path

from .views import *

urlpatterns = [
    path('', mainpage, name='home'),
    path('wind/', wind, name='wind'),
    path('stringed/', stringed, name='stringed'),
    path('drums/', drums, name='drums'),
    path('keyboards/', keyboards, name='keyboards'),
    path('bowed/', bowed, name='bowed'),
]

handler404 = pageNotFound