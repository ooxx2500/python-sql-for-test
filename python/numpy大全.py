# -*- coding: utf-8 -*-
"""
x= np.arange(0, 3 * np.pi ,0.1)
#np.arrange= np的範圍 0開始到3*pi 間格為0.1
"""
import numpy as np



arr = np.array([[1,2,3],[4,5,6]])#建立一個np陣列(2*3的矩陣)
print(arr)

arr2=np.array([1,2,3,4,5,6])
arr3=arr2.reshape(2,3) #將一維重新排列成2*3 二維矩陣
print(arr3)

ran_arr=np.random.random((4,2))#建立4*2隨機矩陣 0~1
print(ran_arr)
---------------------------------

import numpy as np
a = np.floor(5*np.random.random((2,12)))
print(a)

import numpy as np
a = np.floor(10*np.random.random((2,12)))
print(a)


x= np.arange(0, 3 * np.pi ,0.1)
#np.arrange= np的範圍 0開始到3*pi 間格為0.1
y = np.sin(x)
print(x)
print(y)

x = np.arange(1,11,0.5)
y = 2*x+5
print(x)
print(y)


x= np.linspace(-1,1,10) #numpy.linspace(起始,中止,要幾個) 取一數列
y1=2*x+1
y2=x**2
print(x)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

np.random.seed(20131) #設定亂數種子

x =np.arange(0.0,50.0,2.0)  #np.random.rand(裡面要整數)  *x.shape用來轉化數值為int
y =np.random.rand(*x.shape) #x產生的直若為浮點(非整數)
n=x.shape
z=np.random.rand(25)
print(x)
print(y)
print(n)
print(z)
--------------------------------------------
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3,4))*0, columns=['x','y','z','s'])#用NP創造3row*4column
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['x','y','z','s'])#用NP創造3row*4column
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['x','y','z','s'])#用NP創造3row*4column
                
print(df1)
print(df2)
print(df3)

a =np.ones((3,4))*0
print(a)
b =np.ones((3,4))
print(b)



----------------------------------
#用numpy.random.randint建立隨機串列
import pandas as pd
import numpy as np

name = ['Frank','Peter','John','mona']
score = ['first','second','final']
#用np.random建立3(row)*4(column)陣列，每一格的數據在60-99之間
df = pd.DataFrame(np.random.randint(60,100,size=(3,4)), columns=name, 
                  index=score)
print(df)

a = np.random.randint(60,100,size=5) #隨機印出一維5個數字
print(a)                     
b = np.random.randint(60,100,size=(3,4))#隨機產生3*4的整數矩陣
print(b)  

img = np.ones((n,n,3),np.uint8)*255
print(img)



















