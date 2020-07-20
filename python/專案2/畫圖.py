# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:39:04 2020

@author: 莫再提
"""

from tkinter import *
import pymysql
import time
import pandas as pd
import matplotlib.pyplot as plt

'''
db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
test = db.cursor() 
df=pd.read_sql("""SELECT * FROM momom""",con=db)
db.close()
x=df['name']
y=df['qualianty']
plt.bar(x,y,label='a',width=0.3) #在對齊為邊緣下,width正值靠右,負值往左
plt.savefig('figure.png')
plt.show()
window =Tk()
window.title("庫存系統")
window.geometry("440x280")
fig=PhotoImage(file="figure.png")
Label(window,image=fig).pack()
window.mainloop()
'''


def showfigue():
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    test = db.cursor() 
    df=pd.read_sql("""SELECT * FROM momom""",con=db)
    db.close()
    x=df['name']
    y=df['qualianty']
    plt.title('庫存報表')#圖表的標題
    plt.xlabel('產品名稱')#x座標標題
    plt.ylabel('庫存數量')#y座標標題
    plt.bar(x,y,label='a',width=0.3) #在對齊為邊緣下,width正值靠右,負值往左
    plt.savefig('figure.png')


    window =Tk()
    window.title("庫存系統")
    window.geometry("440x280")
    
    fig=PhotoImage(file="figure.png")
    
    Label(window,image=fig).pack()
    window.mainloop()  
    
    
    
    
font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '12'}#設定字形樣式大小
plt.rc('font', **font) #設定PY繪圖系統的字型項目  
showfigue()    
    
    
    
    
    