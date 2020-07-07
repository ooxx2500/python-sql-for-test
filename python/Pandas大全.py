# -*- coding: utf-8 -*-
"""

"""
------------------------------
#將pandas整欄做字串處裡.str

import pandas as pd

path=r"C:\Users\莫再提\Desktop\fsd.csv.csv"
df=pd.read_csv(path, header=0) #header=0 欄位從第幾行開始

df['外陸資買進股數(不含外資自營商)']=df['外陸資買進股數(不含外資自營商)'].str.replace(',','')


#用map+lambda將pandas整欄做字串處裡.str
import pandas as pd

path=r"C:\Users\莫再提\Desktop\fsd.csv.csv"
df=pd.read_csv(path, header=0) #header=0 欄位從第幾行開始
a=df.iloc[8:].index
df=df.drop(a)
df['外陸資買進股數(不含外資自營商)']=df['外陸資買進股數(不含外資自營商)'].map(lambda x:x.replace(',',''))

print(df)

------------------------------------------------------

#例子2  .str.upper()

import pandas as pd

lst=[['dsad','dsad','asdw'],['asda','zxczx','qweqw']]
df=pd.DataFrame(lst,columns=('A','B','C'))
df['A']=df['A'].str.upper()
df['C']=df['C'].str.title()
df['B']=df['B'].str.replace('x','ABCD')

print(df)


-----------------------------------
df=pd.util.testing.makeDataFrame().head(10)
print(df)




----------------------------------
#隨機建立pd
df=pd.util.testing.makeDataFrame().head(10)


#改變DataFrame的型態

df["marry_pair"] = df["marry_pair"].astype(str).astype(int)

#將DF物件轉檔成文字及INT
df["marry_pair"] = df["marry_pair"].astype(int)
df["marry_pair"] = df["marry_pair"].astype(str)
--------------------------------------
#新增欄位並修改name
#用numpy 建立隨機串列
import pandas as pd
import numpy as np

# create a random DataFrame with 7 rows and 2 columns
df = pd.DataFrame(np.random.randint(0,100,size = (3,4)), 
                  columns = ['A','B','C','D'])
df.insert(0,column='name',value='no')

print(df.info())
print(df)


names=['mona','judy','aria']
for i in range(3):
    df.iloc[i,0]=names[i]
    
print(df)


df['A'][0]=10
df['A'][1]=20
df['A'][2]=30

print(df)

df.iloc[0,2]=50
df.iloc[1,2]=60
df.iloc[2,2]=70
print(df)


---------------------------------------

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
df = pd.DataFrame(data)
print(df)
print(df['year'])

-------------------------------------
#用pd讀取csv檔後文件內容文字是OBJ類型 數字是INT 小數點是float
import pandas as pd
rf=pd.read_csv(r'C:\Users\莫再提\Desktop\pm2.5.csv')
print(rf['county'],rf['PM25'])
print(rf['PM25'].sum())

--------------------------------------

import pandas as pd
import numpy as np
list1=['mona',25,30,40,'judy',40,40,50,'aria',2,5,100]
data=np.reshape(list1,(3,4))
print(data)
print(type(data))
print()
df = pd.DataFrame(data)
print(df[1])#用了reshape() 所有數字型態皆為obj
print(df[1].sum())
print()
df[1] = df[1].astype(int) #將OBJ物件轉為INT就可以加總
print(df[1])
print(df[1].sum())

---------------------------------------

#找出pandas中的特定自並印出來
df1=rf2['site_id']
print(df1)
df1=rf2['site_id']=='新北市三重區'
print(rf2[df1])

#找出區間 用兩次mask 4000~5000

rr=(rf2['people']<5000)
rf2=rf2[rr]
rr=(rf2['people'][rr]>4000)
print(rf2[rr])

#如有形態問題可以用astype(str) (int)
--------------------------------------------
#pandas concat合併大法










----------------------------------------------