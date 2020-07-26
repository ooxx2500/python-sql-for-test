# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 11:58:33 2020

@author: 莫再提
"""



import requests
from bs4 import BeautifulSoup
import re

def check_lotto_now():
    url=r"https://www.taiwanlottery.com.tw/result_all.htm"
    list_req=requests.get(url)
    soup=BeautifulSoup(list_req.content,"lxml")
    
    divs=soup.find_all("div",{"id":"right_full"})
       
    tables=soup.find_all("table","tableWin")
    
    count=0
    retext=''
    for table in tables:
        tds=table.find_all("td")
        tdn=1
        for td in tds:
            if tdn==2:
                retext+=td.text.strip()+"\n"
    
            elif tdn==4:
                ted=td.text.strip().replace("\n",'').replace(" ",'').replace('第','').replace('期','').strip()
    
                retext+="期別:"+ted+"\n"  
            elif tdn==6:
               
                retext+=td.text.strip().replace("\n",'').replace(" ",'')+"\n"
            elif tdn==10:
                ted=td.text.strip().replace(" ",'')[:30]
                
                key=ted
                p1=r"\d{2}"    
                pattern=re.compile(p1)
                asd=pattern.findall(key)
    
                if len(asd)<=5:
                    for ii in asd:
                        retext+=ii+" "
                else:
                    for ii in range(6):
                        retext+=asd[ii]+" "
                    retext+="\n"
                    retext+="特別號:"+asd[6]+"\n"+"\n"                
            tdn+=1
        count+=1
        if count==3:
            break
    return retext


print(check_lotto_now())

