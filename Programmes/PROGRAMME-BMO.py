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
import pickle
import ST7789
#--------------------
# ------------------------------------------
#variables:
print("initialisation des variables")
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#variable systeme emotion
##c = threading.Condition()
##facial = facial_reco.Facial_reco(c)
MOUVEMENT = 0
meteo = 0
ville = "Marseille"
url_weather = "http://api.openweathermap.org/data/2.5/weather?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095"
with open("configuration_bmo", "rb") as f:
    Activer_Meteo, Activer_Emo_Meteo, Activer_Facial = pickle.load(f)
height =240
width = 240
frameG = 0
frameD = 0

ecranD = ST7789.ST7789(
        height= 240, #hauteur de l'ecran
        rotation= 180, #rotation de 180 de l'ecran
        port=0,
        cs=ST7789.BG_SPI_CS_BACK, #choix de la broche esclave de l'ecran (ST7789.BG_SPI_CS_BACK = pin CE1)
        dc=9, #choix de la pin data control
        backlight=19, #choix de la pin du controle de l'eclairage
        spi_speed_hz=80 * 1000 * 1000, #vitesse du spi
        offset_left= 40, #decalage avec la gauche
        offset_top= 0 #decalage avec le top
)

ecranG = ST7789.ST7789(
        height= 240, #hauteur de l'ecran
        rotation= 0, #rotation de 180 de l'ecran
        port=0,
        cs=ST7789.BG_SPI_CS_FRONT, #choix de la broche esclave de l'ecran (ST7789.BG_SPI_CS_BACK = pin CE0)
        dc=9,#choix de la pin data control
        backlight=19,#choix de la pin du controle de l'eclairage
        spi_speed_hz=80 * 1000 * 1000, #vitesse du spi
        offset_left= 40, #decalage avec la gauche
        offset_top= 0 #decalage avec le top
)# Initialize display.
ecranD.begin() #on d??mare chaque ecran logicielement parlant
ecranG.begin() #on d??mare chaque ecran logicielement parlant
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

app = Flask(__name__, template_folder = "static")
chaleur = 0
battery = 100
etats = 0
humeure = 0
recharge = 0
name = "Unknown"


visage_detect_running = True
#--------------------------------------------------------------
imageD = Image.open("../affichage/"+"Oeil1.png")
imageG = Image.open("../affichage/"+"Oeil1.png")

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
@app.route("/parametre")
def parametre():
    return render_template("parametre.html")

@app.route("/encodage", methods=["GET" , 'POST'])
def post():
    if request.method == "POST":
        file = request.files["img"]
        npimg = np.frombuffer(file.read(), np.uint8)#on transforme le file qu'on a recu en chaine de int
        decode = cv2.imdecode(npimg, cv2.IMREAD_COLOR)#on decode ca en image
        dst = cv2.cvtColor(decode, cv2.COLOR_BGR2RGB)#on transforme l'image BGR en RGB
        img = Image.fromarray(dst.astype("uint8"))#on load l'image avec le module Pillow
        encoding = face_recognition.face_encodings(np.array(img))
        if len(encoding)!=0:
            img.save(f"static/img_dl/{request.form['Nom']}.jpeg")
            facial.known_face_encodings.append(encoding[0])
            facial.known_face_names.append(request.form["Nom"])

            return render_template("encodage.html",msg ="Success", images = os.listdir("static/img_dl/"))
        else:
            return render_template("encodage.html",msg ="Visage non detect??", images = os.listdir("static/img_dl/"))

    else:
        return render_template("encodage.html", images = os.listdir("static/img_dl/"))

#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#--------------------------------------------------------------
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#fonction web page parametre
    
@app.route("/button",methods = ["POST"])#si on va sur /button on
def bouton():
    
    global Activer_Meteo, Activer_Emo_Meteo, Activer_Facial
    print(request.get_json())    
    bouton_appuyer = request.get_json()
    if bouton_appuyer == "Meteo":
        if Activer_Meteo == "D??sactiver":   
            Activer_Meteo = "Activer"
        else: 
            Activer_Meteo = "D??sactiver"

    if bouton_appuyer == "Emo_meteo":
        if Activer_Emo_Meteo == "D??sactiver":   
            Activer_Emo_Meteo = "Activer"
        else: 
            Activer_Emo_Meteo = "D??sactiver"

    if bouton_appuyer == "Reco_facial":
        if Activer_Facial == "D??sactiver":   
            Activer_Facial = "Activer"
        else: 
            Activer_Facial = "D??sactiver"
    if bouton_appuyer == "SHUTDOWN":
        print("Shutting Down")
        emotion = {"error": (Image.open("../affichage/shutdown.gif"), Image.open("../affichage/shutdown.gif"))}
        imageD, imageG = emotion["error"]
        ecranD.display(imageD.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
        ecranG.display(imageG.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
        os.system("sudo shutdown -h now")
    
    if bouton_appuyer == "Avancer":
        print("Avancer")
        MOUVEMENT = 1
    if bouton_appuyer == "Reculer":
        print("Reculer")
        MOUVEMENT = 2          
    if bouton_appuyer == "SlideG":
        print("SlideG")
        MOUVEMENT = 3
    if bouton_appuyer == "SlideD":
        print("SlideD")
        MOUVEMENT = 4
    if bouton_appuyer == "TourneG":
        print("TourneG")
        MOUVEMENT = 5
    if bouton_appuyer == "TourneD":
        print("TourneD")
        MOUVEMENT = 6
    if bouton_appuyer == "Stop":
        print("Stop")
        MOUVEMENT = 7
##########################################################################
    if bouton_appuyer == "Heureux":
        joie()
    if bouton_appuyer == "Triste":
        triste()
    if bouton_appuyer == "Fatigue":
        fatigue()
    if bouton_appuyer == "Dodo":
        dodo()
    if bouton_appuyer == "Joueur":
        joueur()
    if bouton_appuyer == "Amour":
        amour() 
##########################################################################        
    
    with open("configuration_bmo", "wb") as f:
        pickle.dump((Activer_Meteo, Activer_Emo_Meteo, Activer_Facial) , f)
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
#fonctions WEB qui gere les variables en temps r??el

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
        etats = "allum??"
        #humeure = emotion #emotion str(meteo)
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
    if aleatoire > (Chance_Joueur + Chance_Amoureu) and aleatoire <= (Chance_Joueur + Chance_Amoureu + Chance_Joie):
        joie()
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo      
def triste():
    global imageD
    global imageG
    #yeux triste
    global emotion
    emotion = {"triste": (Image.open("../affichage/triste_D.png"), Image.open("../affichage/triste_G.png"))}
    print("triste")
    imageD, imageG = emotion["triste"]
    ecranD.display(imageD.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    ecranG.display(imageG.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
def fatigue():
    global emotion
    global imageD
    global imageG
    #yeux fatiguer
    emotion = {"fatigue": (Image.open("../affichage/etourdi_D.png"), Image.open("../affichage/etourdi_G.png"))}
    print("fatigue")
    imageD, imageG = emotion["fatigue"]
    ecranD.display(imageD.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    ecranG.display(imageG.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    
    
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo  
def dodo():
    global emotion
    global imageD
    global imageG
    #yeux dodo
    emotion = {"endormie": (Image.open("../affichage/dodo_D.png"), Image.open("../affichage/dodo_G.png"))}
    print("dodo")
    imageD, imageG = emotion["endormie"]
    ecranD.display(imageD.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    ecranG.display(imageG.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    
        
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo 
def joueur():
    global emotion
    global imageD
    global imageG
    #yeux dodo
    emotion = {"joueur": (Image.open("../affichage/content.png"), Image.open("../affichage/content.png"))}
    print("joueur")
    imageD, imageG = emotion["joueur"]
    ecranD.display(imageD.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    ecranG.display(imageG.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
  
    
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo 
def amour():
    global emotion
    global imageD
    global imageG 
    #yeux dodo
    emotion = {"amour": (Image.open("../affichage/coeur.png"),Image.open("../affichage/coeur.png"))}
    print("amour")
    imageD, imageG = emotion["amour"]
    ecranD.display(imageD.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    ecranG.display(imageG.resize((width, height))) #on prend l'image et on la resize a la taille de l'ecran
    
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo 
def joie():
    global emotion
    global imageD
    global imageG 
    #yeux joie
    emotion = {"joie": (Image.open("../affichage/joie.png"), Image.open("../affichage/joie.png"))}
    print("joie")
    imageD, imageG = emotion["joie"]
    ecranD.display(imageD.resize((width, height))) #on prend le gif et on le resize a la taille de l'ecran
    ecranG.display(imageG.resize((width, height))) #on prend le gif et on le resize a la taille de l'ecran
    
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo     
#--------------------------------------------------------------

def Humeur_BMO():
    global totalH
    global Chance_Joueur
    global Chance_Amoureu
    global Chance_Joie
    time.sleep(10)

#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    
    while True:
             
        if battery > 5:
            #ajustement des plages de chance d'avoir chaque emotions via les differents facteurs
            Chance_Joueur = 20
            Chance_Amoureu = 5
            Chance_Joie = 1

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
            
            totalH = (Chance_Joueur + Chance_Amoureu + Chance_Joie)
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
        time.sleep(secrets.randbelow(1200) + 600)
#--------------------------------------------------------------
#--------------------------------------------------------------
#--------------------------------------------------------------

def meteo_api():
    global Activer_Meteo
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
#------------------------------------Humeur_BMO----------------
#--------------------------------------------------------------
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo 
def Move():
    aleatoire = secrets.randbelow(6)  
       
    print("deplacement")
    
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo 

def quand_visage_detect??():
    global name
    while visage_detect_running:
        c.acquire()
        c.wait()
        retour_facial(facial_reco.name)
        c.release()

def retour_facial(nom):
    global imageD
    global imageG
    gif = False
    path = "../affichage/"
    if "bastien" in nom:
        imageD = Image.open(path+"PTDR.gif")
        imageG = Image.open(path+"PTDR.gif") 
        gif=True
    elif "nino" in nom:
        imageD = Image.open(path+"PTDR.gif")
        imageG = Image.open(path+"PTDR.gif")
        gif=True
    elif "dimitri" in nom:
        imageD = Image.open(path+"coeur.png")
        imageG = Image.open(path+"coeur.png")
        gif=False
    elif "maxime" in nom:
        imageD = Image.open(path+"optique.gif")
        imageG = Image.open(path+"optique.gif")
        gif=True
    elif "matteo" in nom:
        imageD = Image.open(path+"PTDR.gif")
        imageG = Image.open(path+"PTDR.gif")
        gif=True
    else:
        imageD = Image.open(path+"Oeil1.png")
        imageG = Image.open(path+"Oeil1.png")
        gif=False
    
    if gif:
        try:

            frameG = 0
            frameD = 0
            # print(frameG)
            # print(frameD)
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
    else:
        ecranD.display(imageD.resize((width, height))) #on prend le gif et on le resize a la taille de l'ecran
        ecranG.display(imageG.resize((width, height))) #on prend le gif et on le resize a la taille de l'ecran
    


#Initialisation
if __name__ == "__main__":
    
    pygame.mixer.init()
    #oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    #son de d??marage
    demarage = pygame.mixer.Sound('../son/boot.wav')
    demarage.set_volume(1.0)
    demarage.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    #oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    threadWEB = threading.Thread(target=WEB)
    threadEMO = threading.Thread(target=Humeur_BMO)
    threadMove = threading.Thread(target=Move)
    ##threadVisage = threading.Thread(target=quand_visage_detect??)
    threadEMO.start()
    threadWEB.start()
    threadMove.start()
    ##facial.start()
    ##threadVisage.start()
    app.run(host='0.0.0.0')

# --------------------------------------------------------------
#boucle

#--------------------------------------------------------------

#______________________________________________________________
#probleme qui peuvent arriver :

#______________________________________________________________

#--------------------------------------------------------------
