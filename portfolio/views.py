from django.shortcuts import render
from .models import proyecto
from blog.models import Post
# Create your views here.

def inicio(request):
    proyectos = proyecto.objects.all()
    return render(request, 'home.html', {"proyectos": proyectos})