# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 22:09:06 2020

@author: 莫再提
"""
from tkinter import *
import pymysql
import time
from datetime import *
import pandas as pd
import matplotlib.pyplot as plt

ww =Toplevel()
ww.geometry("600x400")
ww.title("銷售查詢系統")



lab1=Label(ww,text='請輸入查詢範圍')
lab2=Label(ww,text='全部查詢')
bt1=Button(ww,text="查詢")#全查
lab1.grid(row=0,column=0,sticky=W,columnspan=6)
lab2.grid(row=1,column=0,sticky=W)
bt1.grid(row=1,column=1)

lab3=Label(ww,text='分區查詢')
lab3.grid(row=2,column=0,sticky=W)

lab3=Label(ww,text='查詢ID')
lab4=Label(ww,text='查詢筆數')
firstNum=IntVar()
secondNum=IntVar()
#-------------------------------------依照性名查詢
lab15=Label(ww,text='查詢產品名')
lab15.grid(row=2,column=2,sticky=W)
et7 = Entry(ww,width=5)
et7.grid(row=2,column=3,sticky=W)
bt7=Button(ww,text="查詢")#姓名查
bt7.grid(row=2,column=4) 
#-------------------------------------  

et1 = Entry(ww,width=5,textvariable=firstNum)
et2 = Entry(ww,width=5,textvariable=secondNum)
lab3.grid(row=3,column=0,sticky=W)
et1.grid(row=3,column=1,sticky=W)
lab4.grid(row=3,column=2,sticky=W)
et2.grid(row=3,column=3,sticky=W)


bt2=Button(ww,text="查詢")#分區查
bt2.grid(row=3,column=4)

lab6=Label(ww,text='') #查詢結果
lab6.grid(row=4,column=1,sticky=W,columnspan=2)

text=Text(ww,height=20,width=35)  #文字區塊
text.grid(row=5,column=0,columnspan=4,rowspan=19)
sc1 =Scrollbar(ww)
sc1.grid(row=5,column=4,sticky=(N,S),rowspan=19)
#sc1.config(command=text.yview) #將轉軸設定為文字的Y軸
#st=df.astype('str')
ww.mainloop()