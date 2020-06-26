# -*- coding: utf-8 -*-

#Series物件的值是索引   
import pandas as pd

ss = pd.Series([5,10,15,20,25,30])
print(ss)
print(25 in ss)
print(0 in ss)
ss2 = pd.Series([6,10,15,20,25,30],index=[9,8,7,6,5,4])
print(10 in ss2)
print(4 in ss2)

---------------------------------

import pandas as pd
data={'name':['mona','judy'],'year':[1996,1997],'day':[10,20]}
mona in dara
'''
pandas模組(資料存取)
  主要結構:panel , dataframe , series (命名的由來)

  功能:專為python編寫的外部模組，執行數據處理與分析
        自動讀取網頁表格資料   
        匯入外部資料
        資料修改
        資料排序
        繪製圖表
        
    
  dataframe:pandas資料儲存型態
           為一個二維資料結構.，可以存放整數、浮點數、字串、PY物件
           
    格式:pandas.DataFrame(data, index, dtype, name)        

寫入csv檔:csv(comma separated valus)  
  方法:以to_csv方法將dataframe物件寫入csv
      格式:to_csv(path, sep, header, index, encoding)
      
    [檔案路徑，分隔符號(預設逗號)，是否保留header,是否保留index(預設True),檔案編碼]
    
讀取csv檔:read_csv()用Dataframe物件讀取csv檔
  格式:read_csv(path, sep, header, encoding, index_col, usecols, nrows)
     (路徑，設定哪一個row為欄位標籤，編碼，欄位column索引，讀取欄位，讀取列)



  series:一維資料結構(類似二維)
         可以存放整數、浮點、字串、python物件
         類似python list 具有索引結構

    格式:pandas.series(data , index , dtype ,name) 
    
    方法:concat():資料合併，參數axis(預設為0)預設為直向排列
                 axix=1，顯示索引對上的data一個欄column就是一個series資料
        columns:資料.columns=columns名稱
        name:series資料.name=名稱 (資料在concat時以名稱作為column名) 

繪圖:將數據建立為Series以Pandas繪圖，繪圖使用plot()方法

    畫圓餅圖:只能一組數據，數值格式化百分比(autopct %格式%%),切開圓形圖(explode)
   

'''

----------------------------
#建立DataFrame data為[字典]的串列 (串列橫向排列)
import pandas as pd
data=[{'apple':50,'orange':30,'grape':80},{'apple':50,'grape':80},{'noma':5}]
#字典的key若無對應，則對應處將填入NaN
index=['lst1','lst2','lst3']
fruits = pd.DataFrame(data,index=index)
print(fruits)
--------------------------
#建立DataFrame 直接用字典建立(字典直向排列)
import pandas as pd
cities = {'country':['China','Japan','Singapore'],#key=column標題 
          'town':['Beijing','Tokyo','Singpore'],  #value=欄位資料(直向排列)
          'population':[2000,1600,600]}
ditydf = pd.DataFrame(cities)
print(ditydf)

------------------------------------
#用index設定row名稱  DataFrame(data, index, dtype, name)  
import pandas as pd
cities = {'country':['China','Japan','Singapore'], 
          'town':['Beijing','Tokyo','Singpore'],  
          'population':[2000,1600,600]}
row_index = ['first','second','third'] #新增串列作為row標題
ditydf = pd.DataFrame(cities, index=row_index)
print(ditydf)

---------------------------------------
#用columns index只定顯示的欄列
import pandas as pd
cities = {'country':['China','Japan','Singapore'], 
          'town':['Beijing','Tokyo','Singpore'],  
          'population':[2000,1600,600]}
row_index = ['first','second','third'] #新增串列作為row標題
ditydf = pd.DataFrame(cities, columns = ['town','population'], index=cities['country'])
print(ditydf)        #把字典的元素設為index,不能用其他串列
----------------------------
#用numpy建立dataframe
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3,4))*0, columns=['x','y','z','s'])#用NP創造3row*4column
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['x','y','z','s'])#用NP創造3row*4column
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['x','y','z','s'])#用NP創造3row*4column
                
print(df1)
print(df2)
print(df3)

---------------------------
#用numpy.random.randint建立隨機串列
import pandas as pd
import numpy as np

name = ['Frank','Peter','John','mona']
score = ['first','second','final']
#用np.random建立3(row)*4(column)陣列，每一格的數據在60-99之間
df = pd.DataFrame(np.random.randint(60,100,size=(3,4)), columns=name, 
                  index=score)
print(df)



---------------------------------
#index = rows    
#匯入pandas模組建立表格並儲存成CSV檔
import pandas as pd   #設定pd便是就是pandas模組
datas= [[65,92,78,83,70],[90,72,76,93,56],[81,85,91,89,77],[79,53,47,94,80]]#二維資料
index = ['李大年','王大同','黃美娟','陳美玲'] #row
columns = ['國文','數學','英文','自然','社會'] #表格欄位 
df = pd.DataFrame(datas, columns = columns ,index = index) 
#帶入相關資料，建立DataFrame格式資料，參數colums=欄位名稱 index = row
print(df) 
df.to_csv(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\pdout.csv',encoding = 'utf-8-sig')  
#儲存方法 to_csv to_excel to_sql to_jason to_html (儲存為XX檔)



--------------------------------------------------
#pandas讀取方法 csv: read_csv
import pandas as pd
rd = pd.read_csv(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\pdout.csv',\
                 encoding = 'utf-8-sig',index_col = 0)#設定第一欄為index值
#讀取方法 read_csv read_excel read_sql read_jason read_html (讀取XX檔)
print(rd)



------------------------------
#pandas 寫入 csv: to_csv
import pandas as pd
course = ['chinese','english','math','natural','society']
chinese= [14,12,13,10,13]
eng = [13,14,11,10,15]
math= [15,9,12,8,15]
nature= [15,10,13,10,15]
social= [12,11,14,9,14]
df = pd.DataFrame([chinese,eng,math,nature,social], columns=course, 
                  index= range(1,6))
print(df)
df.to_csv(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\out_a.csv')
#a 將dataframe寫入csv
df.to_csv(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\out_b.csv', 
          header= False, index= False)
#b:不寫入header(column) index(row)


-------------------------------------
#pandas讀取csv檔
import pandas as pd

course = ['chinese','english','math','natural','society']
x =pd.read_csv(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\out_a.csv',
               index_col=0) #設定欄column索引
y =pd.read_csv(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\out_b.csv',
               names=course) #用參數names設定columns
print(x)
print(y)


-------------------------
#用pandas去畫圖 在pd.Series中index會畫成x軸,第一個參數串列會是y軸
import pandas as pd
import matplotlib.pyplot as plt

population = [860,1100,1450,1800,2020,2200,2260]
tw = pd.Series(population, index=range(1950,2011,10))
print(tw)
tw.plot(title = 'Population in TW')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()

------------------
#將數據建立為DataFrame以pandas繪圖
import pandas as pd
import matplotlib.pyplot as plt

cities = {'population':[1000,850,800,1600,600,800],
          'town':['new york','chicago','bangkok','tokyo','singapore','hongkong']}
tw = pd.DataFrame(cities)
print(tw)
print()
tw = pd.DataFrame(cities, columns=['population'],index=cities['town'])
print(tw)  #將row指定給towm  column指定給population
tw.plot(title= 'population in the world')
plt.xlabel('city')
plt.ylabel('Population')
plt.show()

---------------------------
#畫直線圖
import pandas as pd
import matplotlib.pyplot as plt

cities = {'population':[1000,850,800,1600,600,800],
          'town':['new york','chicago','bangkok','tokyo','singapore','hongkong']}

tw = pd.DataFrame(cities, columns=['population'],index=cities['town'])
print(tw)
tw.plot(title= 'population in the world',kind='bar')#參數bar就變成直條圖了
plt.xlabel('city')
plt.ylabel('Population')
plt.show()

-----------------------------
#用pandas畫兩條線
import pandas as pd
import matplotlib.pyplot as plt

cities = {'population':[1000,850,800,1500,600,800],
          'area':[400,500,850,300,200,320],
          'town':['new york','chicago','bangkok','tokyo','singapore','hongkong']}

tw = pd.DataFrame(cities, columns=['population','area'],index=cities['town'])
print(tw)                #欄為有兩條 可以畫出兩條線
tw.plot(title= 'population in the world',rot=45)#參數bar就變成直條圖了 rot=X軸座標轉45度
plt.xlabel('city')
plt.show()
-------------------------
#兩條線比例問題(不建議做法)
import pandas as pd
import matplotlib.pyplot as plt

cities = {'population':[10000000,8500000,8000000,15000000,6000000,8000000],
          'area':[400,500,850,300,200,320],
          'town':['new york','chicago','bangkok','tokyo','singapore','hongkong']}

tw = pd.DataFrame(cities, columns=['population','area'],index=cities['town'])
print(tw)                #欄為有兩條 可以畫出兩條線
tw.plot(title= 'population in the world')#參數bar就變成直條圖了
plt.xlabel('city')
plt.show()

------------------------------
#修改上例面積會顯示正常，多座標軸(建議做法)
import pandas as pd
import matplotlib.pyplot as plt

cities = {'population':[10000000,8500000,8000000,15000000,6000000,8000000],
          'area':[400,500,850,300,200,320],
          'town':['new york','chicago','bangkok','tokyo','singapore','hongkong']}

tw = pd.DataFrame(cities, columns=['population','area'],index=cities['town'])              #欄為有兩條 可以畫出兩條線
#fig:整體圖表物件
#ax:第一個軸(含X Y軸)
#subplot:在一個圖表中繪製不同軸的數據
fig, ax = plt.subplots()
fig.suptitle('city statistics')#設定子繪圖的標題
ax.set_ylabel('population')#設定y軸文字
ax.set_xlabel('city')#設定x軸文字
print(tw)
print()
ax2 = ax.twinx()#產生一個新軸
ax2.set_ylabel('Area')#設定新軸的ylabel

tw['population'].plot(ax=ax, rot=45)#rot:旋轉作標刻度,畫藍線
tw['area'].plot(ax=ax2, style ='r-.')#軸去對上ax2畫紅線
print(tw['population']) #用以上兩圖去畫表
print()
print(tw['area'])

ax.legend(loc=1)#loc指定圖例的位置 右上
ax2.legend(loc=2) #左上
plt.show()


-------------------------------------
#畫圓餅圖:
import pandas as pd
import matplotlib.pyplot as plt

fruits = ['apple','bananas','grapes','pears','oranges']
s = pd.Series([2300,5000,1200,2500,2900], index=fruits, name='Fruits Shop')
print(s)
explode=[0.4,0,0,0.2,0]
s.plot.pie(explode=explode, autopct='%1.2f%%')
plt.show()


------------------------------------
#pandas.series(data , index , dtype ,name)
#資料合併.concat 預設垂直並排
import pandas as pd
years = range(2020,2023)#index
beijing = pd.Series([20,21,19],index = years)#設定Series物件
print(beijing)
hongkong = pd.Series([25,26,27],index = years)#用index去對應data的值
singapore = pd.Series([30,29,31],index = years)#ex: 2020對20 2021對21 2022對19
citydf = pd.concat([beijing, hongkong, singapore])
print(type(citydf)) #concat():資料合併    concat([要合併的資料])
print(citydf)


----------------------------
#更改concat參數 concat([要合併的資料],axis = 1) 顯示索引對上的data
import pandas as pd
years = range(2020,2023)
beijing = pd.Series([20,21,19],index = years)
hongkong = pd.Series([25,26,27],index = years)
singapore = pd.Series([30,29,31],index = years)
citydf = pd.concat([beijing, hongkong, singapore],axis=1)
print(type(citydf))#concat([要合併的資料],axis = 1) 顯示索引對上的data
print(citydf)      #一個欄column就是一個series資料，非直向排列

--------------------------
#更改concat參數 將columns改成城市名 .columns方法
import pandas as pd
years = range(2020,2023)
beijing = pd.Series([20,21,19],index = years)
hongkong = pd.Series([25,26,27],index = years)
singapore = pd.Series([30,29,31],index = years)
citydf = pd.concat([beijing, hongkong, singapore],axis=1)
cities = ['Beijing','Hongkong','Singapore'] #設定cities城市串列 columns
citydf.columns = cities #用方法 合併後資料.columns=欄位串列名稱 來修改欄為名稱
print(citydf)
-----------------------------
#更改series columns的方式 .name方法
import pandas as pd
years = range(2020,2023)
beijing = pd.Series([20,21,19],index = years)#建立series資料
hongkong = pd.Series([25,26,27],index = years)
singapore = pd.Series([30,29,31],index = years)
beijing.name ='Beijing' #用Series資料去.name ,在合併concat時不用在打
hongkong.name = 'Hongkong'
singapore.name = 'Singapore'
print(beijing)
print()
citydf = pd.concat([beijing, hongkong, singapore],axis=1)
print(citydf)

-----------------------------------
#以下方法 name = XX 等同上面的做法
#合併時自動寫入column

import pandas as pd
years = range(2020,2023)   #在series中增加name參數
beijing = pd.Series([20,21,19],index = years, name ='Beijing')#建立series資料
hongkong = pd.Series([25,26,27],index = years, name = 'Hongkong')
singapore = pd.Series([30,29,31],index = years, name = 'Singapore')

print(beijing)
print()
citydf = pd.concat([beijing, hongkong, singapore],axis=1)
print(citydf)











'''
    
time():時間序列:數據由時間順序列出，時間維一系列的時間戳記
    匯入時間模組: from datetime import datetime

    設定特定時間:datetime.datetime(年月日時分秒)
    時間區間:時間=datatime.timedelta(weeks,days,hours,minutes,seconds)
        
    .date_range(起始日期, 終止日期):日期範圍


'''

-----------------------------
#顯示目前時間
from datetime import datetime
tn=datetime.now()
print(type(tn))
print('現在時間',tn)
print('')

----------------------
#取出時間
from datetime import datetime
tn=datetime.now()
print(type(tn))
print('現在時間',tn)
print('年 : ',tn.year)
print('月 : ',tn.month)
print('日 : ',tn.day)
print('時 : ',tn.hour)
print('分 : ',tn.minute)
print('秒 : ',tn.second)

--------------------------
#利用timedelta作表單
import pandas as pd
from datetime import datetime, timedelta

ndays = 5 #天數
start = datetime(2019,3,11) #從哪天開始
dates = [start + timedelta(days=x) for x in range(0,ndays)]
           #5個日期, 0~4 ,0就是3/11
print(dates)
data = [34,44,65,53,39]
ts = pd.Series(data, index = dates)
print(type(ts))
print(ts)

--------------------------
#兩組series物件互相作運算
import pandas as pd
from datetime import datetime, timedelta

ndays = 5 
start = datetime(2019,3,11)
dates = [start + timedelta(days=x) for x in range(0,ndays)]
     
data1 = [34,44,65,53,39]
ts1 = pd.Series(data1, index = dates)

data2 = [34,44,65,53,39]
ts2 = pd.Series(data2, index = dates)

addts = ts1+ts2
print('ts1+ts2')
print(addts)

meants = (ts1+ts2)/2
print('(ts1+ts2)/2')
print(meants)

----------------------------------
#date_range(起始日期, 終止日期)建立串列
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('3/11/2019','3/15/2019')#.date_range(起始日期, 終止日期)
data = [34,44,65,53,39]
ts = pd.Series(data, index=dates)
print(ts)
ts.plot(title= 'Data in Time Series')
plt.xlabel('Date')
plt.ylabel('Data')
plt.show()
