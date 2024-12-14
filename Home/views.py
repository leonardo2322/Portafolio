from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from .models  import Contacto, Proyecto, Reconocimiento, Technologia
# Create your views here.
def home(request):
    return render(request=request,template_name='Base.html')


def perfil(request):
    context = {
        'eliminar_div': True
    }
    return render(request,'Perfil.html',context)


class Proyectos_view(ListView):
    model = Proyecto
    template_name = 'proyectos_temp.html'
    context_object_name = "proyectos"
   

class Reconocimientos_view(ListView):
    model = Reconocimiento
    template_name = 'reconocimientos_temp.html'
    context_object_name = 'reconocimientos'
    

class Technologias_view(ListView):
    model = Technologia
    template_name = 'technologias_temp.html'
    context_object_name = 'technologias'
    paginate_by = 12
    ordering = ['nombre']

class Contacto_view(ListView):
    model = Contacto
    template_name = 'contacto_temp.html'
    context_object_name = 'contactar'



    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["contactos"] = [
            {'contacto':contacto, 'enlace':contacto.enlaces.first()
             }
             for contacto in Contacto.objects.prefetch_related('enlaces')
        ] 
        return context
    