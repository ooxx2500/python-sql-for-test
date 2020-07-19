# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:39:04 2020

@author: 莫再提
"""

def search_data():
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    test = db.cursor() 
    df=pd.read_sql("""SELECT * FROM momom""",con=db)  
    start=eval(et1.get())
    how=eval(et2.get())   
    lab6['text']='區段查詢結果'
    mask=df['id_'].values>=start
    text.delete('1.0', END)
    text.insert(END,df[mask].head(how))
    db.close()

def search_all_data():
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    test = db.cursor() 
    df=pd.read_sql("""SELECT * FROM momom""",con=db)     
    lab6['text']='全部查詢結果'
    st=df.astype('str')  #df轉STR
    text.delete('1.0', END)
    text.insert(END,st)
    db.close()







from tkinter import *
import pymysql
import time
import pandas as pd

db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
test = db.cursor() 
df=pd.read_sql("""SELECT * FROM momom""",con=db)
db.close()





window =Tk()
window.title("庫存系統")
window.geometry("600x400")


lab1=Label(window,text='請輸入查詢範圍')
lab2=Label(window,text='全部查詢')
bt1=Button(window,text="查詢",command=search_all_data)#全查
lab1.grid(row=0,column=0,sticky=W,columnspan=6)
lab2.grid(row=1,column=0,sticky=W)
bt1.grid(row=1,column=1)

lab3=Label(window,text='分區查詢')
lab3.grid(row=2,column=0,sticky=W)

lab3=Label(window,text='查詢ID')
lab4=Label(window,text='查詢筆數')
firstNum=IntVar()
secondNum=IntVar()

    

et1 = Entry(window,width=10,textvariable=firstNum)
et2 = Entry(window,width=10,textvariable=secondNum)
lab3.grid(row=3,column=0,sticky=W)
et1.grid(row=3,column=1,sticky=W)
lab4.grid(row=3,column=2,sticky=W)
et2.grid(row=3,column=3,sticky=W)


bt1=Button(window,text="查詢",command=search_data)#分區查
bt1.grid(row=3,column=4)

lab6=Label(window,text='') #查詢結果
lab6.grid(row=4,column=1,sticky=W,columnspan=2)

text=Text(window,height=20,width=40)  #文字區塊
text.grid(row=5,column=0,columnspan=5,rowspan=20)
sc1 =Scrollbar(window)
sc1.grid(row=5,column=5,sticky=(N,S),rowspan=20)
sc1.config(command=text.yview) #將轉軸設定為文字的Y軸
st=df.astype('str')

text.insert(END,st)
lab5=Label(window,text='6969') #查詢結果
lab5.grid(row=8,column=6,sticky=W)



window.mainloop()