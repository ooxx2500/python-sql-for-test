# -*- coding: utf-8 -*-
"""
    9.以不同的方式進行細部分析                      人工智慧(AI)
        機器學習machine learning                 機器學習
        機器學習套件 scikit-learn(sklearn)        深度學習
        電腦藉由經驗去累積去提高自動化效能
        
    scikit-learn:Numpy pandas scipy matplotlib(包含)
    功能:
        測試資料:
        特徵篩選:
        特徵提取:
        聚類(把沒標記的資料分類):
        演算法(監督式 非監督式學習):
        驗證(交叉):
    scikit-learn常用演算法:
        分類:Classification
        回歸:Regression    
        聚類:Clustering    
            
            
"""
#機器學習套件 scikit-learn(sklearn)
#由sklearn套建載入datasets模組並讀入digits資料
from sklearn import datasets
digits = datasets.load_digits()
print(digits)
--------------------------------
import pandas as pd

digits = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/"
                     "optdigits.tra",header=None)
print(digits)#載入數字檔

-----------------------
#讓機器辨識數字
from sklearn import datasets
import matplotlib.pyplot as plt

digits = datasets.load_digits()

fig = plt.figure(figsize=(4,2))#設定一個長4寬2(4欄2列)的繪圖大小

fig.subplots_adjust(left=0, right=1, bottom=0, hspace=0.05, wspace=0.05)
#繪製並調整子圖(左 右 上 下 高度間距 水平間距參數)
for i in range(8):
    ax = fig.add_subplot(2, 4, i+1, xticks=[], yticks=[])
    #add_subplot(2row, 4column, 位置,x座標刻度,y座標刻度)
    ax.imshow(digits.images[i], cmap=plt.cm.binary)
    #ax.畫出digits.images數字(digits10個相異值0~9) cmap=設定色彩灰階
    ax.text(0,7,str(digits.target[i]))#.text加入文字
                 #digits.target[i] 目標值(10個相異值0~9)
plt.show()


-------------------------------
#
from sklearn import datasets
import matplotlib.pyplot as plt
digits = datasets.load_digits()
images_and_labels=list(zip(digits.images, digits.target))
#將觀測值及目標值放入list裡，透過迴圈將list把元素通通抓出來
for i ,(image, label) in enumerate(images_and_labels[:8]):
#  
    plt.subplot(2,4,i+1)
    plt.axis('off')#關閉子圖刻度
    plt.imshow(image, cmap=plt.cm.binary)#灰階
    plt.title('Training: '+str(label))
plt.show()














