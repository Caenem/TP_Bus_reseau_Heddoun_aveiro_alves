import serial

ser = serial.Serial('/dev/serial0', 115200)
print("Attente donnes")
ser.write(b'!GET_T') #ordre pour demander la température au STM32
x = ser.readline() #on lit le port série jusqu'à un retour à la ligne
print(x)
ser.close()

