'''
numpy模組:建立資料矩陣

numpy.linspace:產生間隔數列
    格式numpy.linspace(起始,終止,數量,其他參數)
    
'''

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])#建立一個np陣列(2*3的矩陣)
print(arr)

ran_arr=np.random.random((4,2))#建立4*2隨機矩陣 0~1
print(ran_arr)
---------------------------------

import numpy as np
a = np.floor(5*np.random.random((2,12)))
print(a)

'''
資料視覺化:繪圖
Matplotlib模組:
    大多繪圖功能放在matplotlib.pyplot中
    主要功能:繪製 x , y 座標圖(通常x,y放在串列中傳給Matplotlib)
繪圖方法:
    模組名稱.plot(x座標串列,y座標串列)
    plot(參數):color = '色碼表'
              linewidth=5 線寬 預設為1
              lw = 3 線寬的縮寫
              linestyle='--':虛線  '-':實線  '-.':點虛線  ':'點線 
              ls = '--' 同上
              label = 'Female' 線的標籤名稱

'''
#用Matplotlib繪圖
import matplotlib.pyplot as plt

listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
plt.plot(listx,listy)
plt.show() #顯示繪圖

--------------------------------------
#繪製雙線圖
import matplotlib.pyplot as plt

listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]
plt.plot(listx1 , listy1 ,label = 'Male',lw =3,ls = ':',color = 'green')
#lw 線寬縮寫 ls 線的外型縮寫
listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]
plt.plot(listx2 , listy2 ,linewidth=5,linestyle='--',label = 'Female',color ='#FF00FF')
        #linewidth=5線寬 預設為1 linestyle='--'虛線 label = 'Female' 線的標籤名稱
plt.legend() #顯示線的label名子(圖例),有label沒寫這行是不會顯示的
plt.xlim(0,20) #設定X軸的範圍,沒設定系統也會自動設
plt.ylim(0,100) #設定Y軸的範圍,沒設定系統也會自動設
plt.title('Pocket Money')#圖表的標題
plt.xlabel('age')#x座標標題
plt.ylabel('Money')#y座標標題
plt.show()

---------------------------------
#畫出波型圖
import matplotlib.pyplot as plt
import numpy as np
x= np.arange(0, 3 * np.pi ,0.1)
#np.arrange= np的範圍 0開始到3*pi 間格為0.1
y = np.sin(x)
print(x)
print(y)
plt.title('sine wave form')
plt.plot(x,y)
plt.show()


----------------------------
#畫出4格圖表
import matplotlib.pyplot as plt

plt.figure() #繪圖畫面中可以再容納多個小圖形

plt.subplot(2,2,1) #此圖形位置1(左上)  subplot(列數,欄數,位置)
plt.plot([0,1],[0,1])

plt.subplot(2,2,2) #此圖形位置2(右上)
plt.plot([0,1],[0,2])

plt.subplot(2,2,3) #此圖形位置3(左下)
plt.plot([0,1],[0,3])

plt.subplot(2,2,4) #此圖形位置4(右下)
plt.plot([0,1],[0,5])
plt.show()


'''
柱狀圖 格式:模組名稱.bar(x座標,y座標,其他參數)
    參數:align='center' 直條對齊坐標刻度   align='edge' 對齊刻度邊緣
        width:直條寬度
    



'''
#繪製柱狀圖
from matplotlib import pyplot as plt
x=[5,8,10]
y=[12,16,6]
x2=[6,9,11]
y2=[6,15,7]
plt.bar(x,y,align='edge')#align='center' 直條對齊坐標刻度 align='edge' 對齊刻度邊緣
plt.bar(x2,y2,color = 'g',align='center')
plt.title('Var graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()


-------------------
#兩組住狀圖重疊變成分開排列 ***align='edge' width=一個正值一個負值
import matplotlib.pyplot as plt
x=['bk','sw','ph','rd','gu']
a=[8,7,1,6,5]
b=[12,2,9,5,3]
plt.bar(x,a,label='a',align='edge',width=0.3) #在對齊為邊緣下,width正值靠右,負值往左
plt.bar(x,b,label='b',align='edge',width=-0.3)
plt.legend()


----------------------

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,11)
y = 2*x+5
print(x)
print(y)
#用numpy產生的串列x y

plt.title('Matplotlib demo')
plt.xlabel('x axis caption')
plt.ylabel('y axis caption')
plt.plot(x,y,lw=2,color = 'b',ls='-.')
plt.show()

--------------------------
#用numpy產生數列畫圖
import numpy as np
import matplotlib.pyplot as plt
x= numpy.linspace(-1,1,50)
y1=2*x+1
y2=x**2
plt.plot(x,y1,ls='--')
plt.plot(x,y2)
plt.show()
--------------
#設定線條圖形顏色
import numpy as np
import matplotlib.pyplot as plt
x= numpy.linspace(-1,1,20)
y1=2*x+1
y2=x**2
plt.plot(x,y1,'ob') #o:圖標記 o:圓形 p:五邊型 s:正方形 x:十字 v:倒三角 ^:正三角 *:星型 h:六邊型 H:六邊型
                    #b:顏色 b:藍色 r:紅 g:綠 y:黃 w:白 k:黑 c:青 m:洋紅
plt.plot(x,y2)
plt.show()

'''
圓形圖:最適合統計一組數據，適合表達數據的百分比
  格式:模組名稱.pie(資料串列,其他參數)~預設為橢圓形
  參數:labeldistance:資料標籤與圓心的距離是半徑的幾倍
      shadow:設定陰影
      startangle:繪圖的起始角度(逆時針旋轉為正)
      pctdistance:百分比文字與圓心的距離是半徑的幾倍
      explore:設定圓型分離區塊的距離以串列設定對應至資料項目 
      

'''
#畫圓餅圖
import matplotlib.pyplot as plt

labels ='A','B','C','D','E','F' #在PY視為一個元祖
size = [33,52,12,17,62,48]
print(labels)
plt.pie(size , labels = labels , autopct='%1.1f%%') #autopct='%1.1f%%' 數值百分比
plt.axis('equal') #x軸比例相等  autopct格式: %格式%% 後面兩個%沒意義但是要加
plt.show()

-------------------------------------
#圓餅圖 修改顯示中文
import matplotlib.pyplot as plt

#以下三行是PY專用顯示中文的，沒加會沒辦法顯示中文
font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '16'}#設定字形樣式大小
plt.rc('font', **font) #設定PY繪圖系統的字型項目
plt.rc('axes',unicode_minus=False) #座標軸如果有負號再加上此參數就可解決

labels = ['東部','南部','北部','中部']
sizes=[5,10,20,15]
colors = ['red','green','blue','yellow']
explode = (0.05,0,0,0) #0表示未分離 
plt.pie(sizes , explode = explode , labels=labels , colors = colors,\
        labeldistance = 1.1 , autopct='%3.1f%%', shadow=True ,\
        startangle = 90 , pctdistance = 0.7) #startangle 逆時針旋轉為正
plt.axis('equal')
plt.legend(loc = 'lower right',fontsize=10) #只定圖例出現在右下位置 fontsize改圖例字體大小
plt.show()

----------------------------
'''
資料視覺化:繪圖
    散布圖:scatter 

'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

np.random.seed(20180731) #設定亂數種子

x =np.arange(0.0,50.0,2.0)  #np.random.rand(裡面要整數)  *x.shape用來轉化數值為int
y =x**1.3 +np.random.rand(*x.shape)*30.0 #x產生的直若為浮點(非整數)
s =np.random.rand(*x.shape)*800+500
print(x)
print(y)
print(s) #x,y數據  s:數量的格式(數量越大圖章越大)
plt.scatter(x ,y , s, c='g', alpha=0.5,label='Luck', marker=r'$\clubsuit$')
#c:顏色 alpha:透明度 marker:圖形
plt.xlabel('Leprechauns')
plt.ylabel('Gold')
plt.legend(loc=2)
plt.show()


---------------------------------
#散布圖s數量都相等150
import matplotlib.pyplot as plt
x = [1,2,4,6,8,1,2,9,3]
y = [5,7,2,3,1,4,6,5,8]
plt.scatter(x,y,s=[150 for i in range(len(x))],c='r',alpha = 0.5)
plt.title('scatter simple')
plt.xlabel('x axes')
plt.ylabel('y axes')    
plt.show()

#散布圖s數量隨機 大小就會不一樣
import matplotlib.pyplot as plt
x = [1,2,4,6,8,1,2,9,3]
y = [5,7,2,3,1,4,6,5,8]
plt.scatter(x,y,s=[random.randint(1,400) for i in range(len(x))],c='r',alpha = 0.5)
plt.title('scatter simple')
plt.xlabel('x axes')
plt.ylabel('y axes')    
plt.show()
-------------------------------
#讀取csv檔做成圖表
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates ,highs ,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],'%Y-%m-%d')
            high = (int(row[1])-32)*5/9
            low = (int(row[3])-32)*5/9
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            
fig = plt.figure(dpi=128 , figsize=(5,3))
plt.plot(dates , highs , c='r',alpha=0.5)            
plt.plot(dates , lows , c='b',alpha=0.5)  
plt.fill_between(dates , highs, lows, facecolor = 'blue', alpha=0.1)

title = 'Daily high and low temperatures -2014\nDeath Valley, CA'
plt.title(title, fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()          
plt.ylabel('Temperature (C)',fontsize=16)

plt.show()











