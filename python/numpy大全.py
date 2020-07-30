# -*- coding: utf-8 -*-
"""
x= np.arange(0, 3 * np.pi ,0.1)
#np.arrange= np的範圍 0開始到3*pi 間格為0.1

np的屬性功能 (執行屬性後不會改變原始ndarray資料)
    ndim   顯示幾維
    shape  用tuple顯示ndarry形狀
    T      回傳轉置後的陣列Ex:shape(2,3)會轉為(3,2)
    data   顯示記憶體位置
    dtype  顯示ndarry的資料型別
    flat   將nadarry物件轉為1維陣列
    imag   顯示ndarry的虛數部分
    real   顯示ndarry的實數部分
    size   顯示ndarry的總元素量
    itemsize  以byte為單位位元顯示每個元素記憶體使用量
    nbytes    以byte為單位位元顯示全部元素記憶體使用量
    strides   步長用tuple顯示各維一棟一個元素需要的byte數
    
np的方法
    np.sum()     np加總
    np.prod()    計算元素的乘積
    np.mean()    計算元素的平均
    np.median()  計算元素的中位數元素
    np.min()     找到最小
    np.max()     找到最大
    np.argmin()  查找最小索引直
    np.argmax()  查找最大索引直
    np.any()     評估是否有任何元素為真
    np.std()     計算標準差
    np.var()     計算(均)方差，np.std()的平方等於np.var()
    np.all()     評估所有元素是否都為真
    np.percentile()  計算元素雞魚排名的統計數據(第%分位的數值)

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


'''
Numpy 多維陣列的高速運算，用已處理機器學習 深度學習，資料處理

import numpy as np

ndarray進行加乘時會對每個元素進行運算

np.arrange(起始，終止-1，間格)

np.linspace(起始，終止，均分給幾個)

np.T  陣列轉置(翻轉矩陣)

np.ndim 查維度
'''

import numpy as np
a=np.array([1,2,3]) #用array建立np陣列
a  #array([1, 2, 3])
type(a)
print(a) #[1 2 3]
a*3 #array([3, 6, 9])
a+2 #array([3, 4, 5])
b=[1,2,3]
b*3 #[1, 2, 3, 1, 2, 3, 1, 2, 3]
#b+2 #錯誤
c=np.array([2,2,0])
a+c #array([3, 4, 3])
#a/c #0會錯誤
np.arange(10) #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.linspace(0,10,15) #0-10之間(包含10)均分15個數值
d=np.array([[1,2,3],[4,5,6]])
d #array([[1, 2, 3],
      # [4, 5, 6]])
d.shpae
-------------------------------------------------------
import time
import numpy as np
def calculate_time():
    a = np.random.randn(100000)
    b = list(a)
    start_time = time.time()
    for _ in range(1000):
        sum_1 = np.sum(a)
    print ('使用 Numpy\t  %f 秒' % (time.time() -start_time))

    start_time = time.time()
    for _ in range(1000):
        sum_2 = sum(b)
    print ('不使用 Numpy\t %f 秒' % (time.time() -start_time))

calculate_time()
---------------------------------------------------
b=np.array([[1,2,3],[4,5,6]])
b
b.T #陣列轉置
'''
[[x11,x12,x13],[x21,x22,x23]] #二維陣列(2,3) 

[[x11,x12,x13],  #2軸陣列  第0軸(axis=0)兩個元素構成的陣列
[x21,x22,x23]]            第1軸(axis=1)兩個子陣列內各有三個元素
第0軸為2維                 維度:陣列每一軸所函的元素各數，稱為每一軸的維度
第1軸維3維   #軸數字越少就是陣列月外層



'''
import numpy as np
a=np.array([[0,1],[2,3],[4,5]])
a
a.ndim
b=np.array([[[0,1],[2,3],[4,5]],[[0,1],[2,3],[4,5]]])
b.shape
b
b.sum(axis=0) #對第0軸相加
b.sum(axis=1)
b.sum(axis=2)


'''
np.random.rand(d0,d1,d2.......dn)
建立d0,d1.....維度的亂數浮點

np.random.rand()
建立0~1(不含1)之間的亂數浮點

np.random.randint(low, high, size)
與np.random.rand()同，差別在產生整數

np.zeros(n):產生元素皆為0的陣列
np.zeros(n,dtype=int):產生元素皆為0的陣列
np.ones(n) 產生元素皆為1的陣列
np.ones(n,dtype=int)
'''
import numpy as np

np.random.rand()   #產生0-1(不函)的隨機浮點數
np.random.randint(10) #產生0-10(不函)的隨機整數
np.random.rand(2,3) #產生2row 3column的隨機浮點數
np.random.randint(10, size=(2,3))#產生0-10(不函)的隨機整數 2row 3column的隨機浮點數

np.zeros(10) #一維
np.zeros(10,dtype=int)
np.zeros((4,3)) #要兩個誇號等同執行shape
np.ones(10)

'''
回歸分析

統計中分析數據的方法

目的:解析單一或多個變數對結果的影響程度(通常為預測)

執行方式:
    1.假設求出結果的方程式 直線:f(x)=xw1+w0
    若所有資料點無法聚合到一條直線，則採用多項是回歸
    
    2.求多項是回歸:將方程式中之x加上次方項(如x之2次方，三次方)
    則方程式為(w0,w1,w2為係數)
    f(x)=w2x**2+w1x+w0
    以一次方相開始測試
    f(x)=w1x+w0
    使用 np.polyfit()函式
    格式:polyfit(x,y,次方數) 
        傳回係數w1 w0(以一次方項為例)
    poly1d(多項式係數)
        傳回poly1d物件代表係數組成的多項式
        
       
       
       
'''
#建立20個(x,y)組合之座標點
import numpy as np
x = np.random.rand(20)*8-4
y=np.sin(x)+np.random.rand(20)*0.2
oma=np.polyfit(x,y,1)
oma
f=np.poly1d(oma)
import matplotlib.pyplot as plt
t=np.poly1d(oma)
plt.title('polyfitfuntion')
plt.grid()
plt.scatter(x,y,marker='x',c='red')
xx=np.linspace(-4,4,100)
plt.plot(xx,f(xx),color='green')
plt.show()



--------------------------------
#以五次方完成回歸分析
import numpy as np
x = np.random.rand(20)*8-4
y=np.sin(x)+np.random.rand(20)*0.2
oma=np.polyfit(x,y,5)
oma
f=np.poly1d(oma)
import matplotlib.pyplot as plt
t=np.poly1d(oma)
plt.title('polyfitfuntion')
plt.grid()
plt.scatter(x,y,marker='x',c='red')
xx=np.linspace(-4,4,100)
plt.plot(xx,f(xx),color='green')
plt.show()

'''
資料模型:
    回歸分析>回歸模型
    自變量(數)>模型>因變量(數)
    透過變量(數)資料(歷史資料)
    運用適當的演算法

資料分析:
    資料產出/取得
    工具(套裝程式<python>...)
    資料預處理:清洗 丟棄 補全 轉換 不處理    
    樣本分析:抽樣數，樣本數，分析方法(演算法)

分析模型:
    依不同功能產業別不同的建置
    會員類型:
        會員類型模型:
        會員活絡度模型:
        會原價值模型:
    
    商品模型:
        商品價格敏感度模型:
        新商品市場定住模型:
        銷售模型:
        商品關聯性模型:

'''







