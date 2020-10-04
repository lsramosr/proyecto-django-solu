from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Producto

# Create your views here.
from django.http import HttpResponse

def home(request):
  return HttpResponse("Hola Mundo. Te encuentras en la página de inicio del Linio Express")

class ProductListView(ListView):
    model = Producto
    
class ProductDetailView(DetailView):
    model = Producto