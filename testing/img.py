import cv2 as cv
import sys
import numpy
import time

cascade_path = "testing/cars.xml"

car_cascade = cv.CascadeClassifier(cascade_path)

video = "testing/car_video.mp4"
cap = cv.VideoCapture(video)

if car_cascade.empty():
    print('Failed to load cascade classifier')
    sys.exit()
    
if not cap.isOpened():
    print('Cannot open video file')
    sys.exit()

while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        print('Finished processing video')
        break 
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors =3)
    
    for (x, y, w, h) in cars:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv.putText(frame, 'Car', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        
    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == 27:
        break
    
cap.release()
cv.destroyAllWindows()