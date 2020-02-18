import dlib
import cv2
import numpy as np
import glob
from scipy.spatial import distance
from imutils import face_utils
from keras.models import load_model
import tensorflow as tf
import imutils

from fr_utils import *
from inception_blocks import *

FR_model = load_model('nn4.small2.v1.h5')

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

threshold = 0.25

face_database = {}

for name in os.listdir('images'):
	for image in os.listdir(os.path.join('images',name)):
		identity = os.path.splitext(os.path.basename(image))[0]
		face_database[identity] = fr_utils.img_path_to_encoding(os.path.join('images',name,image), FR_model)


num_x = 600

def classification(path):
	capture = cv2.VideoCapture(path)
	ret, frame = capture.read()
	frame = imutils.resize(frame, width=600)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
	frame = cv2.flip(frame, 1)

	faces = face_cascade.detectMultiScale(frame, 1.3, 5)
	rects = detector(gray, 0)
    
	for rect in rects:
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)
		for (i, (xx, yy)) in enumerate(shape):
			num_x =  ((xx * 100)/600) - 100
			num_x = abs(int((num_x * 600) /100))
			print("xx: "+str(num_x))
			cv2.circle(frame, (num_x, yy), 1, (0, 0, 255), -1)
    
    
	for(x,y,w,h) in faces:
		print("x: "+str(x))
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		roi = frame[y:y+h, x:x+w]
		encoding = img_to_encoding(roi, FR_model)
		min_dist = 100
		identity = None

		for(name, encoded_image_name) in face_database.items():
			dist = np.linalg.norm(encoding - encoded_image_name)
			if(dist < min_dist):
				min_dist = dist
				identity = name

	capture.release()
	return identity[:-1]

    




