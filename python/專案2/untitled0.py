# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:39:04 2020

@author: 莫再提
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:39:04 2020

@author: 莫再提
"""
#補貨查詢
def add_storage_id():
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    df=pd.read_sql("""SELECT * FROM momom""",con=db)
    test = db.cursor()
    db.close()
  
    try:
        in_id=eval(et5.get())
        check=df['id_']==in_id
        st=df[check]
        text3.delete('1.0', END)
        text3.insert(END,st)
    except Exception as err:
        st="錯誤，請輸入數字"
        text3.delete('1.0', END)
        text3.insert(END,st)
        
        


#補貨增加數量
def add_storage():
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    df=pd.read_sql("""SELECT * FROM momom""",con=db)
    test = db.cursor()

    in_id=eval(et5.get())
    check=df['id_']==in_id
   
    quantity=df[check]['qualianty'].values[0]
    print("數量還剩:",quantity) 
    storage=eval(et6.get())

    if storage<=0:
        text3.delete('1.0', END)
        s1='存入錯誤，不得為0或負數。'
        text3.insert(END,s1)

        db.close()
    else:
        last_number=quantity+storage #存後數量       
        SQL_update="UPDATE `momom` SET `qualianty` = '{0}' WHERE `momom`.`id_` = {1}; "
        SQL_update=SQL_update.format(last_number, in_id )
        test.execute(SQL_update)#資料庫進行相加
        db.commit()
        df=pd.read_sql("""SELECT * FROM momom""",con=db)
        
        print("交易成功，存入%d，庫存%d"%(storage, (last_number)))
        print('=================================')
        print(df[check])
        print('=================================')
     

        lab14['text']="交易成功"      
        text3.delete('1.0', END)
        s1="交易成功，存入{0}，剩餘{1}\n--------------------------\n".format(storage, (last_number))
        text3.insert(END,s1)
        text3.insert(END,df[check])
        db.close()









def search_data(): #查詢區1
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    test = db.cursor() 
    df=pd.read_sql("""SELECT * FROM momom""",con=db)  
    start=eval(et1.get())
    how=eval(et2.get())
    if start==0 or how==0:
        lab6['text']='錯誤 欄位不得為0'
    else:    
        lab6['text']='區段查詢結果'
        mask=df['id_'].values>=start
        text.delete('1.0', END)
        text.insert(END,df[mask].head(how))
        db.close()

def search_all_data(): #查詢區2
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    test = db.cursor() 
    df=pd.read_sql("""SELECT * FROM momom""",con=db)     
    lab6['text']='全部查詢結果'
    st=df.astype('str')  #df轉STR
    text.delete('1.0', END)
    text.insert(END,st)
    db.close()

def sellsomething_ID(): #銷售區查ID
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    df=pd.read_sql("""SELECT * FROM momom""",con=db)
    test = db.cursor()
    db.close()
   
    try:
        in_id=eval(et3.get())
        check=df['id_']==in_id
        s1=df[check]
  
        text2.delete('1.0', END)
        text2.insert(END,s1)
       
    except Exception as err:
        text2.delete('1.0', END)
        s1="錯誤，請輸入數字"
        text2.insert(END,s1)
        


def sellsomething():    #銷售區
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    df=pd.read_sql("""SELECT * FROM momom""",con=db)
    test = db.cursor()
    in_id=eval(et3.get())
    check=df['id_']==in_id
    quantity=df[check]['qualianty'].values[0]
    print("數量還剩:",quantity) 
    sell=eval(et4.get())
    print(sell)

    df=pd.read_sql("""SELECT * FROM momom""",con=db)
    test = db.cursor()
    quantity=df[check]['qualianty'].values[0]
    if sell >quantity:
        lab9['text']='交易錯誤，庫存不足。'
        db.close()
    else:
        df=pd.read_sql("""SELECT * FROM momom""",con=db)
        
        remain_number=quantity-sell #剩餘數量       
        SQL_update="UPDATE `momom` SET `qualianty` = '{0}' WHERE `momom`.`id_` = {1} and `qualianty`>={2}; "
        SQL_update=SQL_update.format(remain_number, in_id, sell )
        test.execute(SQL_update)#資料庫進行扣除
        db.commit()
        df=pd.read_sql("""SELECT * FROM momom""",con=db)
        lab9['text']="交易成功"      
        text2.delete('1.0', END)
        s1="交易成功，賣出{0}，剩餘{1}\n--------------------------\n".format(sell, (quantity-sell))
        text2.insert(END,s1)
        text2.insert(END,df[check])
        db.close()

    
    
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
            time.sleep(2)
            window1.destroy()
            pass_it=False
            return pass_it
        else:
            lb5["text"]="密碼錯誤"
    
    else:
        lb5["text"]="此帳號不存在，請重新輸入。"


from tkinter import *
import pymysql
import time
import pandas as pd


window1 =Tk()
window1.title("庫存系統")
window1.geometry("300x200")

x =StringVar()


lb4 = Label(window1,text="請輸入帳號密碼登入系統").grid(row=0,column=0,columnspan=2)
lb1 = Label(window1,width=10, text="帳號").grid(row=1,column=0)
lb2 = Label(window1, width=10,text="密碼").grid(row=2,column=0)
et1 = Entry(window1,width=10)
et1.grid(row=1,column=1)
et2 = Entry(window1,width=10,show="*")
et2.grid(row=2,column=1)
bt1 = Button(window1,text="重新輸入",command=cleanACPW).grid(row=3,column=0)
bt2 = Button(window1,text="登入",command=login).grid(row=3,column=1)
lb5 = Label(window1)
lb5.grid(row=4,column=1,columnspan=3)
lb3 = Label(window1, textvariable = x).grid(row=5,column=0)


window1.mainloop()


pass_it=True
while pass_it:
    pass



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

    

et1 = Entry(window,width=5,textvariable=firstNum)
et2 = Entry(window,width=5,textvariable=secondNum)
lab3.grid(row=3,column=0,sticky=W)
et1.grid(row=3,column=1,sticky=W)
lab4.grid(row=3,column=2,sticky=W)
et2.grid(row=3,column=3,sticky=W)


bt2=Button(window,text="查詢",command=search_data)#分區查
bt2.grid(row=3,column=4)

lab6=Label(window,text='') #查詢結果
lab6.grid(row=4,column=1,sticky=W,columnspan=2)

text=Text(window,height=20,width=35)  #文字區塊
text.grid(row=5,column=0,columnspan=4,rowspan=19)
sc1 =Scrollbar(window)
sc1.grid(row=5,column=4,sticky=(N,S),rowspan=19)
sc1.config(command=text.yview) #將轉軸設定為文字的Y軸
st=df.astype('str')


sell_firstNum=IntVar()
sell_secondNum=IntVar()


text.insert(END,st)
lab5=Label(window,text='銷售表單') #銷售區
lab5.grid(row=0,column=6,columnspan=3)

lab7=Label(window,text='銷售ID',padx=20) #銷售區
lab7.grid(row=1,column=6,sticky=W)
et3 = Entry(window,width=4) #ID
et3.grid(row=1,column=7,sticky=W)
lab8=Label(window,text='銷售數量',padx=10)
lab8.grid(row=1,column=8,sticky=W)
et4 = Entry(window,width=4) #數量
et4.grid(row=1,column=9,sticky=W)
bt3=Button(window,text="確認ID",command=sellsomething_ID)#確認ID
bt3.grid(row=2,column=8,sticky=W)


bt4=Button(window,text="確認銷售",command=sellsomething)#分區查
bt4.grid(row=2,column=9,sticky=W)

text2=Text(window,height=4,width=30)  #文字區塊2
text2.grid(row=3,column=7,columnspan=4,rowspan=3)

lab9=Label(window,text='',padx=10)
lab9.grid(row=2,column=6,columnspan=2)


#--------------------------------捕貨區
lab10=Label(window,text='入庫表單') #庫存區
lab10.grid(row=7,column=6,columnspan=3)


lab11=Label(window,text='入庫ID',padx=20) #庫存區
lab11.grid(row=8,column=6,sticky=E)
et5 = Entry(window,width=4) #ID
et5.grid(row=8,column=7,sticky=W)
lab12=Label(window,text='存入數量',padx=10)
lab12.grid(row=8,column=8,sticky=W)
et6 = Entry(window,width=4) #數量
et6.grid(row=8,column=9,sticky=W)
bt5=Button(window,text="確認ID",command=add_storage_id)#確認ID
bt5.grid(row=9,column=8,sticky=W)


bt6=Button(window,text="確認存入",command=add_storage)#存入按鈕
bt6.grid(row=9,column=9,sticky=W)

text3=Text(window,height=6,width=30)  #文字區塊2
text3.grid(row=10,column=7,columnspan=4,rowspan=6)

lab13=Label(window,text='',padx=10)
lab13.grid(row=9,column=6,columnspan=2)

lab14=Label(window,text='',padx=10)
lab14.grid(row=9,column=6,columnspan=2)


window.mainloop()







