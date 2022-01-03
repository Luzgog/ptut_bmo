#PROGRAMME BMO

#--------------------------------------------------------------
#library :
print("initialisation des libraries")
from flask import Flask, render_template, jsonify
from gpiozero import CPUTemperature

from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from PIL import Image

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
#variable i2c arduino raspberry

addr = 0x8 # addr de l'arduino(i2c)
arduinobus = smbus.SMBus(1) # creation du bus i2c
ecranbus = i2c(port=1, address=0x3C)
ecranoled = sh1106(ecranbus)
ecranoled.clear() #on enleve l'image deja existant si il y en a
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
#--------------------------------------------------------------
def WEB():
    
    global battery
    global chaleur
    global etats
    global humeure
    
    while True:
        chaleur = CPUTemperature().temperature
        meteo_api()
        #arduinobus.write_byte(addr, 101)
        #time.sleep(0.5)
        #battery = arduinobus.read_byte(addr)
        etats = "allumé"
        humeure = emotion #format(meteo)
        
        time.sleep(2)
#--------------------------------------------------------------    
        
def heureux():
    #yeux heureux
    
    aleatoire = secrets.randbelow(totalH)                
    if aleatoire > 0 and aleatoire <= Ejoueur:
        joueur()
    if aleatoire > Ejoueur and aleatoire <= (Ejoueur + Eamour):
        amour()
    if aleatoire > (Ejoueur + Eamour) and aleatoire <= (Ejoueur + Eamour + Eerror):
        error()
    emotion = "heureux"
#--------------------------------------------------------------       
def triste():
    #yeux triste
    emotion = "triste"
    print("triste")

    ecranoled.clear() #on enleve l'image deja existant si il y en a
    img = Image.open("BMO/affichage_oled/Oeil_triste.png")
    ecranoled.display(img.convert(ecranoled.mode))
    
#--------------------------------------------------------------     
def fatigue():
    #yeux fatiguer
    emotion = "fatigue"
    print("fatigue")
    
    ecranoled.clear() #on enleve l'image deja existant si il y en a
    img = Image.open("BMO/affichage_oled/Oeil_batterie_faible.png")
    ecranoled.display(img.convert(ecranoled.mode))
    
#--------------------------------------------------------------  
def dodo():   
    #yeux dodo
    emotion = "endormie"
    print("dodo")
    
    ecranoled.clear() #on enleve l'image deja existant si il y en a
    img = Image.open("BMO/affichage_oled/Oeil_endormi.png")
    ecranoled.display(img.convert(ecranoled.mode))
        
#--------------------------------------------------------------
def joueur():   
    #yeux dodo
    emotion = "joueur"
    print("joueur")

    ecranoled.clear() #on enleve l'image deja existant si il y en a
    img = Image.open("BMO/affichage_oled/Oeil_content.png")
    ecranoled.display(img.convert(ecranoled.mode))    
    
#--------------------------------------------------------------
def amour():   
    #yeux dodo
    emotion = "amour"
    print("amour")
#--------------------------------------------------------------
def error():   
    #yeux dodo
    emotion = "error"
    print("error")
#--------------------------------------------------------------       
def humeureu():
    global totalH
    global Ejoueur
    global Eamour
    global Eerror
    time.sleep(10)

#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
    while True:
             
        if battery > 5:
            #ajustement des plages de chance d'avoir chaque emotions via les differents facteurs
            Ejoueur = 20
            Eamour = 5
            Eerror = 1

            Eheureux = 100
            Etriste = 30
            Efatigue = 100 - battery

            totalH = (Ejoueur + Eamour + Eerror)
            total = (Eheureux + Etriste + Efatigue)
            aleatoire = secrets.randbelow(total)
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
            if format(meteo) == "few clouds":
                Eheureux = Eheureux - 20
                Etriste = Etriste + 10

            # Scattered cloud = -30 heureux + 10 triste
            if format(meteo) == "scattered clouds":
                print("caca")
                Eheureux = Eheureux - 30
                Etriste = Etriste + 10

            # broken cloud = -40 heureux + 20 triste
            if format(meteo) == "broken clouds":
                Eheureux = Eheureux - 40
                Etriste = Etriste + 20

            # overcast cloud = -60 heureux + 30 triste
            if format(meteo) == "overcast clouds":
                Eheureux = Eheureux - 60
                Etriste = Etriste + 30


            # light snow = + 20 heureux
            if format(meteo) == "light snow":
                Eheureux = Eheureux + 20

            # snow = + 40 heureux + 10 fatigue
            if format(meteo) == "snow":
                Eheureux = Eheureux + 40
                Efatigue = Efatigue + 10

            if aleatoire > 0 and aleatoire <= Eheureux:
                heureux()
            if aleatoire > Eheureux and aleatoire <= (Eheureux + Etriste):
                triste()
            if aleatoire > (Eheureux + Etriste) and aleatoire <= (Eheureux + Etriste + Efatigue):
                fatigue()
                
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        else:
            dodo()    
        print (Eheureux)
        print (Etriste)
        print (Efatigue)
        print (format(meteo))   
        print (" ")
        time.sleep(secrets.randbelow(20) + 10)
#--------------------------------------------------------------

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
