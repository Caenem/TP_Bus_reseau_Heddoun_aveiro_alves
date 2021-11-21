from fastapi import FastAPI
import serial

ser = serial.Serial('/dev/serial0', 115200)

app = FastAPI()

welcome = "Welcome to 3e ESE API!"
K = 0
temp = [1]
pres = [1]
scale = 0
angle = 0

@app.get("/")
def welcome():
    return "Hello World!\n"

###TEMPERATURE###
#Afficher les temperatures
@app.get("/api/temp/")
def get_temp():
    return {"temperatures":temp}

#Demander une nouvelle temperature /(a faire)\
@app.post("/api/temp/")
def post_temp():
    getT()
    return "test"

#Affiche la temperature #x
@app.get("/api/temp/{x}")
def get_temp_x(x:int):
    return {"index":x, "temperature":temp[x]}

#Supprime la temperature #x
@app.delete("/api/temp/{x}")
def delete_temp_x(x:int):
    temp.pop(x)
    return {"index_deleted":x}

###PRESSION###
#Affiche les pressions
@app.get("/api/pres/")
def get_pres():
    return {"pressions":pres}

#Demander une nouvelle pression /(a faire)\
@app.post("/api/pres/")
def post_pres():

    return "test"

#Afficher la pression #x
@app.get("/api/pres/{x}")
def get_pres_x(x:int):
    return {"index":x, "pression":pres[x]}

#Supprimer la pression #x
@app.delete("/api/pres/{x}")
def delete_pres_x(x:int):
    pres.pop(x)
    return {"index_deleted":x}

###ANGLE###
#Affiche l'angle (temp*scale) /(a faire)\
@app.get("/api/angle/")
def get_angle():
    return "test"

###SCALE###
#Affiche K
@app.get("/api/scale/")
def get_scale():
    return {"K":K}

#Modifie la valeur de K par #x
@app.post("/api/scale/{x}")
def post_scale_x(x:int):
    global K
    global ser
    K = x
    return {"K":K}

###FONCTIONS UART###
#Demander temperature
def getT():
    global ser
    ser.write(b'!GET_T') //le "b" sert à préciser 
    temp.append(ser.read_until(b'\n'))
    

#Demander pression
def getP():
    global ser
    ser.write(b'!GET_P')

#Demander coefficient K
def getK():
    global ser
    ser.write(b'!GET_K')

#Demander angle
def getA():
    global ser
    ser.write(b'!GET_A')


