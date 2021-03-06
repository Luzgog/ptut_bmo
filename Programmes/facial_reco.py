import face_recognition
import cv2
import numpy as np
import pickle
import time
import threading
import sys
import os
import re
class VideoCapture:#lance un thread qui ne fait que capturer les images de la cam
    def __init__(self, name):

        self.cap = cv2.VideoCapture(name)#on initialise une capture Opencv d'index name 
        _, frame = self.cap.read()#on prend la premiere frame
        self.frame=frame
        self.running = True
        self.lock = threading.Lock()#on initialise un lock qui va gerer la variable frame pour qu'un seul thread y accede a la fois
        self.t = threading.Thread(target=self._reader)
        self.t.daemon = True
        self.t.start()#on lance le frame reader

    def _reader(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                break
            self.lock.acquire()#permet d'etre thread safe
            self.frame = frame#on ne garde que la derniere thread
            self.lock.release()

    def read(self):
        self.lock.acquire()
        f = self.frame
        self.lock.release()
        return f
    def release(self):
        self.running=False
        self.cap.release()



class Facial_reco:
    def __init__(self, condition_object ,index_capture =0, resize = 0.25 ):
        self.process = False
        self.t = threading.Thread(target=self.detect)#on prepare un thread de detection
        self.video_capture = VideoCapture(index_capture)#on lance une video capture
        self.known_face_encodings , self.known_face_names = self.encodage_dl()#on encode les images deja existante
        self.known_face_encodings_array = np.array(self.known_face_encodings)
        self.face_cascade = cv2.CascadeClassifier("../facial_programme/lbpcascade_frontalface_improved.xml")#on prepare le cascade classifier
        self.face_encoding = []
        self.resize = resize
        
    def detect(self):
        while self.process:
            self.detection()
    def start(self):
        self.process =True
        if not self.t.is_alive():
            self.t.start()
    def stop(self):
        self.process =False
        self.video_capture.release()
    def detection(self):
        global name
        frame = self.video_capture.read()#on choppe la derniere frame 
        gray, img = self.traitement_image(frame, self.resize)# on traite l'image
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)#on detecte les visages presents
        if not isinstance(faces, tuple):#si on detecte un visage
            convert = self.convert_opencv_to_face_recognition(faces)#on conveti les coordonn??e du carr?? contenant le visage pour face_recognition
            # print(convert)
            rgb_small_frame = img[:, :, ::-1]#on converti le BGR en RGB
            self.face_encoding = face_recognition.face_encodings(rgb_small_frame, known_face_locations=convert)#on encode le visage detect??
            # print(face_encoding)
            # print(type(face_encoding))
            # print(type(known_face_encodings))
            matches = face_recognition.compare_faces(self.known_face_encodings_array , np.array(self.face_encoding))# on compare les encodages
            condition_object.acquire()
            name = "Unknown"
            if True in matches:#si on retrouve un des visages 
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]
                condition_object.notify()#on notify the thread de detection de visage
            condition_object.acquire()
    def encodage_visage_pickle(self):
        with open("encodage", 'rb') as f:#on ouvre le fichier encodage
            known_face_encodings, known_face_names = pickle.load(f)#on reprend les objets qui etait dans le fichier
        return known_face_encodings, known_face_names
    def encodage_dl(self):
        path = "static/img_dl/"
        known_face_encodings = []
        known_face_names = []
        for f in os.listdir(path):
            if f.endswith(".jpeg"):#on liste toutes les images
                img = face_recognition.load_image_file(path+f)#on load l'image
                encoding = face_recognition.face_encodings(img)#on fais son encodage
                if len(encoding) == 0:
                    print(f"erreur pour le fichier {path + f}")
                    continue
                known_face_encodings.append(encoding[0])
                known_face_names.append(f[ : f.index('.jpeg')])

        with open("encodage_dl", 'wb') as f:#on ouvre le fichier en ecriture binaire,
            pickle.dump( (known_face_encodings, known_face_names), f)
        return known_face_names, known_face_encodings
    






    def traitement_image(self,img, resize):  
        #crop = img[100:480 , 200:550]
        small_frame = cv2.resize(img, (0, 0), fx=resize, fy=resize)#division de la taille par 4 pour gagner en rapidit?? (mais perte precision)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#on convertie en noir et blanc
        # return gray, small_frame
        return gray, small_frame

    def convert_opencv_to_face_recognition(self, faces):
        """
        Opencv et face_recognition utilise pas le meme objet pour montrer ou se trouve un visage,
        opencv nous donne 1 point d'un rectangle avec la hauteur et largeur du rectangle tandis que facial_recognition utilise
        les coordonn?? des 2 extremit?? du rectangle
        Cette fonction permet de convertir le mode d'opencv a facial_recogntion car il s'est aver?? que 
        opencv est plus rapide a detecter les visage que facial_recognition
        """
        top = faces[0][1]
        right =  faces[0][0]+faces[0][2]
        bottom = faces[0][1]+faces[0][3]
        left = faces[0][0]
        return [(top, right, bottom, left)]
if __name__ == "__main__":#test
    c = threadingCondition()
    facial_reco = Facial_reco(c , 1)#index 0 pour le pi et 2 pour la webcam brancher a mon ordi
    facial_reco.start()
    time.sleep(10)
    facial_reco.stop()


