import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=5)

while True:
    read_data = ser.readlines()

    if read_data:
        temperature = read_data[0].strip("\n")
        humidity = read_data[1].strip("\n")
        current_time = time.strftime("%d/%m/%Y")
        current_date = time.strftime("%H:%M:%S")

        with open('logged_data.txt', 'a') as the_file:
            the_file.write(current_date + " "
                           + current_time + " "
                           + str(temperature)
                           + " " + str(humidity) + "\n")
