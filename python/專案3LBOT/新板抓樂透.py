# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:39:34 2020

@author: ASUS
"""




import requests
from bs4 import BeautifulSoup
def check_lottor(name):
    if name == '威力彩':
        url="https://www.taiwanlottery.com.tw/" #威力彩
        list_req=requests.get(url)
        soup=BeautifulSoup(list_req.content,"lxml")
        divs=soup.find('div','contents_box02').find_all('div')
        text='*****  威力彩  *****'+'\n'
        c=0      
        lst=[x for x in range(10,16)]
        for div in divs:
            c+=1
            if c==2:
                text+=div.text+'\n'+"開獎號碼:"
            elif c in lst:
                text+=div.text+" "
            elif c==16:
                text+='\n'+'特別號:'+div.text       
        return text
    elif name=='樂透' or name=='大樂透':
        url="https://www.taiwanlottery.com.tw/" #威力彩
        list_req=requests.get(url)
        soup=BeautifulSoup(list_req.content,"lxml")
        divs=soup.find(id='rightdown').find_all('div',"contents_box02")
        c=1
        div2=''
        
        text='*****  大樂透  *****'+'\n'
        c=1
        
        lst=[x for x in range(15,21)]
        for div in divs:
        
            if c==3:
                div2=div
            c+=1
        divs=div2.find_all("div")
        for div in divs:
            c+=1
            if c==2:
                text+=div.text+'\n'+"開獎號碼:"
            elif c in lst:
                text+=div.text+" "
            elif c==21:
                      text+='\n'+'特別號:'+div.text  
        
        return text
    
    
    
print(check_lottor('威力彩'))   
print(check_lottor('樂透'))  
    
    
    
    
    
    
    
    
    
    