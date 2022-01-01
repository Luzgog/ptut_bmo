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

#--------------------------------------------------------------
#variables:

#variable web
print("initialisation des variables")
app = Flask(__name__, template_folder = "static/")
chaleur = 0
battery = 0
etats = 0
humeure = 0

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

def job():
    
    global battery
    global chaleur
    global etats
    global humeure
    
    while True:
        chaleur = CPUTemperature().temperature
        
        #bus.write_byte(addr, 101)
        #time.sleep(0.5)
        #battery = bus.read_byte(addr)
        etats = secrets.randbelow(10) #le nombre n'est pas compris dans la liste des nombre aleatoire 
        humeure+=4
        
        time.sleep(2)
        
#--------------------------------------------------------------
#Initialisation

#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#site web

if __name__ == "__main__":
    
    pygame.mixer.init()


    #oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    #son de démarage
    demarage = pygame.mixer.Sound('boot.wav')
    demarage.set_volume(1.0)
    demarage.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    t = threading.Thread(target=job)
    t.start()
    app.run(host='0.0.0.0')

#--------------------------------------------------------------
#boucle


