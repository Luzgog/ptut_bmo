import pickle, face_recognition

bastien_avec_image = face_recognition.load_image_file("image_simple/bastienavec.jpeg")
bastien_avec_face_encoding = face_recognition.face_encodings(bastien_avec_image)[0]
matteo_avec_image = face_recognition.load_image_file("image_simple/matteosans2.jpeg")
matteo_avec_face_encoding = face_recognition.face_encodings(matteo_avec_image)[0]
max_avec_image = face_recognition.load_image_file("image_simple/maxavec.jpeg")
max_avec_face_encoding = face_recognition.face_encodings(max_avec_image)[0]
bastien_sans_image = face_recognition.load_image_file("image_simple/bastiensans.jpeg")
bastien_sans_face_encoding = face_recognition.face_encodings(bastien_sans_image)[0]
matteo_sans_image = face_recognition.load_image_file("image_simple/matteosans.jpeg")
matteo_sans_face_encoding = face_recognition.face_encodings(matteo_sans_image)[0]
max_sans_image = face_recognition.load_image_file("image_simple/maxsans.jpeg")
max_sans_face_encoding = face_recognition.face_encodings(max_sans_image)[0]
print("Tous les encodages ont été réalisé")
known_face_encodings = [
    bastien_avec_face_encoding,
    matteo_avec_face_encoding,
    max_avec_face_encoding,
    bastien_sans_face_encoding,
    matteo_sans_face_encoding,
    max_sans_face_encoding
]
known_face_names = [
    "bastien avec",
    "matteo avec",
    "max avec",
    "bastien sans",
    "matteo sans",
    "max sans"
]

with open("encodage", 'wb') as f:#on ouvre le fichier en ecriture binaire,
    pickle.dump( (known_face_encodings, known_face_names), f)#on met dans se fichier le tuple 
#tout ca a permit d'eviter de recalculer l'encodage, ca prend un peu de temps sur le pi 