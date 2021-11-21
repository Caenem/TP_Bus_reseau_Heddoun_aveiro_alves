import serial

ser = serial.Serial('/dev/serial0', 115200)
print("Attente donnes")
ser.write(b'!GET_T')
x = ser.readline()
print(x)
ser.close()

