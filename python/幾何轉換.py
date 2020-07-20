# -*- coding: utf-8 -*-
"""
影像縮放:resize()函數
cv2.resize(src,dsize,fx,fy,interpolation)
src:原始影像
dsize:輸出影像大小
fx:水平縮放比例
fy:垂值縮放比
interpolation:內插函式
影像執行幾何處理時若無法直接通過對映值獲得像素點新值時，則將用內差處理(通常放大影像使用)
內插處理:
    INTER_AREA      1.區域內插(鄰近最接近區域)
    INTER_NEAREST   2.最鄰近內插(鄰近最接近區域)
    INTER_CUBIC     3.三次樣條內插(像點附近4*4區域)
    INTER_LINEAR    4.線性內插(預設)
    




"""

import cv2 as cv
import numpy as np

img = np.ones([2,4,3],dtype = np.uint8) #原始影像大小:2列4行
size =img.shape[:2]         #resize後的大小:4列2行 結果的行數為原始的列數
rst = cv.resize(img,size)   #shape屬性:第一個值:行 第2個值:列
print('img.shape = \n',img.shape)#dsize屬性:第一個值:列，第二個值:行
print('img = \n',img)

print('rst.shape = \n',rst.shape)
print('rst = \n',rst)

--------------------------------

import cv2 as cv

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
rows,cols = img.shape[:2]
size = (int(cols*0.9),int(rows*0.5))
rst = cv.resize(img,size)
print('img.shape = \n',img.shape)
print('rst.shape = \n',rst.shape)
cv.imshow( 'img', img)
cv.imshow('rst', rst)

cv.waitKey()


-----------------------------
import cv2 as cv

img1 = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
img2 = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
img3 = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
res1 = cv.resize(img1,None, fx=1.5, fy=1.5, interpolation=cv.INTER_AREA)
res2 = cv.resize(img2,None, fx=1.5, fy=1.5, interpolation=cv.INTER_LINEAR)
res3 = cv.resize(img3,None, fx=1.5, fy=1.5, interpolation=cv.INTER_CUBIC)
cv.imshow('img1', img1)
cv.imshow('res1', res1)
cv.imshow('res2', res2)
cv.imshow('res3', res3)
cv.imwrite(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512_A.jpg',res1)
cv.imwrite(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512_L.jpg',res2)
cv.imwrite(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512_C.jpg', res3)
while True:
    if(cv.waitKey() & 0xFF) == ord('q'):
        break
    else:
        pass

cv.destroyAllWindows()

'''
影像翻轉:flip()
cv2.flip(src,flipcode) 
src:原始影像 
flipcode:  0:繞x軸翻轉
        正數:繞Y軸翻轉(1) 
        負數:繞X,Y軸翻轉(-1)


'''
#影像翻轉
import cv2 as cv

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
x=cv.flip(img,0)
y=cv.flip(img,1)
xy = cv.flip(img, -1)
cv.imshow( 'img', img)
cv.imshow( 'x',x)
cv.imshow('y',y)
cv.imshow( 'xy', xy)
cv.waitKey()











