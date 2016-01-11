import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'sensor_app.settings')

import django
django.setup()

from plotter.models import Plot

file1 = open('temp_total.html', 'r')

plots = Plot.objects.all()

for plot in plots:
    plot.code = file1.read()
    plot.save()
