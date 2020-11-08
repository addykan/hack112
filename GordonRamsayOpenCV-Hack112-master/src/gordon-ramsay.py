import numpy as np
import cv2
import pickle
import time, random
from playsound import playsound

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./recognizers/face-trainner.yml")

cap = cv2.VideoCapture(1)

inactiveCount = 0

while(True):
    # capture the camera windows frame-by-frame
    ret, frame = cap.read()
	# use grayscale to best capture face features
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=5)

    # print(face_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=5))

	# if face not detected, ie. looking down/away, inactive ++
    if face_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=5) == ():
    	inactiveCount += 1
    	if inactiveCount > 100:
    			# play sound of Gordon Ramsay insult
    			sounds = ['are-you-always-this-pathetic.mp3',
    					  'get-in-there.mp3', 'this-is-wrong.mp3']
    			playsound(sounds[random.randint(0, len(sounds)-1)])
    			inactiveCount = 0

	# if the face is detected, check for posture			
    for (x, y, w, h) in faces:
    	roi_gray = gray[y:y+h, x:x+w] # (ycord_start, ycord_end)
    	roi_color = frame[y:y+h, x:x+w]

    	# if user has bad posture, ie. sitting low in seat or not centered 
    	if ((x < 200 or x > 300) or (y > 220)):
    		inactiveCount += 1
    		if inactiveCount > 100:
    			# play sound of Gordon Ramsay insult
    			sounds = ['are-you-always-this-pathetic.mp3',
						  'get-in-there.mp3', 'this-is-wrong.mp3']
    			playsound(sounds[random.randint(0, len(sounds)-1)])
    			inactiveCount = 0

    	color = (255, 0, 0) #BGR 0-255 
    	stroke = 2
    	end_cord_x = x + w
    	end_cord_y = y + h
    	cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    print(inactiveCount)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
