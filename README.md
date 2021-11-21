# TP_Bus_reseau_Heddoun_aveiro_alves

PINOUT:
CAN1
PB9 -> CAN1_TX
PB8 -> CAN1_RX

I2C3
PC1 -> I2C3_SDA
PC0 -> I2C3_SCL

USART1 (STM32/PC)
PA9 -> USART1_TX
PA10 -> USART1_RX

USART2 (STM32/RaspberryPi)
PA2 -> USART2_TX
PA3 -> USART2_RX

Lien vidéo montrant la communication entre la STM32 et la Raspberry Pi et l'envoi de requêtes HTTP : https://www.youtube.com/watch?v=D7pqz8I-2W0

Prérequis : 
Sur la Raspberry : 
-Python3 avec pip3
-pyserial
-fastapi
-uvicorn
Il y a un fichier requirement dans le dossier "serv" pour installer les librairies avec la commande : pip3 install -r requirement.txt

Commande pour lancer le serveur : uvicorn fast:app --host 0.0.0.0 --port 5000 --reload
