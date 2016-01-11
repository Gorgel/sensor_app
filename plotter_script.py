import numpy as np
import mpld3
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('ggplot')

data = np.loadtxt('logged_data.txt', dtype={'names': ['time', 'date', 'temperature', 'humidity'],
                     'formats': ['S10', 'S10', 'f4', 'f4']})

date_time = np.array([])
for time, date in zip(data['time'], data['date']):
    test = datetime.strptime(date + " " + time, "%d/%m/%Y %H:%M:%S")
    date_time = np.append(test, date_time)

fig = plt.figure(figsize=(10,6))

ax = fig.add_subplot(111, axisbg='#EEEEEE')

plt.plot(date_time, data['temperature'], linewidth=2, marker='o', )
plt.xticks(rotation='90')
plt.title('Temperatur i Celcius')
mpld3.save_html(fig, 'temp_total.html')
