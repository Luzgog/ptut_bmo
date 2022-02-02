import pickle
import numpy as np
with open("debug/variable", 'rb') as f:
    face_locations, faces = pickle.load(f)
print(type(face_locations))
print(type(face_locations[0]))
print(face_locations[0])
print(type(faces))
print(faces.shape)
print(type(faces[0]))
print(faces[0])

def convert_opencv_to_face_recognition(faces):

    top = faces[0][1]
    right =  faces[0][0]+faces[0][2]
    bottom = faces[0][1]+faces[0][3]
    left = faces[0][0]
    return [(top, right, bottom, left)]

res = convert_opencv_to_face_recognition(faces)
print(f"avant {faces}")
print(f"apres {res}")
print(f"ce qu'il fallait avoir {face_locations}")
print(type(res))
print(type(res[0]))


