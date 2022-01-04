import cv2
import face_recognition
import numpy as np



face_cascade = cv2.CascadeClassifier("data/lbpcascades/lbpcascade_frontalface_improved.xml")
# nino_image = face_recognition.load_image_file("entrainement/nino/nino-6.jpeg")
# nino_face_encoding = face_recognition.face_encodings(nino_image)[0]

# Load a second sample picture and learn how to recognize it.
bastien_image = face_recognition.load_image_file("image_simple/bastienavec.jpeg")
bastien_face_encoding = face_recognition.face_encodings(bastien_image)[0]

# dimitri_image = face_recognition.load_image_file("entrainement/dimitri/dimitri-5.jpeg")
# dimitri_face_encoding = face_recognition.face_encodings(dimitri_image)[0]

max_image = face_recognition.load_image_file("image_simple/maxavec.jpeg")
max_face_encoding = face_recognition.face_encodings(max_image)[0]
# print(max_face_encoding)
# matteo_image = face_recognition.load_image_file("image_simple/matteoavec2.jpeg")
# # print(face_recognition.face_encodings(matteo_image))
# matteo_face_encoding = face_recognition.face_encodings(matteo_image)[0]
# Create arrays of known face encodings and their names
known_face_encodings = [
    # nino_face_encoding,
    bastien_face_encoding,
    max_face_encoding,
    # matteo_face_encoding,
    # dimitri_face_encoding
]
known_face_names = [
    # "Nino",
    "Bastien",
    "Maxime",
    # "Matteo",
    # "Dimitri"
]
def display(img):
    cv2.imshow("image", img)
    cv2.waitKey(1) # si on appuie dans la miliseconde sur c ca quitte tout

def faire_rectangle(liste_visage, img):
    for (x, y, w, h) in faces:#pour tous les visages detecté
        cv2.rectangle(
            img, (x * 4, y * 4), (4 * x + 4 * w, 4 * y + 4 * h), (255, 0, 0), 2
        )#on fais un rectangle autour de leur visages
    
    

# on capture depuis l'unique camera : /dev/video0
cap = cv2.VideoCapture(3)

_, img = cap.read()
face_locations = []
face_encodings = []
face_names = []
print("Debut")
while True:
    _, img = cap.read()  # on lit l'image
    #on la convertie en noir et blanc car les algo ne prennent que du noir et blanc
    small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    # on divise par 4 la taille de l'image pour avoir moins de calcul et plus d'images par secondes
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # for face in faces:
        #faire_rectangle(faces, img)
        # display(img)
    # if not isinstance(faces, tuple):
    #on demarre la reoc faciale
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        print(name +"\n")
    for (top, right, bottom, left), name in zip(face_locations, face_names):
    # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

# Display the resulting image
    cv2.imshow('Video', img)

# Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # else:
    #     print(f"Erreur {faces}")
        
    
cap.release()
