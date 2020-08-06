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

-------------------------------

PDFㄉ
------------------------------
#線性回歸
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

temperatures = np.array([29,28,34,31,25,29,32,31,24,33,25,31,26,30])
                      
drink_sales = np.array([7.7, 6.2, 9.3, 8.4, 5.9, 6.4, 8.0, 7.5, 5.8,9.1,5.1,7.3,6.5,8.4])

X = pd.DataFrame(temperatures, columns=[ 'Temperature' ])
y= pd.DataFrame(drink_sales, columns=["Drink_SaLes"])

lm = LinearRegression()
lm.fit(X,y) 
print('回歸係數:',lm.coef_)   #算出回歸係數
print('截距:',lm.intercept_)  #算出截距
#預測器溫26,30度的業績
new_temperatures = pd.DataFrame(np.array([26,30]))
predicted_sales= lm.predict(new_temperatures)
print(predicted_sales) #預測銷售

plt.scatter(temperatures,drink_sales) #繪圖
regression_sales=lm.predict(X)
plt.plot(temperatures,regression_sales,color='blue')
plt.plot(new_temperatures,predicted_sales ,color='red',marker='o',markersize=10)
plt.show()

----------------------------------------------------

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
waist_height = np.array([[67,160],[68,165],[70,167,],[65,170],[80,165],
                         [85,167],[78,178],[79,182],[95,175],[89,172]])
weights=np.array([50,60,65,65,70,75,80,85,90,81])
x = pd.DataFrame(waist_height, columns=[ 'Waist','Height' ])
y= pd.DataFrame(weights, columns=["Weight"])

lm=LinearRegression()
lm.fit(x,y)
print('回歸係數:',lm.coef_)   #算出回歸係數
print('截距:',lm.intercept_)
#預測身高66 164 82 172的體重
new_waist_heights=pd.DataFrame(np.array([[66,164],[82,172]]))
predicted_weights=lm.predict(new_waist_heights)
print(predicted_weights)



-----------------------------------------------------
#資料集
from sklearn import datasets
#botson, dialbetes 主要用於回歸
boston = datasets.load_boston()
dialbetes = datasets.load_diabetes()

#iris, digits主要用在分類
iris = datasets.load_iris()
digits = datasets.load_digits()

print(boston.keys())
print(diabetes.keys())
print(iris.keys())
print(digits.keys())

print(boston.data.shape) #506,13  506筆13欄位
print(boston.feature_names) #資料欄位名稱在feature_names
print(boston.DESCR) #欄位描述
----------------------------------------------
#將boston資料及作成PD印出來
from sklearn import datasets
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

boston = datasets.load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
print(X.head())

#建立應變數Y的DataFrame物件
target = pd.DataFrame(boston.target, columns=['MEDV']) #自定義欄位名稱為MEDV
print(target.head())
y=target['MEDV']

lm = LinearRegression()
lm.fit(X,y)
print("回歸係數:", lm.coef_)
print("截距:", lm.intercept_)

#上述回歸係數因有13個解釋變數，所以有13個係數，我們可以建立DF物件來顯示每個特徵
coef=pd.DataFrame(boston.feature_names, columns=['features'])
coef['estimatedCoefficients']=lm.coef_ #在df中新增依欄位
print(coef)
#從上圖可以發現RM相關係數最高  RM 3.809865 
#RM與房價高度正相關繪製散佈圖
plt.scatter(X.RM, y)  
plt.xlabel('avg number of rooms per dwelling(RM)')
plt.ylabel('price (MEDV)')
plt.title('Relotionship between RM and price')
plt.show()

--------------------------------------------
#使用train_test_spoilt()函數隨機分割資料集
from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

boston = datasets.load_boston()
X=pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])
y=target['MEDV']

Xtrain, Xtest, ytrain, ytest= train_test_split(X, y ,test_size=0.33, random_state=5)

lm =LinearRegression()
lm.fit(Xtrain, ytrain)
pred_test=lm.predict((Xtest))
pred_train=lm.predict(Xtrain)
plt.scatter(ytest, pred_test)
plt.xlabel('price')
plt.ylabel('predicted price')
plt.title('price vs predicted price')
plt.show()

MSE_train = np.mean((ytrain - pred_train)**2)
MSE_test = np.mean((ytest - pred_test)**2)

print('訓練資料的MSE:', MSE_train)
print('訓練資料的MSE:', MSE_test)

print('訓練資料的R-squared', lm.score(Xtrain, ytrain))
print('訓練資料的R-squared', lm.score(Xtest, ytest))


-----------------------------------------
#訓練和測試資料集
from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


boston = datasets.load_boston()
X=pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])
y=target['MEDV']

lm =LinearRegression()
lm.fit(X, y)
predicted_price = lm.predict(X)
print(predicted_price[0:5])
MSE = np.mean((y-predicted_price)**2)
print('MSE',MSE)
print('R-squared:',lm.score(X,y))

