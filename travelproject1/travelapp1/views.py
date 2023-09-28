from django.shortcuts import render

# Create your views here.

from . models import place
from . models import news

from django.shortcuts import render

def fun(request):

    results=place.objects.all()

    return render(request,"index1.html",{'results':results})

def fun1(request):
    results = news.objects.all()
    return render(request, "index1.html",{'results':results})