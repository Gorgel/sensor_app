from django.shortcuts import render
from django.http import HttpResponse
from plotter.models import Plot

#index page
def index(request):

    #fetch all plots and send them to index template
    plots = Plot.objects.all()
    context = {'plots' : plots}

    return render(request, 'index.html', context)
