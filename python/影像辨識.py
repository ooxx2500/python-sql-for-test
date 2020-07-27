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

--------------------
import cv2 as cv
img=cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena.jpg',0)
a=img
result1=a+img
result2=cv.add(img,a)
cv.imshow('image',img)
cv.imshow('image1',result1)
cv.imshow('image2',result2)
cv.waitKey()


'''
影像加權和:
    計算影像像素值和並加入加權值計算
    使用函數:addWeighted
    addWeighted(src1,a,src2,b,c) 
    src1:影像1 src2影像2 a:影像1加權 b:影像2加權 c:亮度調節
    公式:src1*a+src2*b+c    
兩影像大小及類型必須相同
    ROI:Region Of Interest感興趣區域  
    於程式中自行設定所需要處理的區域範圍


'''
#影像加權練習
import cv2 as cv
import numpy as np
img1=np.ones((3,4,3),dtype=np.uint8)*100
img2=np.ones((3,4,3),dtype=np.uint8)*10
a=3
img3=cv.addWeighted(img1,0.6,img2,5,a)
print(img3)



-----------------------------------
#和成兩張圖片(大小類型必須一致)
import cv2 as cv

img1=cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg')
img2=cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\landscape512.jpg')
result = cv.addWeighted(img1, 0.6, img2, 0.4,0)
cv.imshow('image1',img1)
cv.imshow('image2',img2)
cv.imshow('image3',result)
cv.waitKey()

-------------------------------
#盒成兩張圖片(區域和成)
import cv2 as cv

img=cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\lena_01.jpg',1)
US1=cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\US1_600.jpg',1)
cv.imshow('image',img)
cv.imshow('banknote',US1)
img_face= img[80:230 , 250:370]#影像人臉ROI
US1_face= US1[80:230 , 240:360]#影像鈔票ROI
add= cv.addWeighted(img_face, 0.6, US1_face, 0.4, 0)#兩個ROI加全運算給add變數
US1[80:230, 240:360]=add #將加權後的影像加入鈔票的ROI區域
cv.imshow('result',US1)
cv.waitKey()

'''
逐位元邏輯運算
    bitwise_and:且
    bitwise_or:或
    bitwise_xor:互斥   
    bitwise_not:反向
and運算:
    兩個運算元(邏輯值)都為真，其結果為真
    
函數:bitwise_and
    bitwise_and(src1,src2)  兩個影像

任何數值n與數值0作and運算，結果都是0
    11011011
and 00000000
---------------
    00000000

任何數值n與數值255作and運算，結果為元素值n本身
    11011011
and 11111111
---------------
    11011011    

以上敘述定理可建立掩膜影像只有兩個值0,255







'''
#用numpy建立遠模影像做遠模運算
import cv2 as cv
import numpy as np
img1 =np.random.randint(0,255,(5,5),dtype=np.uint8)
img2 =np.zeros((5,5),dtype=np.uint8)
img2[0:3,0:3] = 255
img2[4,4] = 255      #img2就是遠模影像0 255
a = cv.bitwise_and(img1, img2) 
print('img1 = \n',img1)
print('img2 = \n',img2)
print('a = \n',a)

------------------------
#遠模運算(灰階)
import cv2 as cv
import numpy as np
img1 =cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg',0)
img2 =np.zeros(img1.shape,dtype=np.uint8)
img2[100:400,200:400] = 255   #100:400是Y軸  200:400是X軸
img2[100:500,100:200] = 255
print(img2) 
a = cv.bitwise_and(img1, img2) #and運算 255區域匯式原來的影像
cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.imshow('a',a)
cv.waitKey()

-------------------------
#遠模運算(彩色)
import cv2 as cv
import numpy as np                                    #和上面差別是0改成1
img1 =cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg',1)
img2 =np.zeros(img1.shape,dtype=np.uint8)
img2[100:400,200:400] = 255   #100:400是Y軸  200:400是X軸
img2[100:500,100:200] = 255
a = cv.bitwise_and(img1, img2) #and運算 255區域匯式原來的影像
print("img1.shape =",img1.shape)
print("img2.shape =",img2.shape)
cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.imshow('a',a)
cv.waitKey()
--------------------
'''
xor運算:兩個運算單元都不相同結果為真

函數:bitwise_xor
    bitwise_xor(src1,src2)
    
    11000110(198)
xor 11011011(219)    
-----------------
    00011101(29)    


or運算元:
    兩個運算元(邏輯值)有一個為真，結果為真

函數:bitwise_or
    bitwise_or(src1,src2)
    
not運算元:將元素反向

函數:bitwise_not
    bitwise_not(src)
    

add函數:add(src1,src2,mask)      mask:掩膜得特定範圍

'''

import cv2 as cv
import numpy as np                              
img1 =np.ones((4,4),dtype=np.uint8)*3
img2 =np.ones((4,4),dtype=np.uint8)*5
mask=np.zeros((4,4),dtype=np.uint8)#掩膜影像都是0
mask[2:4,2:4]=1 #將演模影像的特定範圍數值設為1
img3 =np.ones((4,4),dtype=np.uint8)*66

print('img1 = \n',img1)
print('img2 = \n',img2)
print('mask = \n',mask)
print('初值 img3 = \n',img3)
img3= cv.add(img1,img2,mask= mask)#將兩影像相加在用mask遮罩(and運算)
print('求和後 img3 = \n',img3)

-------------------------------
#用and 掩膜影像 遮罩圖片區域
import cv2 as cv
import numpy as np
img=cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg',1) 
w, h, c = img.shape
mask=np.zeros((w,h),dtype = np.uint8)
mask[100:400,200:400]=255
mask[100:500,100:200]=255                             
c=cv.bitwise_and(img,img,mask=mask)
print('img.shap=',img.shape)
print('mask.shap=',mask.shape)
cv.imshow('img',img)
cv.imshow('mask',mask)
cv.imshow('c',c)
cv.waitKey()


------------------------------------------
'''
位元平面分解

將灰階影像中同一個位元上的二進位像素值進行組合，可得到一個二進位影像，該影像稱為灰階
影像的位元平面，其組和過程稱為位元平面分解。

灰階影像中每一象素使用8位元，二進位值表示值的範圍為0-255表示為:
    a7*2**7 a6*2**6 a5*2**5 a4*2**4 a3*2**3 a2*2**2 a1*2**1 a0*2**0  a0-a7為0~1
    
    a7對影像影響最大，加權最高，其位元平面與元影像相關性最高，和原影像類似 
    a0對影像影響最小，加權最低，其位元平面與元影像相關性最低，該位元平面最雜亂
    
執行步驟:
    影像前置處理:
    建立分析矩陣:
    分析影像位元平面:
    設定值處理(逐位元邏輯運算):
    顯示影像:


'''
import cv2 as cv
import numpy as np
img=cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg',0)
cv.imshow('img',img) 
r, c = img.shape#讀取原本影像的大小寬高
x= np.zeros((r,c,8),dtype=np.uint8) #用寬高設定一個分析矩陣 8個通道

for i in range(8):
    x[:,:,i]=2**i#將分析矩陣設為2**i次方
r= np.zeros((r,c,8),dtype=np.uint8)

for i in range(8):
    r[:,:,i] = cv.bitwise_and(img, x[:,:,i])
    mask = r[:,:,i]>0
    r[mask]=255
    cv.imshow(str(i),r[:,:,i])

cv.waitKey()

'''
影像加密及解密
原始影像與金鑰影像:進行互斥運算，產生加密影像(encryption)

加密影像與金鑰影像:進行互斥運算，產生解密影像(decryption)

a:原始資料(明文) b:金鑰  c:加密(xor(a,b)) 
xor(a,b)=c, xor(c,b)=a

位元運算可實踐像素點加密，通常預處理的象素點為灰階值，如某項素點值為216(明文)，
以178(此值由加密者自行決定)做為加密金鑰，將此二數值進行互斥運算，加密後為106
bitwise_xor(216,178)=106 加密後
bitwise_xor(106,178)=216 解密後

    11011000(216)明文           01101010(106)
xor 10110010(178)金鑰       xor 10110010(178) 
-------------------        -------------------
    01101010(106)加密後         11011000(216)解密後 

'''
#影像加密及解密
import cv2 as cv
import numpy as np
img=cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg',0)
cv.imshow('img',img) 
r, c = img.shape#讀取原本影像的大小寬高
key = np.random.randint(0,256,size=[r,c],dtype=np.uint8)#用np產生隨機key
print(key)
encryption =cv.bitwise_xor(img, key) #將影像加密
decryption =cv.bitwise_xor(encryption, key) #將影像解密
cv.imshow('image',img)
cv.imshow('key',key)
cv.imshow('encryption',encryption)
cv.imshow('decryption',decryption)
cv.waitKey()

'''
浮水印(資訊影藏)
最低有效位(Least Significant Bit;LSB):二進位數字中的第D位(最低位)

將需要影藏的二值影像崁入載體影像的最低有效位，即將載體影像的LSB取代為需要影藏的二值影像
，以達到二進位影像影藏的目的。

因二值影像處於載體影像的LSB上，對載體影像影響非常明顯固有較高的影敝性

崁入過成
    1.將影像二值化(處理為灰階)灰階二值影像中像素值只有0,255，表示為黑色白色，
    2.將255轉為1可得到二進位的灰階影像，只用一個位元表達象素值
    


'''
#浮水印加密
import cv2 as cv
import numpy as np
img=cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg',0)
watermark =cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\watermark.jpg',0)
w =watermark[:,:]>0 #將灰階影像的值為255設定為1以方便嵌入
watermark[w]=1
r,c =img.shape

t254=np.ones((r,c),dtype=np.uint8)*254 #產生元素值為254的陣列
imgh7=cv.bitwise_and(img, t254)#取得影像的高7位
e=cv.bitwise_or(imgh7, watermark)#用or運算將watermark影像遷入裡面

t1=np.ones((r,c),dtype=np.uint8)
wm=cv.bitwise_and(e, t1)
print(wm)
w=wm[:,:]>0
wm[w] =255

cv.imshow('img',img)
cv.imshow('watermark',watermark*255)
cv.imshow('e',e)
cv.imshow('wm',wm)
cv.waitKey()



------------------------------------------

import cv2 as cv
import numpy as np
img=cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\Lena512.jpg',0)
r,c =img.shape
mask=np.zeros((r,c),dtype=np.uint8)
mask[100:400,200:400]=1
#取得key
key = np.random.randint(0,256,size=[r,c],dtype=np.uint8)
#使用打碼臉部影像，使用金鑰對原始影像加密
imgxorkey =cv.bitwise_xor(img, key) 
#取得加密臉部資訊
encryptFace=cv.bitwise_and(imgxorkey, mask*255)
#取得加密影像將臉部值設定為0
noface1=cv.bitwise_and(img, (1-mask)*255)
#取得打碼影像
maskface = encryptFace + noface1
#將打碼的臉解碼
#將臉部打碼的影像與金鑰進行互斥運算，取得臉部原始資訊
extractOriginal = cv.bitwise_xor(maskface, key)
#將解碼的臉部資訊分析extractOriginal
extractFace = cv.bitwise_and(extractOriginal, mask*255)
#從打碼的臉部影像分析沒有臉部的影像
noface2 = cv.bitwise_and(maskface, (1-mask)*255)
#取得解碼的影像
extracting =noface2+extractFace   



cv.imshow('img',img)
cv.imshow('mask',mask*255)
cv.imshow('1-mask',(1-mask)*255)
cv.imshow('key',key)
cv.imshow('imgxorkey',imgxorkey)
cv.imshow('encryptFace',encryptFace)
cv.imshow('noface1',noface1)
cv.imshow('maskface',maskface)
cv.imshow('extractOriginal',extractOriginal)
cv.imshow('extractFace',extractFace)
cv.imshow('noface2',noface2)
cv.imshow('extracting',extracting)
cv.waitKey()


"""
影像辨識(機器) 速度 準確(人臉 物品 文字)
影像分類器 載入影像進入辨識(差異:角度、方向、雜訊、面積、色彩)
    經影像處理運算，不同的演算即處理方法    各自特色(分類器)
    產生分類器(調整各參數)
    自行訓練分類>機器學習(深度學習)>各種機器/深度學習演算法

img.shape[0]:圖片亮度
img.shape[1]:圖片寬度
"""
#辨識圖像
import cv2 as cv
pict =r'C:\Users\ASUS\Documents\Python-SQL\python\figure\haarcascade_frontalface_default.xml'
faceCascade = cv.CascadeClassifier (pict)

 

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\face_trump01.jpg')
faces=faceCascade.detectMultiScale(img,scaleFactor=1.1,
minNeighbors=2, minSize=(20,20), flags = cv.CASCADE_SCALE_IMAGE)

cv.rectangle(img, (10,img.shape[0]-20),
(110,img.shape[0]), (0,0,0), -1)
cv.putText(img,"Find " + str(len(faces)) +" face!",
(10, img.shape[0]-5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h) ,(128,255,0),2)

cv.namedWindow("facedetect")
cv.imshow('facedetect',img)
cv.waitKey()
-----------------------------------------
#視窗可條大小
#img.shape[0]:圖片亮度
#img.shape[1]:圖片寬度
"""

辨識流程:
    設定分類器檔案(*.xml)路徑位置
    建立分類器物件(載入上述位置)
    讀入待變式影像
    由分類器物件執行預測影像(人臉)
    繪製圖型編著偵測的影像範圍   
"""
import cv2 as cv
pict =r'C:\Users\ASUS\Documents\Python-SQL\python\figure\haarcascade_frontalface_default.xml'
faceCascade = cv.CascadeClassifier (pict)#建立分類器物件
img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\person_3.jpg')
#讀取待辨識影像
faces=faceCascade.detectMultiScale(img,scaleFactor=1.3,
minNeighbors = 2, minSize=(20,20))
#參數查影像
cv.rectangle(img, (img.shape[1]-140, img.shape[0]-20),
(img.shape[1],img.shape[0]), (0,255,255), -1)
#傳回預測的範圍
#標註區域找影像的範圍
cv.putText(img, "Finding " + str(len(faces)) + " face",
(img.shape[1]-135, img.shape[0]-5),

cv.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)

for (x,y,w,h) in faces:   #把人臉框起來(位置 x,y) 大小寬高(w,h)
    cv. rectangle(img, (x,y), (x+w, y+h) , (255,0,0) ,2) #畫矩形

cv.namedWindow("face")
cv.imshow('face',img)
cv.waitKey()

----------------------------------------
#影像辨識+辨視眼睛(可以換其他分類器抓)
import cv2 as cv
pict =r'C:\Users\ASUS\Documents\Python-SQL\python\figure\haarcascade_frontalface_default.xml'

face_cascade = cv.CascadeClassifier(pict)

eyepict = r'C:\Users\ASUS\Documents\Python-SQL\python\figure\haarcascade_mcs_nose.xml'
               #想抓其他的改上面的分類器xml檔路徑
eye_cascade = cv.CascadeClassifier(eyepict)

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\lena_01.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(img,scaleFactor=1.15,
minNeighbors=10, minSize=(20,20))

for (x,y,w,h) in faces: #先找出臉
    cv. rectangle(img, (x,y), (x+w, y+h) , (255,0,0) ,2) #畫矩形
    roi_gray=gray[y:y+h, x:x+w]
    roi_color=img[y:y+h, x:x+w]
    
    eyes=eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:#在找眼睛
        cv.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh) , (0,255,0) ,2)
cv. imshow('img' ,img)
cv.waitKey()
----------------------------------
#框圖像並存檔
import cv2 as cv
from PIL import Image
casc_path =r'C:\Users\ASUS\Documents\Python-SQL\python\figure\haarcascade_frontalface_default.xml'
faceCascade =cv.CascadeClassifier(casc_path)
imagename=r'C:\Users\ASUS\Documents\Python-SQL\python\figure\person_8.jpg'
image=cv.imread(imagename)
faces=faceCascade.detectMultiScale(image,scaleFactor=1.3,
minNeighbors=1, minSize=(30,30), flags = cv.CASCADE_SCALE_IMAGE)


count=1
for (x,y,w,h) in faces: 
    cv.rectangle(image, (x,y), (x+w,y+h), (128,255,0), 2)
    filename=str(count)+'.jpg'
    image1=Image.open(imagename)
    image2 = image1.crop((x, y, x+w, y+h)) #.crop材切 .resize重置大小
    image3 = image2.resize((200, 200), Image. ANTIALIAS) #.ANTIALIAS 影像最佳化
    res=r'C:\Users\ASUS\Documents\Python-SQL\python\figure\face'+filename
    image3.save(res)    
    count+=1

cv.namedWindow('facedetect')
cv.imshow('facedetect', image)
cv.waitKey()

-----------------------------------
#框圖像並存檔 
import cv2 as cv
from PIL import Image
pictPath = r'C:\Users\ASUS\Documents\Python-SQL\python\figure\haarcascade_frontalface_default.xml'
face_cascade = cv.CascadeClassifier(pictPath)

img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\person_8.jpg')

faces=face_cascade.detectMultiScale(img,scaleFactor=1.1,
minNeighbors=5, minSize=(10,10))

cv.rectangle(img, (img.shape[1]-140, img.shape[0]-20),
(img.shape[1],img.shape[0]), (0,255,255), -1)

cv.putText(img, 'Finded ' + str(len(faces)) + ' face',
           (img.shape[1]-135,img.shape[0]-5),
cv.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)

num=1

for (x,y,w,h) in faces: 
    cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    filename=str(num)+'.jpg'
    image=Image.open(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\person_8.jpg')
    imageCrop = image.crop((x, y, x+w, y+h)) #.crop材切 .resize重置大小
    imageResize = imageCrop.resize((150, 150), Image. ANTIALIAS) #.ANTIALIAS 影像最佳化
    res=r'C:\Users\ASUS\Documents\Python-SQL\python\figure\newface'+filename
    imageResize.save(res)    
    num+=1


cv.imshow('Face', img)
cv.waitKey()

---------------------------------
#辨識人臉加上5官
import cv2 as cv
face_cascade = cv.CascadeClassifier(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\haarcascade_eye.xml')
mouth_cascade = cv.CascadeClassifier(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\haarcascade_mcs_mouth.xml')
nose_cascade = cv.CascadeClassifier(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\haarcascade_mcs_nose.xml')
leftear_cascade = cv.CascadeClassifier(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\haarcascade_mcs_leftear.xml')
rightear_cascade = cv.CascadeClassifier(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\haarcascade_mcs_rightear.xml')
img = cv.imread(r'C:\Users\ASUS\Documents\Python-SQL\python\figure\lena_01.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#face detect
faces=face_cascade.detectMultiScale(gray,scaleFactor=1.2, minNeighbors=3)
for (x, y, w, h) in faces:

    img = cv.rectangle(img, (x,y),(x+w, y+h), (255, 0, 0), 2)
    roi_gray=gray[y:y+h, x:x+w]
    roi_color=img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray,scaleFactor=1.2,minNeighbors=3,minSize=(30,30))
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    mouth=mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.2,minNeighbors=3,minSize=(10,10))
    for (mx, my, mw, mh) in mouth:
        cv.rectangle(roi_color, (mx, my), (mx+mw, my+mh), (0, 0, 255), 2)
        
        
    nose = nose_cascade.detectMultiScale(roi_gray,scaleFactor=1.2,minNeighbors=5,minSize=(30, 30) )
    for (nx, ny, nw, nh) in nose:
        cv.rectangle(roi_color, (nx, ny), (nx+nw, ny+nh), (255, 0, 255), 2)
    
    leftear = leftear_cascade.detectMultiScale(roi_gray,scaleFactor=1.01,minNeighbors=2, minSize=(30,30))
    for (lx, ly, lw, lh) in leftear:
        cv.rectangle(roi_color, (lx, ly), (lx+lw, ly+lh), (0, 0, 0), 2)
    
    rightear = rightear_cascade.detectMultiScale(roi_gray,scaleFactor=1.01,minNeighbors=2, minSize=(30,30))
    for (rx, ry, rw, rh) in rightear:
        cv.rectangle(roi_color, (rx, ry), (rx+rw, ry+rh), (0, 0, 0), 2)
cv.imshow('img', img)
cv.waitKey()


