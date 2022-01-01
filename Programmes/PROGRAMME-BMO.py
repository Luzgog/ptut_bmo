#PROGRAMME BMO

#--------------------------------------------------------------
#library :
print("initialisation des libraries")
from flask import Flask, render_template, jsonify
from gpiozero import CPUTemperature
import smbus2 as smbus
import time, threading
import secrets
import pygame
import requests
import json

#--------------------------------------------------------------
#variables:

#variable web
print("initialisation des variables")
app = Flask(__name__, template_folder = "static/")
chaleur = 0
battery = 0
etats = 0
humeure = 0
ville = "Marseille"
url_weather = "http://api.openweathermap.org/data/2.5/weather?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095"
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#variable i2c arduino raspberry

addr = 0x8 # addr de l'arduino(i2c)
bus = smbus.SMBus(1) # creation du bus i2c
recu = 0

#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#variable systeme emotion

emotion = 0

#--------------------------------------------------------------
#fonctions
print("initialisation des fonctions")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/temperature")#si on va sur /message on retourne le json { "message": "nouvelle valeur"}
def tempera():
    global chaleur #variable python pour changer 
    return jsonify(TEMPE = chaleur)

@app.route("/batterie")#si on va sur /message on retourne le json { "message": "nouvelle valeur"}
def batter():
    global battery
    return jsonify(BATTE = battery)

@app.route("/etats")#si on va sur /message on retourne le json { "message": "nouvelle valeur"}
def etat():
    global etats
    return jsonify(STATS = etats)

@app.route("/humeurs")#si on va sur /message on retourne le json { "message": "nouvelle valeur"}
def humeur():
    global humeure
    return jsonify(HUMER = humeure)

def WEB():
    
    global battery
    global chaleur
    global etats
    global humeure
    
    while True:
        chaleur = CPUTemperature().temperature
        meteo_api()
        #bus.write_byte(addr, 101)
        #time.sleep(0.5)
        #battery = bus.read_byte(addr)
        etats = secrets.randbelow(100) #le nombre n'est pas compris dans la liste des nombre aleatoire 
        humeure = format(meteo)
        
        
        time.sleep(2)
        
        
def heureux():
    #yeux heureux
    print("heureux")
        
def triste():
    #yeux triste
    print("triste")
     
def fatigue():
    #yeux fatiguer
    print("fatigue")
    
def dodo():   
    #yeux dodo
    print("dodo")    

def humeur():   
    print("oui")
        
def meteo_api():
    
    global temperature
    global meteo
    r_weather = requests.get(url_weather)
    data = r_weather.json()
    temperature = data['main']['temp'] # .format(temperature)
    meteo = data['weather'][0]['description'] # .format(meteo)      
#--------------------------------------------------------------
#Initialisation

#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#site web

if __name__ == "__main__":
    
    pygame.mixer.init()


    #oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    #son de démarage
    demarage = pygame.mixer.Sound('BMO/boot.wav')
    demarage.set_volume(1.0)
    demarage.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    
    threadWEB = threading.Thread(target=WEB)
    threadWEB.start()
    app.run(host='0.0.0.0')

#--------------------------------------------------------------
#boucle

#--------------------------------------------------------------

#______________________________________________________________
#probleme qui peuvent arriver :

#______________________________________________________________

#--------------------------------------------------------------
