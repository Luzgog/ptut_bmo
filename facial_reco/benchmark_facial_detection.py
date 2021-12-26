from module_faciale_detection import *
vid = "entrainement/video/bastien.mkv"
print("Debut des tests")
cascade_test_sans_division(vid)


#cascade_test_division_4(vid)


#clib_test(vid)


dlib_test(vid)


test_hog(vid)



face_recognition_test_cnn(vid)
#blablabla

face_recognition_test_hog(vid)