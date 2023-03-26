import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)  # Replace with your port and baud rate

while True:
    line = ser.readline().strip()
    print(line)
