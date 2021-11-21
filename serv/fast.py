from fastapi import FastAPI
import serial

ser = serial.Serial('/dev/serial0', 115200)

app = FastAPI()

K = 0
temp = []
pres = []
scale = 0
angle = 0

@app.get("/")
def welcome():
    return {"welcome":"Welcome to 3ESE API!"}

###TEMPERATURE###
#Afficher les temperatures
@app.get("/api/temp/")
def get_temp():
    return {"temperatures":temp}

#Demander une nouvelle temperature 
@app.post("/api/temp/")
def post_temp():
    global temp
    global ser
    getT() #envoi de l'ordre à la STM32
    resp = ser.readline() #lecture de la réponse
    temp.append(resp) #ajout à la liste des températures
    return {"temperature":resp}

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

#Demander une nouvelle pression 
@app.post("/api/pres/")
def post_pres():
    global pres
    global ser
    getP()
    resp = ser.readline()
    pres.append(resp)
    return {"pression" : resp}

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
#Affiche l'angle (temp*scale) 
#@app.get("/api/angle/")
#def get_angle():
#    global angle
#    return {"angle":angle}

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
    ser.write(K)
    return {"K":K}

###FONCTIONS UART###
#Demander temperature
def getT():
    global ser
    ser.write(b'!GET_T')

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


