import serial
import time

#start serial communication
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

#loop
while True:

    #read serial data to variable
    read_data = ser.readlines()

    #only if there is data
    if read_data:

        #format data
        temperature = read_data[0].strip("\n")
        humidity = read_data[1].strip("\n")

        #create matplotlib time objects and format it
        current_time = time.strftime("%d/%m/%Y")
        current_date = time.strftime("%H:%M:%S")

        #write data to file
        with open('/webapps/sensor_app/sensor_app/logged_data.txt', 'a') as the_file:
            the_file.write(current_date + " "
                           + current_time + " "
                           + str(temperature)
                           + " " + str(humidity) + "\n")
