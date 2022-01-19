import cv2 
import numpy as np
import pickle
import face_recognition
"""
with open("camera_calibre", "rb"):
    ret, mtx, dist, rvecs, tvecs = pickle.load()

def undistort(img, ):
    h,  w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
    return dst
"""
def encodage_visage():
    with open("encodage", 'rb') as f:#on ouvre le fichier encodage
        known_face_encodings, known_face_names = pickle.load(f)#on reprend les objets qui etait dans le fichier
    return known_face_encodings, known_face_names

def display(img):
    cv2.imshow(img)
    cv2.waitKey(1)
def traitement_image(img):  
    #crop = img[100:480 , 200:550]
    small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)#division de la taille par 4 pour gagner en rapidité (mais perte precision)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#on convertie en noir et blanc
    return gray, small_frame
if __name__== "__main__":
    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings, known_face_names = encodage_visage()
    print("Preparation avant la video")
    face_cascade = cv2.CascadeClassifier("lbpcascade_frontalface_improved.xml")
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 0)
    i=0
    print("Debut")
    while True:
        i+=1
        _, img = cap.read()
        gray, img = traitement_image(img)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)#on detecte tous les visages
        
        # for (x, y, w, h) in faces:#pour tous les visages detecté
        # cv2.rectangle(
        #     img, (x * 4, y * 4), (4 * x + 4 * w, 4 * y + 4 * h), (255, 0, 0), 2
        # )#on fais un rectangle autour de leur visages
        
        if not isinstance(faces, tuple):#si il y a un visage de detecté (pas un tuple)
            rgb_small_frame = img[:, :, ::-1]#on converti pour avoir du 
            # rgb a la place du bgr (car utilisé par le module)
            print(f"faces {faces}")
            print(face_recognition.face_locations(rgb_small_frame))
            # face_locations = face_recognition.face_locations(rgb_small_frame)
            face_locations = faces
            # print(face_locations)
            # print(faces)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                
                name = "Unknown"
                
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    print(f"if true {name}")
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    print(f"imatches{name}")
                # top*=4
                # bottom*=4
                # left*=4
                # right*=4
                # Draw a box around the face
                # cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
                print(name)
                # Draw a label with a name below the face
                # cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                # font = cv2.FONT_HERSHEY_DUPLEX
                # cv2.putText(img, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                cv2.imwrite(f"debug/rgb.png", rgb_small_frame)
                cv2.imwrite(f"debug/img.png", img)
        # else:
        #     #cv2.imwrite(f"debug/{i}.png", img)
        #     pass

cap.release()