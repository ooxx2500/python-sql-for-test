# -*- coding: utf-8 -*-
"""
影像辨識 opencv

要安裝opencv模組: pip install opencv-python

  讀取影像: imread(路徑)
  格式 cv2.imread(影像檔案名稱,flag)
  
    讀取的資料匯儲存成一個numpy的陣列(串列)，陣列的前兩個維度為圖片的高度寬度
    第三個維度是圖片色彩的channel，如果是RGB的圖片channel=3、灰階channel=1
    
    #flag:控制檔案類型
     IMREAD_COLOR(1)彩色 三類
     IMREAD_GRAYSCALE(0)灰階 兩類
     IMREAD_UNCHANGED(-1)所有影像頻道包含灰階
        
     
  視窗命名:cv2.namedWindow(視窗名稱)

  cv2.namedWindow(... ,CV.WINDOW_NORMAL) #視窗可調整大小

  顯示影像:cv2.imshow(視窗名稱 , 顯示的影像)

  寫入影像:cv2.imwrite(寫入的檔案名稱，要寫入的檔案)

  關閉式窗:cv2.destoryWindow(視窗名稱)

  關閉所有視窗:cv2.destoryAllWindow()

  等待按鍵:cv2.waitkey(delay) 功能:視窗等待按鍵去關閉 #delay延遲多久
      #等待ASCII碼的數字

繪圖:
  共同參數:
    img:要繪製圖形的影像
    color:色彩使用BGR模型，以數組型態儲存，例如(255,0,0)
    thickness:線條粗細，預設1
    linetype:線條類型
  劃線: cv2.line(img,起點座標,終點座標,color,thickness,linetype)      
    
    numpy.zeros():建立一個所有元素都是0的數組
    a=numpy.zeros(x,x,3) #(0,0,0,)
    a.fill(64)           #變成(64,64,64)
    
  畫矩形: cv2.rectangle(img,頂點1,頂點2,color,thickness,linetype)
    linetype = -1 代表矩形填滿顏色
    
  劃圓: cv2.circle(img,圓心,半徑,color,thickness,linetype) 
    linetype = -1 代表矩形填滿顏色

  劃橢圓形: cv2.ellipse(img,圓心,(軸1,軸2),旋轉角度,圓弧起始角度,圓弧結束角度,color,thickness,linetype)

  畫多邊形: cv.polylines(line,頂點座標,isClosed,color,thickness,linetype)
    頂點座標必須是一個陣列(串列)其資料型態必須為numpy.int32
    繪圖前必須以reshape重新計算調整頂點  

    reshape(頂點數量,1,2)

    1.建立頂點座標:x = numpy.array([[a,b],[c,d],....],numpy.int32)
    2.再用y = x.reshape(頂點數量:設-1由其他參數計算得出 , 1 , 2)
    3.cv.polylines(line,頂點座標,isClosed(布林直),color,thickness,linetype)
    
                                   bottomLeft(origin):文字映射(True/False)
  寫文字:cv2.putText(img,文字,座標 ,字型,大小,color,thickness,bottomLeft(origin),True)
                                                            
  使用自定字型:載入PIL模組下的:
    1.ImageFont ImageFont.truetype 載入字體
    2.Image Image.fromarray 將numpy陣列轉為PIL影像
    3.ImageDraw ImageDraw.Draw 在PIL影像上寫文字
    4.使用text方法已設定的字型及大小寫入文字
  台北黑體 Taipei Sans TC



"""

'''
有以下錯誤開不了圖片 路徑不能打中文
error: OpenCV(4.2.0) C:\projects\opencv-python\opencv\modules\highgui\src\window.cpp:376:
error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'
'''
#讀取影像 用PY的方法
import cv2 as cv

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\lena_01.jpg')
cv.namedWindow('image')
cv.imshow('image',img)
cv.waitKey()
------------------------------------
#讀取圖案灰階，esc關閉 s儲存並關閉
import cv2 as cv
img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\lena_01.jpg',1)
#參數0讀取灰階圖案
cv.imshow('image',img)
x = cv.waitKey() #x代表ascii的數字
if x ==27: #27代表鍵盤左上角的ESC按鍵
    cv.destroyAllWindows()
elif x == ord('s'): #當x數值等於ascii的's'時
    cv.imwrite(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\lena_01.png' ,img)
    cv.destroyAllWindows()
------------------------------
#用numpy畫圖 cv2.circle(img,圓心,半徑,color,thickness,linetype) 
import cv2 as cv
import numpy as np
#numpy.zeros():建立一個所有元素都是0的數組  #np.zeros(512,512,3)  #由imshow()讀入
img = np.zeros((512,512,3),np.uint8)   #建立512*512大小的影像圖片，每一格中有3個元素都是0(BGR)黑色
cv.line(img,(0,0),(511,511),(255,0,0),5)#(255,0,0)是BGR的顏色數值 5線粗           
cv.imshow('image',img)
cv.waitKey()

----------------------------------
#用numpy畫圖 三條線 不同顏色粗細
import cv2 as cv
import numpy as np
n=300                      #取消正負號，這樣就會沒有負數
img = np.zeros((n+1,n+1,3),np.uint8)#用np.zeros建立一個都是0(黑色)的圖檔
img = cv.line(img,(0,0),(n,n),(255,0,0),3) ##(255,0,0)是BGR的顏色數值 3線的粗細
img = cv.line(img,(0,100),(n,100),(0,255,0),1)
img = cv.line(img,(100,0),(100,n),(0,0,255),60)
cv.imshow('image',img)
cv.waitKey()
-------------------------------------
#畫矩形 cv2.rectangle(img,頂點1,頂點2,color,thickness,linetype)
import cv2 as cv

img = np.zeros((512,512,3),np.uint8) #np.uint8:設定無號的8位元整數(沒負號)
cv.rectangle(img,(384,0),(510,128),(0,255,0),5)
cv.imshow('image',img)
cv.waitKey()

-----------------------------
#畫矩形 底白色並用紅色填滿矩形
import cv2 as cv
import numpy as np
n=300  #用np.zeros建立一個都是1(白色)的圖檔*255 
img = np.ones((n,n,3),np.uint8)*255
print(img)
img = cv.rectangle(img,(50,50),(n-100,n-50),(0,0,255),-1) #-1叫做填滿
cv.imshow('image',img)
cv.waitKey()
------------------------------
#劃圓形 cv2.ellipse(img,圓心,(軸1,軸2),旋轉角度,圓弧起始角度,圓弧結束角度,color,thickness,linetype)
import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8)
print(img)
cv.circle(img,(250,250),100,(0,0,255),-1)#圓心,半徑,顏色,線粗(-1代表填滿圓)
cv.imshow('image',img)
cv.waitKey()

----------------------------
#畫同心圓
import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),dtype='uint8') #建立512*512的黑色圖片
#取得中心點(img.shape[1] / 2 , img.shape[0] /2)
#img.shape[0]:圖片的垂直寬度(column)
#img.shape[1]:圖片的水平寬度(row)
#img.shape[2]:channel數
for r in range(0,175,25):
    cv.circle(img,(img.shape[1] //2, img.shape[0] //2),r,(0,0,255))
    #要用商數因位帶入的數值一定要整數
cv.imshow('image',img)
cv.waitKey()
-------------------------------------
#畫同心圓2
import cv2 as cv
import numpy as np
d = 400
img = np.ones((d,d,3),dtype='uint8')*255 #建立512*512的黑色圖片
print(img)
(centerX , centerY) = (round(img.shape[1]/2), round(img.shape[0]/2))
#找圓心座標            #四捨五入求水平  #四捨五入求重直 #round(數值,小數位數):求四捨五入
red=(0,0,255) 
for r in range(5,round(d/2),12):
    cv.circle(img,(centerX,centerY),r,red,3)

cv.imshow('image',img)
cv.waitKey()
-------------------------------
#劃橢圓形 cv2.ellipse(img,圓心,(軸1,軸2),旋轉角度,圓弧起始角度,圓弧結束角度,color,thickness,linetype)
import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8)
img.fill(200)

cv.ellipse(img,(180,200),(100,60),0,0,360,(128,0,255),2)
#s(起始):0 e(結束):360 就是一個完整的橢圓
#cv.ellipse(img,(180,200),(50,100),45,0,180,(255,0,128),-1)

cv.imshow('image',img)
cv.waitKey()
cv.destroyAllWindows()
-------------------------------------
#亂數畫橢圓
import cv2 as cv
import numpy as np
d=400
img = np.ones((d,d,3),np.uint8)*255
center=(round(d/2),round(d/2))
size=(100,200)
for i in range(0,10):
    angle = np.random.randint(0,361)
    color = np.random.randint(0,high=256,size = (3,)).tolist()
                                 #size=(3,) 每行三個 不只定row
    
    thickness = np.random.randint(1,9)
    cv.ellipse(img,center,size,angle,0,360,color,thickness)
    print(color)
cv.imshow('image',img)
cv.waitKey()

--------------------------------
#畫多邊形
import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8) 
pts = pts.reshape((-1,1,2))        #建立4個頂點然後設定格式為np.int32 
pts = np.array([[10,5],[60,90],[100,100],[130,80],[110,70]],np.int32) 
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
cv.imshow('image',img)
cv.waitKey()


---------------------------
#寫字 cv2.putText(img,文字,座標 ,字型,大小,color,thickness,bottomLeft(origin))
import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8) 
font = cv.FONT_HERSHEY_SIMPLEX  #font的字體名稱
cv.putText(img,'openCV',(10,350),font,4,(255,255,255),10,cv.LINE_AA)
                                     #字體大小        #粗細 #反鋸齒處理
cv.imshow('image',img)
cv.waitKey()
cv.destroyAllWindows


------------------
#寫入文字並顯示各種字型文字
import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8) 
text = 'OpenCV for py'

cv.putText(img,text,(10,40),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,255),1,cv.LINE_AA)
cv.putText(img,text,(10,80),cv.FONT_HERSHEY_PLAIN,1,(0,255,255),2,cv.LINE_AA)
cv.putText(img,text,(10,120),cv.FONT_HERSHEY_DUPLEX,1,(0,255,255),1,cv.LINE_AA)
cv.putText(img,text,(10,160),cv.FONT_HERSHEY_COMPLEX,1,(0,255,255),2,cv.LINE_AA)
cv.putText(img,text,(10,200),cv.FONT_HERSHEY_TRIPLEX,1,(0,255,255),1,cv.LINE_AA)
cv.putText(img,text,(10,240),cv.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255),2,cv.LINE_AA)
cv.putText(img,text,(10,280),cv.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,255,255),1,cv.LINE_AA)
cv.putText(img,text,(10,320),cv.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,255,255),2,cv.LINE_AA)                                             
cv.imshow('image',img)
cv.waitKey()
cv.destroyAllWindows

---------------------------
#描邊文字
import cv2 as cv
import numpy as np
d=400
img = np.ones((d,d,3),dtype='uint8')*255
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(0,200),font,3,(0,255,0),10)
cv.putText(img,'OpenCV',(0,200),font,3,(0,0,255),5)  #改粗細就可以描邊
cv.imshow('image',img)
cv.waitKey()


-------------------
#鏡射文字
import cv2 as cv
import numpy as np
d=400
img = np.ones((d,d,3),dtype='uint8')*255
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(20,150),font,3,(0,0,255),15,cv.LINE_AA)
cv.putText(img,'OpenCV',(20,220),font,3,(0,255,0),15,
           cv.FONT_HERSHEY_SIMPLEX,True)
  
cv.imshow('image',img)
cv.waitKey()
--------------------------
#自訂字形
from PIL import ImageFont,ImageDraw, Image
import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8) 
img.fill(64)#將(0,0,0)變成(64,64,64)

img[:] =(0,0,192) #全不設定為(0,0,192) 所以背景為紅色
text = '恭賀\n新喜'
fontPath = r'C:\Users\ASUS\Desktop\Software\TaipeiSansTCBeta-Regular.ttf'
#字型檔案的路徑
font = ImageFont.truetype(fontPath , 224) #ImageFont.truetype(字體檔案位置,字體大小)

imgPil = Image.fromarray(img)#將numpy陣列轉為PIL影像

draw =ImageDraw.Draw(imgPil) #在影像上加入文字
draw.text((30,30),text,font = font,fill=(0,0,0,0))#填滿(前三0是顏色最後一個0是透明度)  

img= np.array(imgPil)#PIL轉為numpy
cv.imshow('image',img)
cv.waitKey()
cv.destroyAllWindows


---------------------------------
"""
影像加法運算:灰階影像中像素以8位元表示，像素值範圍0~255，像素的飽和值為255(最大值)

  影像加法:兩影像對應得像素值相加，如果<=255 直接相加
                           ，如果>255，將結果mod256得出結果 Ex:(255+58)%256=57
  add():影像像素相加，如果<=255 直接相加
                 ，如果>255 值接等於最大值255
    格式:cv2.add(影像1,影像2)
                           
  


"""
#測式兩陣列相加
import numpy as np
img1=np.random.randint(0,256,size=[3,3],dtype=np.uint8)#建立兩個模擬圖像，數值0~255
img2=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
print('img1=\n', img1)
print('img2=\n', img2)
print('img1+img2=\n', img1+img2)

--------------------
#兩圖片相加 最大值255
import cv2 as cv
import numpy as np
img1=np.random.randint(0,256,size=[3,3],dtype=np.uint8)#建立兩個模擬圖像，數值0~255
img2=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
print('img1=\n', img1)
print('img2=\n', img2)
img3=cv.add(img1,img2)
print('cv.add(img1+img2)=\n', img3)


