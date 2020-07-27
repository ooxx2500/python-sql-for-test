# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:36:11 2020

@author: ASUS
"""

import dlib
import cv2 as cv
import imutils

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\face_execuite.jpg')
img = imutils.resize(img, width=1280)
detector = dlib.get_frontal_face_detector()

#偵測人臉，輸出分數
face_rects, scores, idx = detector.run(img, 1, -1)

for i, d in enumerate(face_rects):
  x1 = d.left()         
  y1 = d.top()
  x2 = d.right()
  y2 = d.bottom()
  text ="%2.2f(%d)" % (scores[i], idx[i])
  cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4, cv.LINE_AA)
  #標示分數                                                    
  cv.putText(img, text, (x1, y1), cv.FONT_HERSHEY_DUPLEX,
          0.7, (255, 255, 255), 1, cv.LINE_AA)
cv.imshow("Face Detection", img)
cv.waitKey()