# -*- coding: utf-8 -*-
"""
RGB色彩空間:
    RGB三者重要性相等，但忽略亮度資訊
    為硬體角度的色彩模型
    以人眼觀看存在一定的差異程度
    
HSV色彩空間:
    視覺感知的色彩模型，以心理學及視覺角度指出人類視覺感知包含三個部分
    1.色調(色相)Hue:光的顏色
        設定值範圍 0~360
        0   紅色  240 藍
        60  黃    300 品紅
        120 綠
        180 青
    2.飽和度(Saturation):色彩深淺程度，為ㄧ比例值範圍:0~1
        是色彩純度與最大純度值之比值，飽和度=0即為灰階
    3.明暗(Value):光的明暗程度，範圍:0~1

函數:cvtColor() 色彩空間轉換
    cvtColor(src,mode)  src:原始影像  mode:色彩空間轉換    
    openCV色彩轉換模型為BGR與RGB不同

灰階轉BGR:當影像由灰色色彩空間轉換BGR色彩空間時，最後所有通道是相同的

RGB和BGR互換:R值與B值互換，G值不變

BGR2GARY
GARY2BGR

"""
#RGB/BGR轉換到GRAY(灰階)
#GRAY=0.299*R+0.587*G+0.114*B
import cv2 as cv
import numpy as np

img = np.random.randint(0,256,size=[2,4,3],dtype=np.uint8)
rst = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

print('img = \n',img)
print('rst = \n',rst)
print('像素點(1,0) 直接計算得到的值 =',img[1,0,0]*0.114+img[1,0,1]*0.587+img[1,0,2]*0.299)
print('像素點(1,0) 使用公式cv.cvtColor() 轉換值 =',rst[1,0])

---------------------------------------
#灰階變BGR 黑白變彩色
import cv2 as cv
import numpy as np

img = np.random. randint(0,256,size=[2,4],dtype=np.uint8)#2列4行
rst = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
print('img = \n',img)
print('rst \n', rst)

---------------------------
#BGR RGB互相轉換
import cv2 as cv
import numpy as np
np.random.randint(0,256,size=[2,4,3],dtype=np.uint8)

img=np.random.randint(0,256,size=[2,4,3],dtype=np.uint8)
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
bgr = cv.cvtColor(rgb,cv.COLOR_RGB2BGR)

print('img = \n',img)
print('rgb = \n',rgb)
print('bgr = \n',bgr)

--------------------------------
#img轉灰階再轉彩色

import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)#彩色轉灰階
bgr = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)#輝接轉彩色
#灰階轉BGR時變為三個相同數字的，性值還是彩色(3通道)
print('img. shape =', img.shape)#.shape影像結構 前兩個素值長寬 第三個素值:色彩通到
print( 'gray.shape =' ,gray.shape)
print('bgr.shape = ',bgr.shape)

 

cv.imshow( 'img' , img)
cv.imshow( 'gray' ,gray)
cv.imshow( 'bgr' ,bgr)
print('bgr = \n',bgr)
cv.waitKey()

---------------------------------
#RGB BGR顏色互換
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow( 'img' , img)
cv.imshow( 'rgb' , rgb)
cv.waitKey()


'''
HSV
色調(H值):設定範圍為0-360，8位元影像每個像素點能表示的灰階等級為2**8=256個，故8位元影像
    要以HSV表示時必須將H值調整為0~255，處理方法: H值/2(得到0~180之間的數值，配合8進位2進位表示)
0:紅    90:青
30:黃   120:藍
60:綠   180:品紅

飽和度(S值):設定範圍為0~1
    因灰階影像之RGB值成分相等，相當於一種極度不飽和的色彩，故灰階影像其飽和度=0
    灰階影像顯示時較亮區域對應的色彩具有比較高的飽和度
    極低飽和度所得之色調值不可靠
    
亮度(V值):設定範圍為0~1對應到0~255

BGR2HSV

HSV色彩主要差異是在H通道可對通道進行篩選，以選出特定色彩。
    inRange()函數針對象素點之象素值判斷是否在某範圍內
    cv2.inRange(src,lower,upper) src:影像 lower:範圍下限 upper:範圍上限
    若src的值在範圍內，則傳回值中對應位置上之值為:255 否則:0

'''

import cv2 as cv
import numpy as np

imgblue = np.zeros([1,1,3],dtype=np.uint8)#一個像素值3通道
print(imgblue)
imgblue[0,0,0] = 255 #像素點第0個通道設為255
print(imgblue)
Blue = imgblue #測試藍色的HSV值
BlueHSV = cv.cvtColor(Blue,cv.COLOR_BGR2HSV)
print('Blue = \n',Blue)
print('BlueHSV = \n',BlueHSV)
imggreen = np.zeros([1,1,3],dtype=np.uint8)
print(imggreen)
imggreen[0,0,1] = 255
print(imggreen)
Green = imggreen
GreenHSV = cv.cvtColor(Green,cv.COLOR_BGR2HSV)
print('Green = \n',Green)
print('GreenHSV = \n',GreenHSV)
imgred = np.zeros([1,1,3],dtype=np.uint8)
imgred[0,0,2] = 255
Red = imgred
RedHSV = cv.cvtColor(Red,cv.COLOR_BGR2HSV)
print('Red = \n',Red)
print('RedHSV = \n',RedHSV)

-------------------------------------------

import cv2 as cv
import numpy as np
img= np.random.randint(0,256,size=[5,5],dtype=np.uint8)
min=100
max=200
mask=cv.inRange(img,min,max)
print('img = \n',img)
print('mask = \n',mask)


-------------------------------------------

import cv2 as cv
import numpy as np

img = np.ones([5,5],dtype=np.uint8)*9#用亂數產生5*5都是9的矩陣
mask = np.zeros([5,5],dtype=np.uint8)
mask[0:3,0] = 1
mask[2:5,2:4] = 1
roi = cv.bitwise_and(img,img,mask=mask)
print('img = \n',img)
print('mask = \n',mask)
print('roi = \n',roi)


'''
HSV色彩空間分析色彩時並非分析一特定值而是分析一色彩區間，如藍色H值為120分析藍色時會以
其附近值做為區間，通常複進值為半徑10，即120+10，120-10做為分析區間，S通道V通道分析區間
在100~255，因保合度亮度太低時，得到的H值不可靠

HSV色彩區間:[H-10,100,100]~[H+10,255,255]

紅色色彩區間:[0,100,100]~[10,255,255]

綠色色彩區間:[50,100,100]~[70,255,255]

藍色色彩區間:[110,100,100]~[130,255,255]

膚色分析(HSV)
一般可設定為:
    色調值:5~170   飽和度:25~166
    
處理並設定HSV值:並將其設定為遮罩mask在將影像遮罩做位元運算，達到以遮罩控制影像顯示的目的

於RGB/BGR 3通道在加一通到名為alpha及透明度通道，即為4通道影像，為RGBA/BGRA色彩空間，
設定值範圍:0~1 or 0~255(透明~不透明)
    
'''

import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\opencv-logo.png')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow( 'img' , img)
minBlue = np.array([110,50,50])
maxBlue = np. array([133,255,255])#指定值的範圍
mask = cv.inRange(hsv,minBlue,maxBlue)#確定藍色的區域
blue = cv.bitwise_and(img,img,mask=mask)
cv.imshow( 'blue',blue)
minGreen= np.array([50,50,50])
maxGreen =np.array([70,255,255])
mask = cv.inRange(hsv,minGreen,maxGreen)
green = cv.bitwise_and(img,img,mask=mask)
cv.imshow( 'green' ,green)
minRed = np.array([0,50,50])
maxRed = np.array([30,255,255])
mask = cv.inRange(hsv,minRed,maxRed)
red = cv.bitwise_and(img,img,mask=mask)
cv.imshow( 'red', red)
cv.waitKey()

----------------------------------

import cv2 as cv

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
h,s,v = cv.split(hsv)
minHue=4
maxHue=170
hueMask = cv.inRange(h,minHue,maxHue)
minSat=25
maxSat = 165
satMask = cv.inRange(s,minSat,maxSat)
mask = hueMask & satMask
roi = cv.bitwise_and(img, img,mask=mask)
cv.imshow( 'img' , img)
cv.imshow( 'ROI', roi) 
cv.waitKey()

---------------------------------

import cv2 as cv
import numpy as np

img = np.random. randint(0,256,size=[2,3,3],dtype=np.uint8)
bgra = cv.cvtColor(img,cv.COLOR_BGR2BGRA)
print('img = \n',img)
print('bgra = \n',bgra)
b,g,r,a = cv.split(bgra)#分割成4個變數
print('a = \n',a)
a[:,:] = 125
bgra =cv.merge([b,g,r,a]) #將所有的bgra的a從255改成125
print('bgra = \n',bgra)

-----------------------

import cv2 as cv

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
bgra = cv.cvtColor(img,cv.COLOR_BGR2BGRA)
b,g,r,a = cv.split(bgra)
a[:,:]=60
bgral25 = cv.merge([b,g,r,a])
a[:,:]=0
bgra0 = cv.merge([b,g,r,a])
cv.imshow( 'img' , img)
cv.imshow( 'bgra' ,bgra)
cv.imshow( 'bgra125',bgral25)
cv.imshow( 'bgra0' ,bgra0)
cv.waitKey()
cv.destroyAllWindows ( )
cv. imwrite(r'C:\Users\ASUS\Desktop\Python\bgra.png' ,bgra)
cv. imwrite(r'C:\Users\ASUS\Desktop\Python\bgra125. png' ,bgral25)
cv. imwrite(r'C:\Users\ASUS\Desktop\Python\bgra0. png' ,bgra0)

------------------------------

import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\lena_01.jpg')
cv.imshow("img", img)
hsv_low = np.array([0, 0, 0])
hsv_high = np.array([0, 0, 0])
def h_low(value):
    hsv_low[0] = value
def h_high(value):

    hsv_high[0] = value
def s_low(value):

    hsv_low[1] = value
def s_high(value):

    hsv_high[1] = value
def v_low(value):

    hsv_low[2] = value
def v_high(value):

    hsv_high[2] = value
cv.namedWindow('image')


cv.createTrackbar('H_low', 'image',0,255,h_low)
cv.createTrackbar('H_high','image',0,255,h_high)
cv.createTrackbar('S_low','image',0,255,s_low)
cv.createTrackbar('S_high','image',0,255,s_high)
cv.createTrackbar('V_low','image',0,255,v_low)
cv.createTrackbar('V_high','image',0,255,v_high)

while(1):
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hsv = cv.inRange(hsv, hsv_low, hsv_high)
    cv.imshow('hsv',hsv)
    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()



















