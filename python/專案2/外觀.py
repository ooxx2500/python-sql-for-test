# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 13:03:17 2020

@author: 莫再提
"""
def cleanACPW():
    et1.delete(0,END)
    et2.delete(0,END)
    
    

def login():
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    test = db.cursor() 
    df=pd.read_sql("""SELECT * FROM users""",con=db)
    db.close()
    account=et1.get()
    if account in df['accont'].values:
        password=et2.get()
        mask=df['accont'].values==account
        if df[mask]['password'].values ==password:
            lb5["text"]="密碼正確成功登入"
            time.sleep(3)
            window.destroy()
        else:
            lb5["text"]="密碼錯誤"
    
    else:
        lb5["text"]="此帳號不存在，請重新輸入。"













from tkinter import *
import pymysql
import time
import pandas as pd


window =Tk()
window.title("庫存系統")
window.geometry("600x400")

x =StringVar()


lb4 = Label(window,text="請輸入帳號密碼登入系統").grid(row=0,column=0,columnspan=2)
lb1 = Label(window,width=10, text="帳號").grid(row=1,column=0)
lb2 = Label(window, width=10,text="密碼").grid(row=2,column=0)
et1 = Entry(window,width=10)
et1.grid(row=1,column=1)
et2 = Entry(window,width=10,show="*")
et2.grid(row=2,column=1)
bt1 = Button(window,text="重新輸入",command=cleanACPW).grid(row=3,column=0)
bt2 = Button(window,text="登入",command=login).grid(row=3,column=1)
lb5 = Label(window)
lb5.grid(row=4,column=1)
lb3 = Label(window, textvariable = x).grid(row=5,column=0)



window.mainloop()