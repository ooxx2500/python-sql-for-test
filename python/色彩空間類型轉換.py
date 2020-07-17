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