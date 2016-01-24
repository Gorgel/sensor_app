import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

while True:
    read_data = ser.readlines()

    if read_data:
        temperature = read_data[0].strip("\n")
        humidity = read_data[1].strip("\n")
        current_time = time.strftime("%d/%m/%Y")
        current_date = time.strftime("%H:%M:%S")

        with open('/webapps/sensor_app/sensor_app/logged_data.txt', 'a') as the_file:
            the_file.write(current_date + " "
                           + current_time + " "
                           + str(temperature)
                           + " " + str(humidity) + "\n")
