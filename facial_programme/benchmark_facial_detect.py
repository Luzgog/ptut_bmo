import cv2
import time
import dlib
import face_recognition



def cascade_test_sans_division(vid):
    classifier = [
    "data/haarcascades/haarcascade_frontalface_alt2.xml",
    "data/haarcascades/haarcascade_frontalface_alt_tree.xml",
    "data/haarcascades/haarcascade_frontalface_alt.xml",
    "data/haarcascades/haarcascade_frontalface_default.xml",
    "data/lbpcascades/lbpcascade_frontalface_improved.xml",
    "data/lbpcascades/lbpcascade_frontalface.xml",
    ]
    for c in classifier:
        detect = 0
        print(f"{c} ")
        cap = cv2.VideoCapture(vid)
        if (cap.isOpened()== False):
	        print("Error opening video stream or file")
        face_cascade = cv2.CascadeClassifier(c)
        ret, img = cap.read()
        t = time.perf_counter()
        while cap.isOpened():
            ret, img = cap.read()  # on lit l'image
            #on la convertie en noir et blanc car les algo ne prennent que du noir et blanc
            if ret:
                #f+=1
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # on divise par 4 la taille de l'image pour avoir moins de calcul et plus d'images par secondes
                #small_frame = cv2.resize(gray, (0, 0), fx=0.25, fy=0.25)
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)
                if len(faces) >=1:
                    detect +=1
                #faire_rectangle(faces, img)
            else:
                break
        t1 = time.perf_counter()
        print(f"{c} : {t1-t}, detection : {detect }")
        cap.release()

def dlib_test(vid):
    detect = 0
    print(f"dlib ")
    cap = cv2.VideoCapture(vid)
    if (cap.isOpened()== False):
	    print("Error opening video stream or file")
    cnn_face_detector = dlib.cnn_face_detection_model_v1("data/mmod_human_face_detector.dat")
    ret, img = cap.read()
    t = time.perf_counter()
    while cap.isOpened():
        ret, img = cap.read()  # on lit l'image
        if ret:
            rects = cnn_face_detector(img, 0)
            if len(rects)>=1:
                detect+=1
        else:
            break
    t1 = time.perf_counter()
    print(f"dlib : {t1-t}, detection : {detect }")
    cap.release()

def test_hog(vid):
    detect = 0
    print(f"dlib_hog ")
    cap = cv2.VideoCapture(vid)
    if (cap.isOpened()== False):
	    print("Error opening video stream or file")
    detector = dlib.get_frontal_face_detector()
    ret, img = cap.read()
    t = time.perf_counter()
    while cap.isOpened():
        ret, img = cap.read()  # on lit l'image
        
        if ret:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            rects = detector(gray, 0)
            if len(rects) >=1:
                detect+=1
        else:
            break
    t1 = time.perf_counter()
    print(f"dlib_hog : {t1-t}, detection : {detect }")
    cap.release()  


def face_recognition_test_cnn(vid):
    detect = 0
    cap = cv2.VideoCapture(vid)
    if (cap.isOpened()== False):
	    print("Error opening video stream or file")
    print(f"face_recognition cnn")
    ret, img = cap.read()
    t = time.perf_counter()
    while cap.isOpened():
        ret, img = cap.read()  # on lit l'image
        if ret:
            rects_1 = face_recognition.face_locations(img, 0, "cnn")
        else:
            break
    t1 = time.perf_counter()
    print(f"face_recognition cnn: {t1-t}, detection : {detect }")
    cap.release()     

def face_recognition_test_hog(vid):
    detect = 0
    cap = cv2.VideoCapture(vid)
    if (cap.isOpened()== False):
	    print("Error opening video stream or file")
    print(f"face_recognition hog")
    ret, img = cap.read()
    t = time.perf_counter()
    while cap.isOpened():
        ret, img = cap.read()  # on lit l'image

        if ret:
            rects_1 = face_recognition.face_locations(img, 0, "hog")
        else:
            break

    t1 = time.perf_counter()
    print(f"face_recognition hog: {t1-t}, detection : {detect }")
    cap.release()



vid = "entrainement/video/bastien.mkv"
print("Debut des tests")
cascade_test_sans_division(vid)
dlib_test(vid)
test_hog(vid)
face_recognition_test_cnn(vid)
face_recognition_test_hog(vid)