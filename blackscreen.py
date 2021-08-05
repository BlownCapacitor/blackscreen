import numpy as np
import time 
from cv2 import cv2  
import keyboard


img = cv2.imread('imageforproject.jpeg')

cv2.imshow('image', img)
while True:

    frame = cv2.VideoCapture(0)
    image = cv2.VideoCapture(0)
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    time.sleep(1)

    l_black= np.array([104,153,70])
    u_black = np.array([30,30,0])

    mask1 = cv2.inRange(img, 0)
    res = cv2.bitwise_and(frame, frame, mask = mask1)
    
    f = frame - res

    f = np.where(f == 0, image,  f)

    frame_out = cv2.addWeighted(res, 1, img, 1,0)

    image_out = image

    cv2.imshow('image',image_out)
    cv2.imshow('frame', frame_out)
    cv2.waitKey(1)
    
    if keyboard.is_pressed('q'):
        break
    if keyboard.is_pressed('esc'):
        break
