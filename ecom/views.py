
from django.shortcuts import render
from .models import *

def products(request):
    productss = Labexam.objects.all()
    return render(request, 'products.html', {'productss':productss})