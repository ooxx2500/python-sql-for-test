# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 16:45:13 2020

@author: ASUS
"""

data=[]
import json
from matplotlib import pyplot as plt
import pandas as pd
font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '12'}#設定字形樣式大小
plt.rc('font', **font) #設定PY繪圖系統的字型項目
plt.rc('axes',unicode_minus=False) #座標軸如果有負號再加上此參數就可解決
with open(r'C:\Users\ASUS\Desktop\109A1.json',encoding = 'utf8')as file:
    rf_1 = json.load(file)
    
    
rf=pd.DataFrame(rf_1,columns=['發生地點','發生時間','車種','經度'])

print(rf['經度'])
rf['經度']=rf['經度'].dropna()
print(rf['經度'])
rf['經度']=rf['經度'].astype(float)