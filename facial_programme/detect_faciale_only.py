import cv2 


def display(img):
    cv2.imshow(img)
    cv2.waitKey(1)
def traitement_image(img):
    crop = img[100:480 , 200:550]
    small_frame = cv2.resize(crop, (0, 0), fx=0.25, fy=0.25)#division de la taille par 4 pour gagner en rapidité (mais perte precision)
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)#on convertie en noir et blanc
    return gray
if __name__== "__main__":
    print("Preparation avant la video")
    face_cascade = cv2.CascadeClassifier("lbpcascade_frontalface_improved.xml")
    cap = cv2.VideoCapture(0)
    i=0
    print("Debut")
    while True:
        _, img = cap.read()
        gray = traitement_image(img)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)#on detecte tous les visages
        
        # for (x, y, w, h) in faces:#pour tous les visages detecté
        # cv2.rectangle(
        #     img, (x * 4, y * 4), (4 * x + 4 * w, 4 * y + 4 * h), (255, 0, 0), 2
        # )#on fais un rectangle autour de leur visages
        
        if not isinstance(faces, tuple):#si il y a un visage de detecté (pas un tuple)
            print("Visage humain detecté")

cap.release()