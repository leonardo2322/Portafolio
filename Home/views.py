from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request=request,template_name='Base.html')


def perfil(request):
    return render(request,'Perfil.html')


# class Perfil_view(ListView):
#     model = Model
#     template_name = ".html"
# )