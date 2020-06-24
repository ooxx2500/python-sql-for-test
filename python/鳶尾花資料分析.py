# -*- coding: utf-8 -*-
"""
鳶尾花(Iris)資料分析 
數據分布中有的資料集
為加州大學爾灣分校作為機器學習(machine learning)之常用資料集
數據資料150筆 包含以下
資料: 花萼長度 (speal length)
      花萼寬度 (speal width)
      花瓣長度 (petal length)
      花半寬度 (petal width)
類別: (species setosa versicolor virginica)
        種類    柔滑     雜色      維吉尼卡

鳶尾花專案:
    1.網頁資料擷取:
        下載資料轉成所需要的格式，如轉為pandas的dataframe轉存為CSV
        可先將資料讀取並印出了解資料內容包含的項目
    2.視覺化分析資料:
        繪製各式圖表
        直方圖:呈現不同區塊
        散點圖
    3.密度圖:
        將數據中估計的值方圖平滑化，每個單獨的數據匯至連續曲線,
        稱為內核(長用內核為高斯-鐘型取線)
    4.盒鬚圖:呈現數據分佈 
        圖型上下的一之間為區塊，超過部分為離散值
        盒子的上面是75%分位數
        綠線是50%分位數
        盒子的下面是25%分位數
    5.直條圖:三種品種各自的四個特徵
    6.堆疊圖:在總和不具重要性情況下，呈現個別資料與整體資料之間的關係及資料
            在特定時間範圍的變化趨勢
    7.橫條圖:類似直線圖
    8.由視覺畫圖表產生分析結論(報告)
        產生經營方向
        產品成本單項分析結果                        順序(都是演算法)
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
        
    10.以線性回歸分析鳶尾花資料集     
            
            
            
            
            
        

"""
#step1: 下載資料集並存為csv檔
import requests

url='http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
try:
    htmlfile = requests.get(url)
    print('下載成功')
except Exception as err:
    print('下載失敗',err)
    
fn = 'iris.csv'
with open(fn, 'wb') as fileobj:
    for diskstorage in htmlfile.iter_content(10240):
        size = fileobj.write(diskstorage)
        
---------------------------  
#setp2: 讀取csv並轉換為DataFrame      
import pandas as pd

colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv(r'C:\Users\ASUS\Documents\Python-SQL\python\iris.csv',
                   names=colName)
print('資料集長度 :',len(iris))   
print(iris)
s = iris.describe() #數量
#std:標準差 25,50,75% 分位數
#min:最小值 max:最大直
print(s)     
        
----------------------------
#step3:資料視覺化(直方圖)
import pandas 
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'      
names = ['sepal-length','sepal-width','petal-length','petal-width','class']       
dataset = pandas.read_csv(url, names=names) 
print(dataset.describe())
dataset.hist() 
--------------------------
#sep4:畫散點圖(花萼的長寬分析)
import pandas 

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'      
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
#將鳶尾花的特徵轉為串列       
dataset = pandas.read_csv(url, names=names) 
print(dataset.describe())#describe取得數量
dataset.plot(x='sepal-length',y='sepal-width',kind='scatter')#種類scatter散點(佈)圖
#散佈圖:呈現X Y軸的兩個變數之間的變化，某一個變數是否受另一個變數的影響(必須要有兩組變數)
#散點圖的資料點的散佈型態越趨近於直線，代表兩個變數之間的關聯性越高(正相關)
#散點突如果越分散，代表兩圖沒啥相關      

------------------------
#sep5 密度圖(核密度估計圖)
#呈現每一組數據本身的分布狀況
#X軸為變量的值每一個值代表一個數據點
#Y軸為核估計之機率密度函數
import pandas 
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'      
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
     
dataset = pandas.read_csv(url, names=names) 
print(dataset.describe())
dataset.plot(kind='kde') #kde核密度估計圖    
        
---------------------------        
#盒鬚圖(箱型圖,K線圖)  
import pandas       
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'      
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
     
dataset = pandas.read_csv(url, names=names) 
print(dataset.describe())
dataset.plot(kind='box',subplots=True,layout=(2,2), 
sharex=False, sharey=False) #box=盒鬚圖 subplot=繪子圖 layout=(2row,2column)     
#sharex = True(每一個子圖是否要共用X Y座標，預設是false)        
        
----------------------------------
#用plt畫散佈圖 (不同的點用花萼長 寬標記色彩)       
import pandas as pd
import matplotlib.pyplot as plt
colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv(r'C:\Users\ASUS\Documents\Python-SQL\python\iris.csv', names = colName)
           
plt.plot(iris['sepal_len'],iris['sepal_wd'],'*',color='g')#x資料 y資料 線型圖案'*' 顏色
plt.xlabel('sepal length')        
plt.ylabel('sepal width') 
plt.title('Iris sepal length and width anslysis')
plt.show()         
--------------------------------
#直線圖        
import pandas as pd
import matplotlib.pyplot as plt
colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv(r'C:\Users\ASUS\Documents\Python-SQL\python\iris.csv', names = colName)

iris_mean = iris.groupby('species',as_index=False).mean()#.mean():均值
#groupby分組(依據品種,as_index=False用原標題)
print(iris_mean)
iris_mean.plot(kind='bar')
plt.xticks(iris_mean.index, iris_mean['species'], rotation=10)
#.xticks(設定X軸的刻度為品種名稱:,rotation=刻度旋轉幾度)
plt.show()         
        
--------------------------------------------------
#ex:練習分組
import pandas as pd

df=pd.DataFrame(data={'book':['b1','b1','b1','b2','b2','b3'],
                      'price':[12,12,12,15,15,17]})
print(df)
print()
print(df.groupby('book',as_index=True).sum())
print()
print(df.groupby('book',as_index=False).sum())
gb=df.groupby('book',as_index=False)
print(gb.get_group('b1'))
---------------------------------------------
#畫值線圖 將Iris取代掉(不同品種的花萼花瓣的長寬)
import matplotlib.pyplot as plt
import pandas as pd
colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv(r'C:\Users\ASUS\Documents\Python-SQL\python\iris.csv', names = colName)

iris['species']=iris['species'].apply(lambda x: x.replace('Iris-',''))
#.apply(方法 lambda:)
#lambda:用在跌代，用在迴圈重複執行的動作用在一行
iris_mean = iris.groupby('species',as_index=False).mean()#.mean():均值
print(iris_mean)
iris_mean.plot(kind='bar')
plt.xticks(iris_mean.index, iris_mean['species'], rotation=10)
plt.show()         

---------------------------------------------
#繪製堆疊圖(容易看出各資料間的占比)不同品當中的花瓣花萼長寬的關係
import matplotlib.pyplot as plt
import pandas as pd
colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv(r'C:\Users\ASUS\Documents\Python-SQL\python\iris.csv', names = colName)
iris['species']=iris['species'].apply(lambda x: x.replace('Iris-',''))
iris_mean = iris.groupby('species',as_index=False).mean()#.mean():均值
print(iris_mean)
iris_mean.plot(kind='bar',stacked=True)#True設定為堆疊圖
plt.xticks(iris_mean.index, iris_mean['species'], rotation=10)
plt.show()  

---------------------------------
#橫條圖(沒堆疊)
import matplotlib.pyplot as plt
import pandas as pd
colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv(r'C:\Users\ASUS\Documents\Python-SQL\python\iris.csv', names = colName)
iris['species']=iris['species'].apply(lambda x: x.replace('Iris-',''))
iris_mean = iris.groupby('species',as_index=False).mean()#.mean():均值
print(iris_mean)
iris_mean.plot(kind='barh')#True設定為堆疊圖 barh=橫條圖
plt.yticks(iris_mean.index, iris_mean['species'], rotation=10)
plt.show() 
-------------------------------
#堆疊橫條圖
import matplotlib.pyplot as plt
import pandas as pd
colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv(r'C:\Users\ASUS\Documents\Python-SQL\python\iris.csv', names = colName)
iris['species']=iris['species'].apply(lambda x: x.replace('Iris-',''))
iris_mean = iris.groupby('species',as_index=False).mean()#.mean():均值
print(iris_mean)
iris_mean.plot(kind='barh',stacked=True)#True設定為堆疊圖
plt.yticks(iris_mean.index, iris_mean['species'], rotation=10)
plt.show() 

---------------------
#載入Iris資料集
from sklearn.datasets import load_iris
hua = load_iris()#將資料集指定給hua

x=[n[0] for n in hua.data]#取得花瓣的長[0]
y=[n[1] for n in hua.data]#取得花瓣的寬[1]

import numpy as np
x=np.array(x).reshape(len(x),1) #將串列轉換維陣列，因訓練時fit需要用陣列
y=np.array(y).reshape(len(y),1) #將串列轉換維陣列

from sklearn.linear_model import LinearRegression
                    #線性模型 import 線性回歸
clf = LinearRegression()
clf.fit(x,y)#fit()資料型態需要維陣列(fit():訓練機器)
pre = clf.predict(x)#預測資料

import matplotlib.pyplot as plt
plt.scatter(x,y,s=100)
plt.plot(x,pre,'r-',linewidth=4)#畫出紅線 看相關趨勢
for idx, m in enumerate(x):#
    plt.plot([m,m],[y[idx],pre[idx]],'g-')#畫出綠線
    
#若有依花萼長為5.0請問寬度是多少?
print(clf.predict([[5.0]]))    





















        