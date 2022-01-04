#PROGRAMME BMO

#--------------------------------------------------------------
#libraries :
print("initialisation des libraries")
from flask import Flask, render_template, jsonify
from gpiozero import CPUTemperature

from luma.core.interface.serial import i2c
from luma.oled.device import sh1106 #libraries de l'ecran oled:
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
ecranoled = sh1306(ecranbus)
ecranoled.clear() #on enleve l'image deja existant si il y en a
img = Image.open("BMO/affichage_oled/Oeil_test.png")
ecranoled.display(img.convert(ecranoled.mode))    
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
        humeure = emotion #str(meteo)
        
        time.sleep(2)
#--------------------------------------------------------------    
        
def heureux():
    #yeux heureux
    
    aleatoire = secrets.randbelow(totalH)                
    if aleatoire >= 0 and aleatoire <= Chance_Joueur:
        joueur()
    if aleatoire > Chance_Joueur and aleatoire <= (Chance_Joueur + Chance_Amoureu):
        amour()
    if aleatoire > (Chance_Joueur + Chance_Amoureu) and aleatoire <= (Chance_Joueur + Chance_Amoureu + Chance_Error):
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
    global Chance_Joueur
    global Chance_Amoureu
    global Chance_Error
    time.sleep(10)

#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
    while True:
             
        if battery > 5:
            #ajustement des plages de chance d'avoir chaque emotions via les differents facteurs
            Chance_Joueur = 20
            Chance_Amoureu = 5
            Chance_Error = 1

            Chance_Heureux = 100
            Chance_Triste = 30
            Chance_Fatigue = 100 - battery

            # Clear Sky = + 40 heureux
            if str(meteo) == "clear sky":
                Chance_Heureux = Chance_Heureux + 40


            # light rain = -20 heureux + 10 triste
            if str(meteo) == "light rain":
                Chance_Heureux = Chance_Heureux - 20
                Chance_Triste = Chance_Triste + 10

            # moderate rain = -20 heureux + 40 triste
            if str(meteo) == "moderate rain":
                Chance_Heureux = Chance_Heureux - 20
                Chance_Triste = Chance_Triste + 40    

            # heavy intensity rain = -40 heureux + 80 triste
            if str(meteo) == "heavy intensity rain":
                Chance_Heureux = Chance_Heureux - 40
                Chance_Triste = Chance_Triste + 80


            # few cloud = -20 heureux + 10 triste
            if str(meteo) == "few clouds":
                Chance_Heureux = Chance_Heureux - 20
                Chance_Triste = Chance_Triste + 10

            # Scattered cloud = -30 heureux + 10 triste
            if str(meteo) == "scattered clouds":
                print("caca")
                Chance_Heureux = Chance_Heureux - 30
                Chance_Triste = Chance_Triste + 10

            # broken cloud = -40 heureux + 20 triste
            if str(meteo) == "broken clouds":
                Chance_Heureux = Chance_Heureux - 40
                Chance_Triste = Chance_Triste + 20

            # overcast cloud = -60 heureux + 30 triste
            if str(meteo) == "overcast clouds":
                Chance_Heureux = Chance_Heureux - 60
                Chance_Triste = Chance_Triste + 30


            # light snow = + 20 heureux
            if str(meteo) == "light snow":
                Chance_Heureux = Chance_Heureux + 20

            # snow = + 40 heureux + 10 fatigue
            if str(meteo) == "snow":
                Chance_Heureux = Chance_Heureux + 40
                Chance_Fatigue = Chance_Fatigue + 10
            
            totalH = (Chance_Joueur + Chance_Amoureu + Chance_Error)
            total = (Chance_Heureux + Chance_Triste + Chance_Fatigue)
            aleatoire = secrets.randbelow(total)

            if aleatoire >= 0 and aleatoire <= Chance_Heureux:
                heureux()
            if aleatoire > Chance_Heureux and aleatoire <= (Chance_Heureux + Chance_Triste):
                triste()
            if aleatoire > (Chance_Heureux + Chance_Triste) and aleatoire <= (Chance_Heureux + Chance_Triste + Chance_Fatigue):
                fatigue()
                
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        else:
            dodo()
        print (aleatoire)    
        print (Chance_Heureux)
        print (Chance_Triste)
        print (Chance_Fatigue)
        print (str(meteo))   
        print (" ")
        time.sleep(secrets.randbelow(20) + 10)
#--------------------------------------------------------------

def meteo_api():
    
    global temperature
    global meteo
    r_weather = requests.get(url_weather)
    data = r_weather.json()
    temperature = data['main']['temp'] # .str(temperature)
    meteo = data['weather'][0]['description'] # .str(meteo)
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
