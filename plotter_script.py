import numpy as np
import mpld3
import matplotlib.pyplot as plt
from datetime import datetime
import os
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'sensor_app.settings')

import django
django.setup()

from plotter.models import Plot

plt.style.use('ggplot')

while True:
	
	#load data file
	data = np.loadtxt('/webapps/sensor_app/sensor_app/logged_data.txt', dtype={'names': ['time', 'date', 'temperature', 'humidity'],
			     'formats': ['S10', 'S10', 'f4', 'f4']})

	#convert time data to time objects
	date_time = np.array([])
	for times, dates in zip(data['time'], data['date']):
	    test = datetime.strptime(dates + " " + times, "%d/%m/%Y %H:%M:%S")
	    date_time = np.append(test, date_time)

	plots = ['temperature', 'humidity']
	titles = ['Temperature in celsius', 'Humidity in %']
	for plot, title in zip(plots,titles):
		
		#plot and save to file
		fig = plt.figure(figsize=(8,6))
		ax = fig.add_subplot(111, axisbg='#EEEEEE')
		plt.plot(date_time, data[plot][::-1], linewidth=2, marker='o', )
		plt.xticks(rotation='90')
		plt.title(title)
		mpld3.save_html(fig, plot + '.html')

		#save temperature plot to database
		file = open('/webapps/sensor_app/sensor_app/' + plot + '.html', 'r')
		query = Plot.objects.filter(name=plot)
		query_object = query[0]
		query_object.code = file.read()
		query_object.save()
	
	#sleep for 5 min
	time.sleep(60*5)

