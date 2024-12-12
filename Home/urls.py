from django.urls import path

from Home.views import home, perfil

urlpatterns = [
    path('',home),
    path('portafolio/', perfil,name='portafolio')
]