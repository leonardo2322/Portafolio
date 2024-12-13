from django.urls import path

from Home.views import Contacto_view, home, perfil,Proyectos_view, Reconocimientos_view, Technologias_view


urlpatterns = [
    path('',home),
    path('portafolio/', perfil,name='portafolio'),
    path('Proyectos/',Proyectos_view.as_view(), name='Proyectos' ),
    path('reconocimiento/', Reconocimientos_view.as_view(), name='reconocimientos'),
    path('technologias/', Technologias_view.as_view(), name='tech'),
    path('contacto/', Contacto_view.as_view(), name='contacto')
]