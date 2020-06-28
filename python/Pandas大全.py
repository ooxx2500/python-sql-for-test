# -*- coding: utf-8 -*-
"""

"""
#改變DataFrame的型態

df["marry_pair"] = df["marry_pair"].astype(str).astype(int)

#將DF物件轉檔成文字及INT
df["marry_pair"] = df["marry_pair"].astype(int)
df["marry_pair"] = df["marry_pair"].astype(str)


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



