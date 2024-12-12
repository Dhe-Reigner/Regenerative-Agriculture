from django.shortcuts import render
from .models import Generative

# Create your views here.
# def home(request):
#     return render(request, 'Agriculture/home.html')

def home(request):
    generative = Generative.objects.all()
    return render(request, 'home.html', {'generative': generative})