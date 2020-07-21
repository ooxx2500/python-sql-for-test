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

透過幾何轉換執行平宜旋轉，此旋轉可保持影像的平行性(平行線)及平值性(值線)

warpAffine():訪射函數
    cv2.warpAffine(src,M,dsize,flags,borderMode borderValue)
    src:影像 M:旋轉矩陣 borderMode:框線模式 BORDER_CONSTANT
    borderValue:框線值 預設0 flags:內插法 INTER_LINEAR dsize:輸出影像尺

'''
#影像縮放
import cv2 as cv

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
x=cv.flip(img,0)  #0:繞x軸翻轉
y=cv.flip(img,1)  #繞Y軸翻轉(1) 
xy = cv.flip(img, -1)  #繞X,Y軸翻轉(-1)
cv.imshow( 'img', img)
cv.imshow( 'x',x)
cv.imshow('y',y)
cv.imshow( 'xy', xy)
cv.waitKey()

#C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg
---------------------------------
#影像位移
import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
height,width = img.shape[:2] #將512 512帶給h ,w
x = 50
y = 200   #x水平位移量 y垂直位移量
M = np.float32([[1,0,x],[0,1,y]])
move = cv.warpAffine(img, M , (width, height) )
cv.imshow( 'img' , img)
cv.imshow('move' ,move)
cv.waitKey()

--------------------------------------
'''
getRatationMatrix2D()
    產出以warpAffine()進行旋轉轉換時的轉換矩陣
    
    cv2.getRotationMatrix2D(center,angle,scale)
    center:旋轉中心點 angle:旋轉角度(逆時針) scale:縮放比例
    以原點旋轉:(自訂旋轉)

getAffinetransform():
    產出以warpAffine()進行訪射轉換時的轉換矩陣(以三個點進行轉換)
    cv2.getAffineTransform(src,dst)
    src:影像的三個點座標 dst:轉換的三個點座標  以上兩個都是2維陣列
'''
#影像旋轉
-----------------------------------
import cv2 as cv

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')

height,width = img.shape[:2]

M = cv.getRotationMatrix2D ((width/2,height/2) ,45,0.8)
rotate = cv.warpAffine(img,M, (width, height) )
cv.imshow( 'img' , img)

cv.imshow( 'rotate', rotate)

cv.waitKey()

---------------------------------------
#影像旋轉
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
rows,cols,ch = img. shape

p1= np.float32([[0,0], [cols-1,0],[0, rows-1]])

p2= np.float32([[0, rows*0.33], [cols*0.85, rows*0.25], [cols*0.15, rows*0.7]])
M = cv.getAffineTransform(p1,p2)

dst = cv.warpAffine(img,M, (cols, rows) )

cv.imshow( 'img' , img)

cv.imshow( 'result',dst)

cv.waitKey()

---------------------------------------
'''
透視轉換:
    將矩陣轉換為任意四邊形，無須維持平行性及平值性
    
warpPerspective()函數
    cv2.warpPerspective(src, M, dsize, flags, borderMode, borderValue)
    參數相同warpAffine()
    
getPerspectivetTransform()函數:
    產出warpPerspective()執行時的轉換矩陣M
    
cv2.getPerspecttiveTrans(src,dst)
    src=原始影像的4個點座標  dst:轉換影像的4個點座標
    任意四邊形無需平行性平值性
    
    
    




    


'''

------------------------------------

import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')

rows,cols = img.shape[:2]

print(rows,cols)

pts1 = np. float32([[150,50], [300,50], [60,450], [210,450]])
pts2= np. float32([[50,50], [rows-50,50], [50,cols-50], [rows-50,cols-50]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M, (cols, rows) )
cv.imshow( 'img',img)
cv.imshow( 'dst',dst)

cv.waitKey()


------------------------------------------
import numpy as np
img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\opencv-logo.png')

rows,cols = img.shape[:2]
print(rows,cols)
ptsl = np. float32([[300, 290], [500, 290], [300, 400], [500, 400]])
pts2 = np. float32([[50,50], [rows-170,100], [50,cols+100], [rows-240,cols-200]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M, (cols, rows) )
cv.imshow( 'img' , img)
cv.imshow( 'dst',dst)
cv.waitKey()


'''
重對映 
    將影像中的象素點放到另一個位置
remap()函數
    cv2.remap(src,x,y,interpolation,borderMode,borderValue)
    src:原始影像  x:對映的x座標  y:對映的y座標
    
繞X，Y軸翻轉:
    對映過程中
        Y軸座標值以X軸做為對秤軸進行交換
        X軸座標值以Y軸做為對秤軸進行交換
    對稱關係為:列號索引從0開始
        目前列號+對稱列號=總列數-1
        目前行號+對稱行號=總行數-1
    




'''
import cv2 as cv

import numpy as np

img = np.random. randint(0,256,size=[4,5],dtype=np.uint8)
rows,cols = img.shape

mapx = np.ones(img.shape,np. float32)*3

mapy = np.ones(img.shape,np. float32)*0

rst = cv. remap(img,mapx,mapy,cv. INTER_LINEAR)
print('img = \n',img)

print('mapx = \n',mapx)

print('mapy = \n',mapy)

print('rst = \n',rst)

-----------------------------------------
import cv2 as cv

import numpy as np

img = np.random. randint(0,256,size=[4,5],dtype=np.uint8)

rows,cols = img.shape

mapx = np.zeros(img.shape,np. float32)

mapy = np.zeros(img.shape,np. float32)

for i in range(rows):

    for j in range(cols):

        mapx.itemset((i,j),j)
        mapy.itemset((i,j),i)

rst = cv.remap(img, mapx,mapy,cv.INTER_LINEAR)

print('img = \n',img)

print('mapx = \n',mapx)

print('mapy = \n',mapy)

print('rst = \n',rst)

--------------------------------
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
rows,cols = img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),i)
rst = cv.remap(img, mapx,mapy,cv.INTER_LINEAR)
cv.imshow( 'img' , img)
cv.imshow('rst', rst)
cv.waitKey()
-------------------------------------
import cv2 as cv

import numpy as np

img = np.random. randint(0,256,size=[4,5],dtype=np.uint8)
rows,cols = img.shape
mapx = np.zeros(img.shape,np. float32)
mapy = np.zeros(img.shape,np. float32)

for i in range(rows):

    for j in range(cols):

        mapx.itemset((i,j),j)
        mapy.itemset((i,j),rows-1-i)

rst = cv.remap(img, mapx,mapy,cv.INTER_LINEAR)

print('img = \n',img)

print('mapx = \n',mapx)

print('mapy = \n',mapy)

print('rst = \n',rst)

------------------------------------------
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
rows,cols = img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),rows-1-i)
rst = cv.remap(img, mapx,mapy,cv.INTER_LINEAR)
cv.imshow( 'img' , img)
cv.imshow('rst',rst)
cv.waitKey()

---------------------------------------------

import cv2 as cv

import numpy as np
img = np.random. randint(0,256,size=[4,6],dtype=np.uint8)
rows,cols = img.shape
mapx = np.zeros(img.shape,np. float32)
mapy = np.zeros(img.shape,np. float32)
for i in range(rows):
    for j in range(cols):
        mapx. itemset((i,j),i)
        mapy.itemset((i,j),j)
rst = cv.remap(img, mapx,mapy,cv.INTER_LINEAR)
print('img = \n',img)
print('mapx = \n',mapx)
print('mapy = \n',mapy)
print('rst = \n',rst)

'''
X,Y軸互換:
    mapx調整為所在行的行號
    mapy調整為所在列的列號
    若行列數量不相同，則無法完成對映的值會設為0



'''












