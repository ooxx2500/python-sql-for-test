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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        