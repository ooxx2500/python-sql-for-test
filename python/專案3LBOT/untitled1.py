# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:36:11 2020

@author: ASUS
"""

import numpy as np
import cv2 as cv
import dlib

predictor_path = r'C:\Users\ASUS\Documents\Python-SQL\python\figure\shape_predictor_68_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\person_8.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
nums = detector(img_gray, 0)
for i in range(len(nums)):
    landmarks = np.matrix([[p.x, p.y] for p in predictor(img,nums[i]).parts()])
    for idx, point in enumerate (landmarks):
        pos = (point[0 , 0], point[0, 1])
        print(idx,pos)
        cv.circle(img, pos, 3, color=(0, 255, 0))
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, str(idx+1), pos, font, 0.4, (0, 0, 255), 1,cv.LINE_AA)
cv.imshow("img", img)
cv.waitKey()
