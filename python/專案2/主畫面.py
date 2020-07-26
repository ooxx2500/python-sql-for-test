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
   
    quantity=df[check]['quantity'].values[0]
    print("數量還剩:",quantity) 
    storage=eval(et6.get())

    if storage<=0:
        text3.delete('1.0', END)
        s1='存入錯誤，不得為0或負數。'
        text3.insert(END,s1)

        db.close()
    else:
        last_number=quantity+storage #存後數量       
        SQL_update="UPDATE `momom` SET `quantity` = '{0}' WHERE `momom`.`id_` = {1}; "
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


def search_sellall_data(): #查詢所有銷售
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    df=pd.read_sql("""SELECT date as "日期", price*quantity as "總銷售",name as "產品" FROM sell_list""",con=db)
    
    lab24['text']='全部查詢結果'
    st=df.astype('str')  #df轉STR
    text4.delete('1.0', END)
    text4.insert(END,st)
    db.close()


def search_selldate_data(): #查詢日期銷售
   
    
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    df=pd.read_sql("""SELECT date as "日期", price*quantity as "總銷售",name as "產品" FROM sell_list""",con=db)
    search_name=et11.get() #2000-01-11
    search_name=search_name.replace('-','')
    sdate = df['日期'].astype(str).apply(lambda x:x.replace('-',''))
    db.close()
    
    if search_name in sdate.values:
        mask=sdate.iloc[:]==search_name
        
        text4.delete('1.0', END)
        text4.insert(END,df[mask])
        
        
        print(df[mask])
    else:  
        text4.delete('1.0', END)
        text4.insert(END,"查無關鍵日期")   
    
   

def search_sellname_data(): #查詢銷售名稱
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    df=pd.read_sql("""SELECT date as "日期", price*quantity as "總銷售",name as "產品" FROM sell_list""",con=db)
    search_name=et10.get()
    print(search_name)
    
    if search_name in df['產品'].values:
        mask=df.iloc[:,2]==search_name #索引2是產品名
        lab24['text']='查詢成功'
        text4.delete('1.0', END)
        text4.insert(END,df[mask])
    else:  
        lab24['text']='無此關鍵字'

def sellsomething_ID(): #銷售區查ID
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    df=pd.read_sql("""SELECT * FROM momom""",con=db)
    test = db.cursor()
    db.close()
   
    try:
        in_id=eval(et3.get())
        print(in_id)
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
    quantity=df[check]['quantity'].values[0]
    print("數量還剩:",quantity) 
    sell=eval(et4.get())
    print(sell)
    
    df=pd.read_sql("""SELECT * FROM momom""",con=db)
    test = db.cursor()
    quantity=df[check]['quantity'].values[0]
    if sell >quantity:
        lab9['text']='交易錯誤，庫存不足。'
        db.close()
        print(656565456)
    else:
        df=pd.read_sql("""SELECT * FROM momom""",con=db)
        
        remain_number=quantity-sell #剩餘數量       
        SQL_update="UPDATE `momom` SET `quantity` = '{0}' WHERE `momom`.`id_` = {1} and `quantity`>={2}; "
        SQL_update=SQL_update.format(remain_number, in_id, sell )
        test.execute(SQL_update)#資料庫進行扣除
        db.commit()
        SQL_price="SELECT * FROM momom where id_=%d"%in_id
        print(SQL_price)
        
        test.execute(SQL_price)
        price=0
        goods=''
        for i in test:
            price=i[0]        
            goods=i[3]
            print(i)
        print(price,sell,goods)
        totalsell = sell*price
        print(totalsell)
        t=date.today()
        print(t)
        SQL_set="INSERT INTO `sell_list` (date, `price`, `quantity`, `total`, `id_`, `name`) VALUES('{0}','{1}','{2}',{3},NULL,'{4}');"
        SQL_set=SQL_set.format(t, price, sell,totalsell, goods)
        print(SQL_set)
        test.execute(SQL_set)
        db.commit()
        print('銷售表新增交易完成')
        df=pd.read_sql("""SELECT * FROM momom""",con=db)
        lab9['text']="交易成功"      
        text2.delete('1.0', END)
        s1="交易成功，賣出{0}，剩餘{1}\n--------------------------\n".format(sell, (quantity-sell))
        text2.insert(END,s1)
        text2.insert(END,df[check])
        print("交易成功")
        db.close()




def serch_name(): #查詢姓名
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    test = db.cursor() 
    df=pd.read_sql("""SELECT * FROM momom""",con=db)
    db.close()  
    search_name=et7.get()

    if search_name in df['name'].values:
        mask=df.iloc[:,3]==search_name
        lab6['text']='查詢成功'
        text.delete('1.0', END)
        text.insert(END,df[mask])
    else:  
        lab6['text']='無此關鍵字'
    
def serch_name2(): #查詢姓名2
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    test = db.cursor() 
    df=pd.read_sql("""SELECT * FROM momom""",con=db)
    db.close()  
    search_name=et7.get()

    if search_name in df['name'].values:
        mask=df.iloc[:,3]==search_name
        lab6['text']='查詢成功'
        text.delete('1.0', END)
        text.insert(END,df[mask])
    else:  
        lab6['text']='無此關鍵字'

#------------------------------------------------------------------------

def search_all_sell():#查詢年月日銷售裱
    print(56456)



#SELECT * FROM `sell_list` WHERE date BETWEEN '2020-07-01' and '2020-07-22' 

def show_sell_figue():
    search_start=et12.get()
    search_end=et13.get()
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    
    sql="""SELECT date as '日期', SUM(price*quantity) as '銷售額' 
    FROM sell_list Where date between '{0}' and '{1}'
    GROUP BY date""".format(search_start,search_end)
 
    df=pd.read_sql(sql,con=db)
    print(df)
    
    df.plot(x='日期',y='銷售額')
    plt.xticks(rotation=45 )
    plt.title('銷售報表')#圖表的標題
    
    plt.savefig('figure_sell.png')
    
    window =Toplevel()
    window.title("銷售圖表")
    window.geometry("550x430")    
    fig=PhotoImage(file="figure_sell.png")  
    Label(window,image=fig).pack()
    
    db.close()
    window.mainloop()  
  
def showfigue():
    db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
    test = db.cursor() 
    df=pd.read_sql("""SELECT name , SUM(quantity) as "數量" FROM momom GROUP BY name""",con=db)


    df.plot.bar(x='name',y='數量')
    plt.title('庫存報表')#圖表的標題
    plt.xlabel('產品名稱')#x座標標題
    plt.ylabel('庫存數量')#y座標標題
    plt.xticks(rotation=0 )
    plt.savefig('figure.png')
    
    w =Toplevel()
    w.title("庫存圖表")
    w.geometry("550x430")    
    fig=PhotoImage(file="figure.png")  
    Label(w,image=fig).pack()
    db.close()
    w.mainloop()    
    






#------------------------------------------------------------------------

from tkinter import *
import pymysql
import time
from datetime import *
import pandas as pd
import matplotlib.pyplot as plt
font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '12'}#設定字形樣式大小
plt.rc('font', **font) #設定PY繪圖系統的字型項目  

db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')
test = db.cursor() 
df=pd.read_sql("""SELECT * FROM momom""",con=db)
db.close()




window =Tk()
window.title("庫存系統")
window.geometry("850x400")


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
#-------------------------------------依照性名查詢
lab15=Label(window,text='查詢產品名')
lab15.grid(row=2,column=2,sticky=W)
et7 = Entry(window,width=5)
et7.grid(row=2,column=3,sticky=W)
bt7=Button(window,text="查詢",command=serch_name)#姓名查
bt7.grid(row=2,column=4) 
#-------------------------------------  

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

text2=Text(window,height=4,width=35)  #文字區塊2
text2.grid(row=3,column=6,columnspan=4,rowspan=4,padx=10)

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

text3=Text(window,height=4,width=35)  #文字區塊2
text3.grid(row=10,column=6,columnspan=4,rowspan=8)

lab13=Label(window,text='',padx=10)
lab13.grid(row=9,column=6,columnspan=2)

lab14=Label(window,text='',padx=10)
lab14.grid(row=9,column=6,columnspan=2)
#-------------------------------------------------------------------------

lab15=Label(window,text='銷售區間',padx=10)
lab15.grid(row=19,column=6)

lab16=Label(window,text='起始日期',padx=5)
lab16.grid(row=19,column=8)
lab17=Label(window,text='結束日期',padx=5)
lab17.grid(row=20,column=8)


et12 = Entry(window,width=9)    #起始日期
et12.grid(row=19,column=7,sticky=W)

et13 = Entry(window,width=9)    #結束日期
et13.grid(row=20,column=7,sticky=W)



bt7=Button(window,text="庫存圖表",command=showfigue)#存入按鈕
bt7.grid(row=18,column=9,sticky=W)

bt7=Button(window,text="銷售圖表",command=show_sell_figue)#存入按鈕
bt7.grid(row=19,column=9,sticky=W)

#-------------------------------------------最右邊銷售表 col=10




lab18=Label(window,text='請輸入銷售表查詢範圍')
lab19=Label(window,text='全部查詢')
bt8=Button(window,text="查詢",command=search_sellall_data)#全查
lab18.grid(row=0,column=10,sticky=W,columnspan=6)
lab19.grid(row=1,column=10,sticky=W)
bt8.grid(row=1,column=11)

lab20=Label(window,text='分區查詢')
lab20.grid(row=2,column=10,sticky=W)

lab21=Label(window,text='查詢日期')


#-------------------------------------依照性名查詢
lab23=Label(window,text='查詢產品名')
lab23.grid(row=2,column=12,sticky=W)
et10 = Entry(window,width=8)
et10.grid(row=2,column=13,sticky=W)
bt10=Button(window,text="查詢",command=search_sellname_data)#姓名查
bt10.grid(row=2,column=14) 
#-------------------------------------  

et11 = Entry(window,width=10,textvariable=StringVar()) #輸入日期

lab21.grid(row=3,column=10,sticky=W)
et11.grid(row=3,column=11,sticky=W)




bt11=Button(window,text="查詢",command=search_selldate_data)#分區查
bt11.grid(row=3,column=12)

lab24=Label(window,text='') #查詢結果
lab24.grid(row=4,column=11,sticky=W,columnspan=2)

text4=Text(window,height=20,width=35)  #文字區塊4
text4.grid(row=5,column=10,columnspan=5,rowspan=19)
sc12 =Scrollbar(window)
sc12.grid(row=5,column=15,sticky=(N,S),rowspan=19)
sc12.config(command=text2.yview) #將轉軸設定為文字的Y軸





window.mainloop()