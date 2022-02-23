#PROGRAMME BMO

#--------------------------------------------------------------
#libraries :
print("initialisation des libraries")
from flask import Flask, render_template, jsonify, request
from gpiozero import CPUTemperature
from PIL import Image
import smbus2 as smbus
import time, threading
import secrets
import os
import pygame
import requests
import json
import facial_reco
#--------------------------------------------------------------
#variables:
print("initialisation des variables")
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#variable systeme emotion
meteo = 0
ville = "Marseille"
url_weather = "http://api.openweathermap.org/data/2.5/weather?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095"

#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#variable i2c arduino raspberry

addr = 0x8 # addr de l'arduino(i2c)
#arduinobus = smbus.SMBus(1) # creation du bus i2c   
recu = 0

#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#variable systeme emotion

emotion = "aucune"
totalH = 0

#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#variable web

app = Flask(__name__, template_folder = "static/")
Activer_Meteo = "Activer"
Activer_Emo_Meteo = "Activer"
Activer_Facial = "Activer"
chaleur = 0
battery = 100
etats = 0
humeure = 0
recharge = 0
name = "Unknown"
c = threading.Condition()

visage_detect_running = True
#--------------------------------------------------------------
#--------------------------------------------------------------
#--------------------------------------------------------------
#fonctions WEB ,interactive javascript ,python ,html
#fonction tableau d'infos

print("initialisation des fonctions")
@app.route("/")
def index():
    return render_template("index.html")
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
@app.route("/temperature")#si on va sur /message on retourne le json { "message": "nouvelle valeur"}
def tempera():
    global chaleur #variable python pour changer 
    return jsonify(TEMPE = chaleur)
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
@app.route("/batterie")#si on va sur /message on retourne le json { "message": "nouvelle valeur"}
def batter():
    global battery
    return jsonify(BATTE = battery)
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
@app.route("/etats")#si on va sur /message on retourne le json { "message": "nouvelle valeur"}
def etat():
    global etats
    return jsonify(STATS = etats)
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
@app.route("/humeurs")#si on va sur /message on retourne le json { "message": "nouvelle valeur"}
def humeur():
    global humeure
    return jsonify(HUMER = humeure)
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#--------------------------------------------------------------
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#fonction web page parametre
    
@app.route("/button",methods = ["POST"])#si on va sur /button on
def bouton():
    global Activer_Meteo
    global Activer_Emo_Meteo
    global Activer_Facial
    
    print(request.get_json())    
    bouton_appuyer = request.get_json()
    if bouton_appuyer == "Meteo":
        if Activer_Meteo == "Désactiver":   
            Activer_Meteo = "Activer"
        else: 
            Activer_Meteo = "Désactiver"

    if bouton_appuyer == "Emo_meteo":
        if Activer_Emo_Meteo == "Désactiver":   
            Activer_Emo_Meteo = "Activer"
        else: 
            Activer_Emo_Meteo = "Désactiver"

    if bouton_appuyer == "Reco_facial":
        if Activer_Facial == "Désactiver":   
            Activer_Facial = "Activer"
        else: 
            Activer_Facial = "Désactiver"
    if bouton_appuyer == "SHUTDOWN":
        print("Shutting Down")
        os.system("sudo shutdown -h now")            

    return "JE SAIS PAS QUOI RETURN MDR"
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
@app.route("/PARAMETRE_METEO")#si on va sur /message on retourne le json { "message": "nouvelle valeur"}
def PARAMETRE_METEO():
    global Valeur_PARAMETRE_METEO
    return jsonify(Valeur_PARAMETRE_METEO = Activer_Meteo)
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
@app.route("/PARAMETRE_EMO_METEO")#si on va sur /message on retourne le json { "message": "nouvelle valeur"}
def PARAMETRE_EMO_METEO():
    global Valeur_PARAMETRE_EMO_METEO
    return jsonify(Valeur_PARAMETRE_EMO_METEO = Activer_Emo_Meteo)
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
@app.route("/PARAMETRE_RECO_FACIAL")#si on va sur /message on retourne le json { "message": "nouvelle valeur"}
def PARAMETRE_RECO_FACIAL():
    global Valeur_PARAMETRE_RECO_FACIAL
    return jsonify(Valeur_PARAMETRE_RECO_FACIAL = Activer_Facial)
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
#--------------------------------------------------------------
#fonctions WEB qui gere les variables en temps réel

def WEB():
    
    global battery
    global chaleur
    global etats
    global humeure
    global emotion
    
    while True:
        chaleur = CPUTemperature().temperature
        meteo_api()
        #arduinobus.tristewrite_byte(addr, 101)
        #time.sleep(0.5)
        #battery = arduinobus.read_byte(addr)
        etats = "allumé"
        humeure = emotion #emotion str(meteo)
        time.sleep(1)


#--------------------------------------------------------------    
#--------------------------------------------------------------
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
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo      
def triste():
    #yeux triste
    global emotion
    emotion = {"triste": (Image.open("triste_D.png"), Image.open("triste_G.png"))}
    print("triste")
    imgeD, imageG = emotion["triste"]
    ecranD.display(imageD.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    ecranG.display(imageG.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
def fatigue():
    global emotion
    #yeux fatiguer
    emotion = {"fatigue": (Image.open("etourdi_D.png"), Image.open("etourdi_G.png"))}
    print("fatigue")
    imgeD, imageG = emotion["fatigue"]
    ecranD.display(imageD.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    ecranG.display(imageG.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    
    
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo  
def dodo():
    global emotion   
    #yeux dodo
    emotion = {"endormie": (Image.open("dodo_D.png"), Image.open("dodo_G.png"))}
    print("dodo")
    imgeD, imageG = emotion["endormie"]
    ecranD.display(imageD.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    ecranG.display(imageG.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    
        
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo 
def joueur():
    global emotion
    #yeux dodo
    emotion = {"joueur": (Image.open("Oeil1.png"), Image.open("Oeil1.png"))}
    print("joueur")
    imgeD, imageG = emotion["joueur"]
    ecranD.display(imageD.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    ecranG.display(imageG.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
  
    
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo 
def amour():
    global emotion   
    #yeux dodo
    emotion = "amour"
    print("amour")
    imgeD, imageG = emotion["amour"]
    ecranD.display(imageD.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    ecranG.display(imageG.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo 
def error():
    global emotion   
    #yeux dodo
    emotion = {"error": (Image.open("Shutdown.gif"))}
    print("error")
    imgeD, imageG = emotion["error"]
    frameG = 0
    frameD = 0
    # Boucle pour les gifs
    X=0
    while X<2:
        try:
            print(frameG)
            print(frameD)
            imageG.seek(frameG) #on enregistre le nombre de frame dans le gif et on enregistre ce nombre dans frame
            imageD.seek(frameD) #on enregistre le nombre de frame dans le gif et on enregistre ce nombre dans frame
        
            ecranD.display(imageD.resize((width, height))) #on prend le gif et on le resize a la taille de l'ecran
            ecranG.display(imageG.resize((width, height))) #on prend le gif et on le resize a la taille de l'ecran
        
            frameG += 1 #on avance d'une frame
            frameD += 1
            time.sleep(0.02)

        except EOFError: #quand on arrive a la fin du gif alors sa reset les frames pour retourner au debut du fichier
            frameD = 0
            frameG = 0
            X=X+1
        
        except KeyboardInterrupt:
            exit()

    
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo     
#--------------------------------------------------------------

def Humeur_BMO():
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
#--------------------------------------------------------------
#--------------------------------------------------------------

def meteo_api():
    global temperature
    global meteo
    if Activer_Meteo == True:
        r_weather = requests.get(url_weather)
        data = r_weather.json()
        temperature = data['main']['temp'] # .str(temperature)
        meteo = data['weather'][0]['description'] # .str(meteo)
    else:
        temperature = "NON ACTIVER"
        meteo = "NON ACTIVER"
        
#--------------------------------------------------------------    
#--------------------------------------------------------------
#--------------------------------------------------------------

def quand_visage_detecté():
    global name
    while visage_detect_running:
        c.acquire()
        c.wait()
        print(facial_reco.name)
        c.release()



#Initialisation
if __name__ == "__main__":
    
    facial = facial_reco(c)
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
    threadEMO = threading.Thread(target=Humeur_BMO)
    threadEMO.start()
    threadWEB.start()
    facial.start()
    app.run(host='10.3.141.1')

#--------------------------------------------------------------
#boucle

#--------------------------------------------------------------

#______________________________________________________________
#probleme qui peuvent arriver :

#______________________________________________________________

#--------------------------------------------------------------
