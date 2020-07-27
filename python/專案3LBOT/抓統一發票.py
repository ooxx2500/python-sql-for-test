import requests
from bs4 import BeautifulSoup
import re


url=r"https://www.etax.nat.gov.tw/etw-main/web/ETW183W1/"
list_req=requests.get(url)
soup=BeautifulSoup(list_req.content,"lxml")

tables=soup.find_all("table",{"id":"fbonly"})
for table in tables:
    tds=table.find_all("td")
c=0
html=''
text=''
for td in tds:  #1 :欄位數    2:幾月中獎
    c+=1
    if c==2:
        a=td.find('a')
        html=a.get("href")
        text=td.text
        break
    
new_url="https://www.etax.nat.gov.tw"+html

retext=''

list_req=requests.get(new_url)
soup=BeautifulSoup(list_req.content,"lxml")

trs=soup.find("table").find_all('tr')
c=0
for tr in trs:
    retext+=(tr.text.strip().replace('\n',''))+'\n'
    c+=1
    if c ==13:
        break

print(retext)
















