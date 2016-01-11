from django.shortcuts import render
from django.http import HttpResponse
from plotter.models import Plot

def index(request):

    plots = Plot.objects.all()
    context = {'plots' : plots}

    return render(request, 'index.html', context)
