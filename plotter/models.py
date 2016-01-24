from __future__ import unicode_literals

from django.db import models

# Create your models here.

#class for saving matplotlib plots converted to html
class Plot(models.Model):
    name = models.CharField(max_length=120, blank=True)
    code = models.TextField(max_length = 60000, blank=True)
