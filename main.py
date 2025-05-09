import cv2
import numpy as np
from keras.models import load_model

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    _,img  = video.read()
    img = cv2.resize(img,(640,480))

    cv2.imshow('IMG',img)
    cv2.waitKey(1)