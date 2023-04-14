from django.http import HttpResponse
from django.shortcuts import render

from . models import Place
from . models import Team1
# Create your views here.

def demo(request):
    obj = Place.objects.all()
    ob = Team1.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': ob})
  