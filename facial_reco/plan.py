import cv2
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#soit haarcascade soit lb=pb
#default 51/30 i/s
#alt 53/30 i/s
#alt2 54/30 i/s
# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
import time 
_, img = cap.read()
i=0
t = time.time()
while True:
    i = face_detect()
    if i:
        for e in i:
            reco_faciale("bastien", e)
            reco_faciale("nino", e)

# Release the VideoCapture object
cap.release()

