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
battery = 100
etats = 0
humeure = 0
recharge = 0
emotion = "aucune"
ville = "Marseille"
totalH = 0
meteo = 0
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
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
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
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo        
        
def heureux():
    #yeux heureux
    
    aleatoire = secrets.randbelow(totalH)                
    if aleatoire > 0 and aleatoire < Ejoueur:
        joueur()
    if aleatoire > Ejoueur and aleatoire < (Ejoueur + Eamour):
        amour()
    if aleatoire > (Ejoueur + Eamour) and aleatoire < (Ejoueur + Eamour + Eerror):
        error()
    emotion = "heureux"
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo        
def triste():
    #yeux triste
    emotion = "triste"
    print("triste")
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo     
def fatigue():
    #yeux fatiguer
    emotion = "fatigue"
    print("fatigue")
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
def dodo():   
    #yeux dodo
    emotion = "endormie"
    print("dodo")    
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo 
def joueur():   
    #yeux dodo
    emotion = "joueur"
    print("joueur")
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
def amour():   
    #yeux dodo
    emotion = "amour"
    print("amour")
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo 
def error():   
    #yeux dodo
    emotion = "error"
    print("error")
       
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
def humeureu():
    global totalH
    global Ejoueur
    global Eamour
    global Eerror
    while True:    
        Ejoueur = 20
        Eamour = 5
        Eerror = 1

        Eheureux = 100
        Etriste = 30
        Efatigue = 100 - battery

        totalH = (Ejoueur + Eamour + Eerror)
        total = (Eheureux + Etriste + Efatigue)
        aleatoire = secrets.randbelow(total)

    #oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo  
        #ajustement des plages de chance d'avoir chaque emotions via les differents facteurs

        # Clear Sky = + 40 heureux
        if format(meteo) == "clear sky":
            Eheureux = Eheureux + 40


        # light rain = -20 heureux + 10 triste
        if format(meteo) == "light rain":
            Eheureux = Eheureux - 20
            Etriste = Etriste + 10

        # moderate rain = -20 heureux + 40 triste
        if format(meteo) == "moderate rain":
            Eheureux = Eheureux - 20
            Etriste = Etriste + 40    

        # heavy intensity rain = -40 heureux + 80 triste
        if format(meteo) == "heavy intensity rain":
            Eheureux = Eheureux - 40
            Etriste = Etriste + 80


        # few cloud = -20 heureux + 10 triste
        if format(meteo) == "few cloud":
            Eheureux = Eheureux - 20
            Etriste = Etriste + 10

        # Scattered cloud = -30 heureux + 10 triste
        if format(meteo) == "scattered clouds":
            print("caca")
            Eheureux = Eheureux - 30
            Etriste = Etriste + 10

        # broken cloud = -40 heureux + 20 triste
        if format(meteo) == "broken cloud":
            Eheureux = Eheureux - 40
            Etriste = Etriste + 20

        # overcast cloud = -60 heureux + 30 triste
        if format(meteo) == "overcast cloud":
            Eheureux = Eheureux - 60
            Etriste = Etriste + 30


        # light snow = + 20 heureux
        if format(meteo) == "light snow":
            Eheureux = Eheureux + 20

        # snow = + 40 heureux + 10 fatigue
        if format(meteo) == "snow":
            Eheureux = Eheureux + 40
            Efatigue = Efatigue + 10

    #oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    

        if battery > 5: 
            if aleatoire > 0 and aleatoire < Eheureux:
                heureux()
            if aleatoire > Eheureux and aleatoire < (Eheureux + Etriste):
                triste()
            if aleatoire > (Eheureux + Etriste) and aleatoire < (Eheureux + Etriste + Efatigue):
                fatigue()

    #oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        else:
            dodo()    
            print (Eheureux)
            print (Etriste)
            print (Efatigue)
            print (format(meteo))     
            time.sleep(secrets.randbelow(20) + 10)
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo        
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
    #oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    threadWEB = threading.Thread(target=WEB)
    threadEMO = threading.Thread(target=humeureu)
    threadEMO.start()
    threadWEB.start()
    app.run(host='0.0.0.0')

#--------------------------------------------------------------
#boucle

#--------------------------------------------------------------

#______________________________________________________________
#probleme qui peuvent arriver :

#______________________________________________________________

#--------------------------------------------------------------
