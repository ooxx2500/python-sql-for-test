# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:38:22 2020

@author: ASUS
"""
'''
Dlib:(C++函式庫)

用於機器學習、影像處理、影像辨識。
人臉偵測演算法:
    方向梯度直方圖(HDG)
    直線分類器(Linear Classifier)
    影像金字塔(image pyramid)
    滑動窗格(sliding window)
演算結果的到一分數值:分數越大越接近人臉，分數越小越接近誤判

python要安裝3.6板(spyder內降板)

要從新裝pip install cv2    pip install dlib


get_frontal_face_detector函式
    格式:變數=dlib.get.frontal_face_detector()
        產生正面臉部偵測元件
    偵測人臉:
        結果=變數.run(特徵偵測影像，偵測參數，分數參數:-1)
    安裝 imutils  pip install imutils
        提供影像編輯功能




'''
#Dlib抓人臉
import dlib
import cv2
import imutils

img=cv2.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\person_8.jpg')
img=imutils.resize(img, width=1280)
detector =dlib.get_frontal_face_detector()
face_rects=detector(img,1) #0:一般針測 1:人臉偵測

for i , d in enumerate(face_rects):
    x1=d.left()
    y1=d.top()
    x2=d.right()
    y2=d.bottom() #取出人臉的上下左右
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0),4,cv2.LINE_AA)

cv2.imshow('Face_Detection',img)
cv2.waitKey()

--------------------------------
#分數越高越等於人臉，分數越低越等於誤判

import dlib
import cv2 as cv
import imutils

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\face_execuite.jpg')
img = imutils.resize(img, width=1280)
detector = dlib.get_frontal_face_detector()

#偵測人臉，輸出分數
face_rects, scores, idx = detector.run(img, 1, -1)#0:一般針測 1:人臉偵測

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
















