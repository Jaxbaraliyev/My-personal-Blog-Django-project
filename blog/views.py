from django.shortcuts import render, redirect
from .models import *

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

def blog(request):
    all_maqola = Maqolalar.objects.all()
    data = {
        "maqolalar":all_maqola
    }
    return render(request, "blog.html", data)


def maqola(request, pk):
    m = Maqolalar.objects.filter(id=pk)
    data = {
        "maqolalar":m
    }
    return render(request, "maqola.html", data)



