import face_recognition
import cv2
import numpy as np
import pickle
import time
import threading
import sys
class VideoCapture:#lance un thread qui ne fait que capturer les images de la cam
    def __init__(self, name):

        self.cap = cv2.VideoCapture(name)
        _, frame = self.cap.read()
        self.frame=frame
        self.running = True
        self.lock = threading.Lock()
        self.t = threading.Thread(target=self._reader)
        self.t.daemon = True
        self.t.start()

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
    def __init__(self, condition_object ,index_capture =0, resize = 0.25, ):
        self.process = False
        self.t = threading.Thread(target=self.detect)
        self.video_capture = VideoCapture(index_capture)
        self.known_face_encodings , self.known_face_names = self.encodage_visage()
        self.known_face_encodings = np.array(self.known_face_encodings)
        self.face_cascade = cv2.CascadeClassifier("../facial_programme/lbpcascade_frontalface_improved.xml")
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
        frame = self.video_capture.read()
        gray, img = self.traitement_image(frame, self.resize)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        if not isinstance(faces, tuple):
            convert = self.convert_opencv_to_face_recognition(faces)
            # print(convert)
            rgb_small_frame = img[:, :, ::-1]
            self.face_encoding = face_recognition.face_encodings(rgb_small_frame, known_face_locations=convert)
            # print(face_encoding)
            # print(type(face_encoding))
            # print(type(known_face_encodings))
            matches = face_recognition.compare_faces(self.known_face_encodings, np.array(self.face_encoding))
            condition_object.acquire()
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]
                condition_object.notify()
            condition_object.acquire()
    def encodage_visage(self):
        with open("../facial_programme/encodage", 'rb') as f:#on ouvre le fichier encodage
            known_face_encodings, known_face_names = pickle.load(f)#on reprend les objets qui etait dans le fichier
        return known_face_encodings, known_face_names
    def traitement_image(self,img, resize):  
        #crop = img[100:480 , 200:550]
        small_frame = cv2.resize(img, (0, 0), fx=resize, fy=resize)#division de la taille par 4 pour gagner en rapidité (mais perte precision)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#on convertie en noir et blanc
        # return gray, small_frame
        return gray, small_frame

    def convert_opencv_to_face_recognition(self, faces):
        """
        Opencv et face_recognition utilise pas le meme objet pour montrer ou se trouve un visage,
        opencv nous donne 1 point d'un rectangle avec la hauteur et largeur du rectangle tandis que facial_recognition utilise
        les coeerdonné des 2 extremité du rectangle
        Cette fonction permet de convertir le mode d'opencv a facial_recogntion car il s'est averé que 
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


