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

----------------------------------

import dlib
import cv2 as cv

cap = cv.VideoCapture(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\short_hamilton_clip.mp4')
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fourcc = cv.VideoWriter_fourcc(*'XVID')#XVID編碼
out = cv.VideoWriter(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\output.avi', fourcc, 20.0, (width, height))
detector = dlib.get_frontal_face_detector()

while(cap.isOpened()):
  ret, frame = cap.read()

  face_rects, scores, idx = detector.run(frame, 0)

  for i, d in enumerate(face_rects):
    x1 = d.left()          
    y1 = d.top()
    x2 = d.right()
    y2 = d.bottom()
    text = "%2.2f(%d)" % (scores[i], idx[i])

    cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4, cv.LINE_AA)

    cv.putText(frame, text, (x1, y1), cv.FONT_HERSHEY_DUPLEX,
             0.7, (255, 255, 255), 1, cv.LINE_AA)

  out.write(frame)

  cv.imshow('Video face Detection', frame)
  if cv.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
out.release()
cv.destroyAllWindows ()

-------------------------------------------

import dlib
import cv2

predictor_path = r'C:\Users\ASUS\Documents\Python-SQL\python\figure\shape_predictor_5_face_landmarks.dat'
face_path = r'C:\Users\ASUS\Documents\Python-SQL\python\figure\face_trumpfamily.jpg'

def renderFace(im, landmarks, color=(0, 255, 0), radius=3):
    for p in landmarks.parts():
        cv2.circle(im, (p.x, p.y), radius, color, -1)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

img = cv2.imread(face_path)

dets = detector(img, 1)

for k, d in enumerate(dets):
    shape = predictor(img, d)
    renderFace(img, shape)

cv2.imshow("face-rendered", img)
cv2.waitKey()

'''
Dlib模型
人臉特徵點定位，對齊(如眼角嘴角)
用途:
    1.改善人臉識別使人辨識演算法更有效
    2.人臉平均:獎多張人臉進行融合型成一新平均人臉
    3.人臉交換:獎兩張人臉鏡行無縫融合，型成換臉(A臉換至B臉)
    4.人臉裝扮:人臉化妝美圖等等
'''

import cv2
import imutils
import dlib
from imutils.face_utils import FaceAligner
from imutils import face_utils

predictor_path = r'C:\Users\ASUS\Documents\Python-SQL\python\figure\shape_predictor_5_face_landmarks.dat'
face_path = r'C:\Users\ASUS\Documents\Python-SQL\python\figure\1185550311.jpg'

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
fa = FaceAligner(predictor, desiredFaceWidth=256)

image = cv2.imread(face_path)
image = imutils.resize(image, width=800)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Input", image)
rects = detector(gray, 2)

for rect in rects:
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        faceOrig = imutils.resize(image[y:y + h, x:x + w], width=256)
        faceAligned = fa.align(image, gray, rect)

        cv2.imshow("original", faceOrig)
        cv2. imshow( "Aligned", faceAligned)
        cv2.waitKey()


-----------------------------------

#偵測人數
import numpy as np
import cv2 as cv
import dlib

predictor_path = r'C:\Users\ASUS\Documents\Python-SQL\python\figure\shape_predictor_68_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\person_8.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
nums = detector(img_gray, 2)#修改0-2可以找出人臉
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
'''
局部二值模式長條圖

將象素值與其最鄰近的81個像素值逐一比對
    若像素值>鄰近像素值則得到0
    若像素值<鄰近像素值則得到1
    將象素值得到的0,1值連接得到一個二靜位素值再將二進位數值轉為10進位即為像素之LBP值
LBPH人臉辨識
    face_LBPHFaceRecognizer_create(
        radius, 半徑值(預設1)
        neighbors, 鄰近據點個數(預設8)
        grid_x, 行方向的象素分組單位(預設8)
        grid_y, 列方向的象素分組單位(預設8)
        threshold) 閥值:預測用大於該值表示沒有影像         
        )
    
face_FaceRecognizer.train()函數
    為LBPH識別器模型物件
face_forcognizer.traib
    src,   訓練影像
    lavels) 每個影像對映的標籤值
    對影像進行計算，得到一象量值
face_FaceRecognizer.predict()函數
    為LBPH辨識器模型物件
face_FaceRecognizer.predict(src)
    傳回值=label.confidence
         #辨識結果標籤   #可靠度評分為辨別結果與模型之間的巨離 
                      0:完全吻合 大部分低於50可視度大餘80則差別較大
    
    
'''







