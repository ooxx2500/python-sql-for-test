# -*- coding: utf-8 -*-
"""
PY資料處裡精簡版

"""
#搜尋文章字詞
import jieba
import jieba.analyse

data_from = r"C:\Users\莫再提\Desktop\pytest\asd.txt"
#TXT路徑
f = open(data_from,'r',encoding = 'utf8')
    
article = f.read()  #extract_tags(文章,取幾個出現最多的)               
tags = jieba.analyse.extract_tags(article,10) #提取字詞分析權重最大值的傳回數
print('最重要字詞:',tags) #分析出文章最重要的十個字詞

"""
PDF專區
安裝pip install pdfkit
轉PDF檔  先去安裝wkhtmltopdf
"""

import pdfkit

config = pdfkit.configuration(wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
                 #使用前下載安裝wkhtmltopdf軟體 他安莊所在位置

pdfkit.from_url('https://tw.stock.yahoo.com/',\
            r'C:\Users\莫再提\Desktop\pytest\out1.pdf',configuration = config)
                   #將網頁轉乘PDF (網址 , 轉存的PDF位置 ,組態 )  
            
pdfkit.from_string('Hello world', \
                  r'C:\Users\莫再提\Desktop\pytest\ou55456t2.pdf',configuration = config) 
                   #將文字轉PDF (字串 , 轉存的PDF位置 ,組態 )
    
pdfkit.from_file(r'C:\Users\莫再提\Downloads\原價屋@酷！PC • 網站入口.html' ,\
                 r'C:\Users\莫再提\Desktop\pytest\out3.pdf',configuration = config )    
                  #獎檔案轉為PDF檔 (檔案, 轉存的PDF位置 ,組態 )            

pdfkit.from_file(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\test01.html' ,\
                 r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\out4.pdf',configuration = config )
                 #將html檔案做成PDF


-----------------------------------------------------
#pip install PyPDF2
from PyPDF2 import PdfFileReader , PdfFileWriter
readFile = r'C:\Users\莫再提\Downloads\E7B86v3.0.pdf'

read_pdf = PdfFileReader(readFile)
#讀取PDF檔案

documentInfo = read_pdf.getDocumentInfo()
print('documentInfo = %s' % documentInfo)
#取得頁面資訊

pageLayout = read_pdf.getPageLayout()
print('pageLayout = %s' % pageLayout)
#取得頁面配置

pageMode = read_pdf.getPageMode()
print('pageMode = %s' % pageMode)
#取得頁面模式

xmpMetadata = read_pdf.getXmpMetadata()
print('xmpMetadata = %s'% xmpMetadata)
#取得檢索資料

pageCount = read_pdf.getNumPages()
print('pageCount = %s' % pageCount)
#取得頁數

-----------------------
#新增一個PDF最後加上空白頁
from PyPDF2 import PdfFileReader , PdfFileWriter

readFile = r'C:\Users\莫再提\Downloads\E7B86v3.0.pdf'
read_pdf = PdfFileReader(readFile , strict = False) #設定讀取檔案


outFile = r'C:\Users\莫再提\Desktop\pytest\output10.pdf'
#即為輸出檔 output
write_pdf = PdfFileWriter() #將pdfw給變數

numPages = read_pdf.getNumPages() #取得總頁數
for index in range(0,numPages):
    pageobj = read_pdf.getPage(index) #取得頁面索引頁，依照索引取完每頁
    
    write_pdf.addPage(pageobj)  #增加寫入頁，寫入讀取每頁的頁面，通常由pdfFileReader讀取取得
    write_pdf.write(open(outFile,'wb'))#將每次讀取的頁面寫入output檔 這可以省略
    
write_pdf.addBlankPage() #新增一頁空白頁
write_pdf.write(open(outFile,'wb')) #再將空白頁寫入output


------------------
#將PDF分割 從第4頁開始複製
from PyPDF2 import PdfFileReader , PdfFileWriter

readFile = r'C:\Users\莫再提\Downloads\E7B86v3.0.pdf'
read_pdf = PdfFileReader(readFile , strict = False)
documentInfo = read_pdf.getDocumentInfo()
write_pdf = PdfFileWriter()
outFile = r'C:\Users\莫再提\Desktop\pytest\output11.pdf'
numPages = read_pdf.getNumPages()
#a = read_pdf.numPages
#b = read_pdf.getNumPages()   此兩個方法都能取得PDF總頁數
#print(a,b)
if numPages >3:
    
    for index in range(3,numPages):
        pageobj = read_pdf.getPage(index) #頁數索引從0開始，將頁面取出來
        write_pdf.addPage(pageobj)
        
    
    write_pdf.write(open(outFile, 'wb')) #最後才用write寫入並另外存檔給OUTFILE


---------------
#合併三頁PDF
import PyPDF2

pdfFiles = [r'C:\Users\莫再提\Desktop\pytest\out1.pdf',\
            r'C:\Users\莫再提\Desktop\pytest\out2.pdf',\
                r'C:\Users\莫再提\Desktop\pytest\out3.pdf']
           #創建一個串列
    
write_pdf = PyPDF2.PdfFileWriter()#將寫入方法給此變數
pdfOutput = open(r'C:\Users\莫再提\Desktop\pytest\comb.pdf','wb')    
for fileNum in pdfFiles:#依續開啟三個檔案
    read_pdf = PyPDF2.PdfFileReader(open(fileNum,'rb'))#用讀取開起三ㄍ檔
    for pageNum in range(read_pdf.numPages):#看此檔有幾頁
        print(read_pdf.getPage(pageNum))#依照索引值取頁面資訊
        write_pdf.addPage(read_pdf.getPage(pageNum))#依照索引值取頁面資訊，加入PDF
write_pdf.write(pdfOutput)
pdfOutput.close()


"""
txt文字檔處理

"""
#作txt的讀取，練習score 統計分數共幾人
f = open(r'C:\Users\莫再提\Documents\python-sql-for-test\python\練習資料\score.txt')#唯讀 沒加參數
a = f.read()
L = a.split() #分割字串去除' ' '\n'，串列中的資料是字串
for i in range(0,len(L)):#將文字轉為數字加到串列
    L[i] = int(L[i]) 

c = [0,0,0,0,0,0] #紀錄級距人數
for x in L:
    if x >= 90:
        c[0] += 1
    elif x >= 80:
        c[1] += 1
    elif x >= 70:
        c[2] += 1
    elif x >= 60:
        c[3] += 1
    elif x >= 40:
        c[4] += 1
    else:
        c[5] += 1
#輸出各級別統計結果
print('90分以上%d人' % c[0],end=' ' )
print('89-80分以上%d人' % c[1],end=' ' )
print('79-70分以上%d人' % c[2],end=' ' )
print('69-60分以上%d人' % c[3],end=' ' )
print('59-40分以上%d人' % c[4],end=' ' )
print('39分以下%d人' % c[5],end='\n' )

---------------------------------------------------------------------------
#txt文字的寫入
import math #將資料打開命名為fin 將資料用寫入模式命名fout
with open(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\data5.txt','r') as fin:
    with open(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\data5_w.txt', 'w') as fout:
        for line in fin:
            data = math.ceil(20/(float(line)*0.001425))
            #math.ceil(數值) 取得大餘或等於的整數(最小-最接近)
            #math.floor(數值) 取得小於或等餘的整數(最大-最接近)
            print('每股價格:%5.2f, 每日需購股數:%5.0f' % (float(line),data))
            
"""
CSV讀取

"""
#讀取CSV檔
import csv
with open(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\ubike_1.csv','r',encoding = 'utf8') \
    as csvfile:#用編碼utf8開啟
        plots = csv.reader(csvfile, delimiter = ',')#用reader方法讀取 plots是個串列
                              #用delimiter設定資料以逗號分隔字元，藉以取出每個資料
        for row in plots:
            print(row[0]+' '+row[1]+' '+row[3]+' '+row[5]+' '+row[12])
      #sbi 目前有幾台 mday 更新時間 bemp 空幾台  
    
--------------------------------------------    
#讀取CSV檔
import csv
with open(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\air.csv','r',encoding = 'utf8') \
    as csvfile:#用編碼utf8開啟
        plots = csv.reader(csvfile, delimiter = ',')#用reader方法讀取 plots是個串列
                              #用delimiter設定資料以逗號分隔字元，藉以取出每個資料
        for row in plots:
            print(row[0]+' '+row[2]+' '+row[3])

#讀取+寫入 CSV檔
import csv
with open(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\stock.csv','r') \
    as fin:#用編碼utf8開啟
    with open(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\stock_out.csv','w') \
    as fout:#用編碼utf8開啟
        csvreader = csv.reader(fin, delimiter=',') #讀取csv.reader(檔案,分隔符號)
        csvwriter = csv.writer(fout, delimiter=',')#寫入csv.writer(檔案,分隔符號)
        header = next(csvreader)#先讀取第一行 next(讀取逸代對象)物件之後會從下一行開始 
        print(header)                
        csvwriter.writerow(header)
        
        for row in csvreader:#讀取除了第一行剩下的
            row[6] = row[6].replace('/','-')
            print(','.join(row))
            csvwriter.writerow(row)
        
"""
JSON檔讀取

JSON：JavaScritp Object Notation
→JavaScript 開放資料交換格式
→JSON 為JavaScript程式的一個子集合

JSON型態轉換到Python型態的對照：
object→dict
array→list
string→unicode
number(int)→int,long
number(real)→float
true→True
false→False
null→None

"""
#用PY建立JASON檔
import json
print(json.dumps(['two',{'bar':('jaz',None,2.0,1)}]))
print(json.dumps("\"two\bar"))
print(json.dumps("\u4321"))
print(json.dumps("\\"))
print(json.dumps({'c':0,'b':0,'d':0}, sort_keys=True))#排序遞增      
print(json.dumps([0,1,2,3,{'4':5,'6':7}], separators=(',',':')))#分隔符號
                                         #separators(item符號-符號是數組, dict符號-字典)
print(json.dumps({'4':5,'6':7}, sort_keys=True, indent=5))#indent會改變輸出位置
d1 = {'b':789, 'c':456, 'a':123}
d2 = json.dumps(d1,sort_keys = True,indent = 4)
#json.dumps()：將Python中的文件序列化為json格式字串
#json.loads()：為json.dumps()的反向，將已編碼的json字串解碼為Python物件
print(d2)



--------------------------------------------------
#將JSON檔轉為python物件

import json
with open(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\ubike_1.json',encoding = 'utf8')\
    as file:
    data = json.load(file)    
    for item in data:
        print([item['sno'],item['sna'],item['tot']]) #以索引列印item各欄位資料
'''
        
XML讀取

XML：eXtensible Markup Language；可延伸標記語言
→是一種電腦標記語言
→規則特性：
    →是一種標籤語法
    →以<名稱>開頭，後面接一段內容，再以</名稱>結尾。
    →忽略空格/
    →<名稱>下可能有<子名稱>，層層結構。
    →<名稱>可稱為一個節點
    →<名稱 屬性=屬性值>：代表該名稱的設定功能
    →通常用於資料傳遞與消息發佈，如RSS....，一般業界會自訂客製化的XML格式。

'''

#解碼XML
import xml.etree.ElementTree as et #載入xml.etree.ElementTree套件 解析為數狀結構
tree = et.ElementTree(file=r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\menu.xml')
#讀取XML檔，儲存到 tree 變數
root = tree.getroot() #取得根節點(即XML標籤)

print(root.tag) #輸出根節點(menu標籤名) 最上層的標籤
for child in root: #(menu標籤下的子標籤)
    print('tag',child.tag, 'attributes:' ,child.attrib) #tag：取得標籤、attrib：取得標籤屬性
    for grandchild in child: #子標籤下的子標籤
        print('\ttag:',grandchild.tag,'attributes:',grandchild.attrib)
print(len(root))      # 菜單選項的數目
print(len(root[0]))   # 早餐選項的數目

--------------------

import xml.etree.ElementTree as et

tree = et.parse(r'C:\Users\莫再提\Documents\python-sql-for-test\python\練習資料\country_data.xml')
root = tree.getroot()
print('country_data.xml的根結點:'+root.tag)
print('根結點標籤裡的屬性和屬性值:'+str(root.attrib))

for child in root:
    print(child.tag, child.attrib)
print('排名'+root[0][0].text ,'國內生產總值:'+root[0][2].text) 

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)             #標籤.iter('標籤名') 取得標籤是該名稱的所有標籤
for country in root.findall('country'):#標籤.attrib 取得該標籤屬性識字典型式 {'屬姓名':值}
    rank = country.find('rank').text    #標籤.find('標籤名') 尋找該標籤
    name = country.get('name')          #標籤.get('屬姓名') 直接取得該署性的值
    print(name,rank)                    #標籤.set(屬性 , 屬性值)：設定元素的屬性、屬性值
 -------------------------------------- 
  
#修改XML  
import xml.etree.ElementTree as et
#以parse讀取解析XML檔案
tree = et.parse(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\country_data.xml')
root = tree.getroot() #取得根節點最外層DATA標籤

for rank in root.iter('rank'):
    new_rank = int(rank.text)+1  #轉成數字做運算
    rank.text = str(new_rank)    #轉回文字檔才能修改原本的項目
    rank.set('updated' ,'yes')   #以set()方法設定 rank 標籤的屬性、屬性值 <rank updated="yes">5</rank>
                                 #Element.set(屬性 , 屬性值)：設定元素的屬性、屬性值
tree.write(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\country_data_output.xml',\
           encoding = 'utf-8')
-----------------------------------------------------
#刪除XML

import xml.etree.ElementTree as et

tree = et.parse(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\country_data.xml')
root = tree.getroot() 

for country in root.findall('country'): #依續搜尋三個國家標籤
    rank = int(country.find('rank').text) #在國家下搜尋rank標籤    
    if rank > 50:
        root.remove(country)#若 rank 標籤顯示文字大於 50
                            #則使用 remove() 方法移除根節點下的 country 標籤
tree.write(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\country_data_output01.xml',encoding = 'utf-8')


'''
網頁資料擷取及轉換

Python擷取網頁的流程:
    1.存取網站取得內容
    2.解析取得的內容
    3.處理資料(分析視覺化)

Python取得網頁資料
  靜態網頁資料:
     1.站中不含.js檔(java.scrip)
     2.伺服器回傳的是一整個網頁
     3.處理方法:需要解析html檔案
     4.HTML網頁架構:標籤tag 屬性attributr 內容content ，樹狀結構構成
     5.HTML標籤結構:<標簽名 屬性(可以多個)>內容</標籤>
     6.常用HTML標籤:(網頁爬蟲)
        <header>表頭    <h1>標題文字第一級
        <title>標題     <a href>超連結
        <body>網頁主體   <form>表單
        <div>區塊       <tr> , <td> 表格列/表格欄
        <th>標格頭
  動態網頁資料:


'''
'''
讀取網站檔案:requests
    發送GET請求:Browser輸入網址，再由伺服器回應到使用者端，不安全看得到密碼
    Requests請求:可不經過瀏覽器發送GET直接存取網頁
    
    import requests #範例
    變數 = requests.get(網址)


Beautifulsoup的解析器
    html.parser 官方的
    lxml
    xml
    html5lib
    
  方法:
    find():傳回第一個符合的標籤內容，傳回值為字串
    find_all():傳回所有符合的標籤內容，傳回值是一個串列
    find(標簽名稱,{'屬性名稱':'屬性值'})     屬性為字典型別
    find_all(標簽名稱,{'屬性名稱':'屬性值'}) 沒屬性用標籤名稱就可以   
    select():以CSS選擇器的方式讀取指定的資料，傳回值為串列
        1.讀取CSS的ID:必須於id前加上# 
          例如<div id='first'>內容</div>
          data = BeautifulSoup物件.select('#first')
        2.讀取CSS物件類別:必須在類別的前面加上.
          例如<p class='second'>內容</p>
          data = BeautifulSoup物件.select('.second')
        3.多層標籤:逐層依序寫出
          例如<html><head><title>內容</title></head></html>
          data = BeautifulSoup物件.select('html head title')
'''
#安裝爬蟲套件
#pip install requests
#pip install bs4



import csv    #載入 csv 模組，處理csv檔案格式
import requests	#載入 requests 模組，存取網站取得內容

#載入 BeautifulSoup 模組，解析網頁
#BeautifulSoup讀取 HTML 原始碼，自動進行解析並產生一個 BeautifulSoup 物件，
#此物件中包含了整個 HTML 文件的結構
from bs4 import BeautifulSoup #BeautifulSoup自動解析網路
from time import localtime, strftime, strptime, mktime    #處理時間系列
from datetime import datetime    #處理日期時間
from os.path import exists    #處理檔案儲存路徑、查看特定的路徑是否存在，不分檔案或目錄

#requests.get(網址)取得網站內容
html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")

#將取得的網站內容分析並建立物件bsObj  html.content取出網頁內容
bsObj = BeautifulSoup(html.content, "lxml")#bsobj是經過分析後的網站樹狀結構


for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"):
    #find("table", {"title":"牌告匯率"}) 找table標籤下，屬性(字典)title=牌告利率的
    #find("tbody") 然後在往下找tbody標籤
    #findAll("tr") 在tbody標籤下找出所有的tr標籤
    #findall找出所有的td儲存到cell
    cell = single_tr.findAll("td")

    #在cell[0]下找到class屬性是visible-phone的欄位
    #以contents回傳欄位內容給currency_name(匯率名稱),contents[0]代表回傳幣別名
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0]
    #contents代表欄位內容並回傳
    #刪除表格中不必要的資料如\r , \n , 空白鍵
    currency_name = currency_name.replace("\r","")
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")

    #以contents回傳欄位內容給currency_rate(匯率)
    currency_rate = cell[2].contents[0]
    #該tr標籤下第0 1 2個td標籤，並把標籤內容回傳
    print(currency_name, currency_rate)

    #建立csv檔案
    file_name = r'C:\Users\莫再提\Documents\python-sql-for-test\python\練習資料\bkt_rate' + currency_name + ".csv"

    #取得目前時間   
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    #Y西元年 m月份 d日期 H小時 M分鐘 S秒
    #寫入csv檔，如果檔案不存在，則抓取網頁上的時間及匯率寫入，若檔案存在，即使用原資料
    #如果檔案不存在，加入一行資料，以串列中的串列處理每天的匯率資料。
    #每一個串列代表擷取得每一筆匯率資料。
    if not exists(file_name):
        data = [['時間', '匯率'], [now_time, currency_rate]]
    else:
        data = [[now_time, currency_rate]]
    f = open(file_name, "a")    #開啟csv檔
    w = csv.writer(f)    #寫入csv檔
    w.writerows(data)    #寫入data物件
    f.close()    #關閉csv檔案    
    
'''
urllib :使用urllib.request的urlopen的方法取得遠端網頁，再使用read()方法讀取內容

requests :requests.get("網址") 也可以取得網頁內容

'''    
    
#抓取統一發票號嗎        
#設定Python程式中新舊版本對unicode字串與輸出入的相容性
from __future__ import unicode_literals, print_function
import urllib    #存取網頁
from bs4 import BeautifulSoup	#解析網頁
import urllib.request    #存取網頁

# 財政部官網
request_url = 'http://invoice.etax.nat.gov.tw/' 

# 以urllib.request.urlopen開啟網頁物件並以read()讀取網頁內容
htmlContent = urllib.request.urlopen(request_url).read()

#將取得的網站內容分析並建立物件soup，以html.parser方法解析(解析HTML、XHTML)
soup = BeautifulSoup(htmlContent, "html.parser") #soup被解析為一個樹狀圖

#搜尋所有網頁中標籤為span，且class屬性為t18Red者設定給results，t18Red是中獎號碼
results = soup.find_all("span", class_="t18Red")

subTitle = ['特別獎', '特獎', '頭獎', '增開六獎']     # 設定獎項串列

#搜尋所有網頁中標籤為h2，且id屬性為tabTitle者設定給months
months = soup.find_all('h2', {'id': 'tabTitle'}) 
# 最新一期，使用months物件的find_next_sibling方法找尋標籤為'h2'下的內容
month_newest = months[0].find_next_sibling('h2').text #印出月份
# 上一期months[1] 本期 momths[0]
month_previous = months[1].find_next_sibling('h2').text

print("最新一期統一發票開獎號碼 ({0})：".format(month_newest))

for index, item in enumerate(results[:4]):    #enumerate：列舉資料中的每一個項目
    #分解出 索引和標籤(中獎號嗎)網頁前4組是號碼
	print('>> {0} : {1}'.format(subTitle[index], item.text))#item會是個標籤.text出現文字
print ("上期統一發票開獎號碼 ({0})：".format(month_previous))
for index2, item2 in enumerate(results[4:8]):
	print ('>> {0} : {1}'.format(subTitle[index2], item2.text))


-------------
#練習enumerate
a1=[1,2,3,4,5,6]
for index , value in enumerate(a1):
    print(index , value)
#可以取出索引+內容

------------
#requests取得html原始碼
import requests
url = 'https://tw.yahoo.com/'
html = requests.get(url)
html.encoding = 'utf-8'
if html.status_code == requests.codes.ok: #status_code取得回應狀態碼
    print(html.text)    #requests.codes.ok 狀態碼:代表伺服器回應OK
    
f = open(r'C:\Users\ASUS\Desktop\001.text','w',encoding = 'utf8')
f.write(html.text)
-------------------------
#requests取得網址
import requests

payload = {'key1':'value1','key2':'value2'} #定義個字典

html = requests.get('http://httpbin.org/get' , params= payload) #params= payload請求附帶參數
#httpbin.org:測試網站Request(請求)及Response(回應)的服務
    #請求網址:http:httpbin.org/get
           #http://httpbin.org/post
    #若帶有參數請求則以?&合併於網址後
print(html.url) #印出網址，如果是密碼也會顯示出來

-----------------------
import requests

payload = {'key1':'value1','key2':'value2'} #定義個字典

html = requests.post('http://httpbin.org/post' , data= payload) #data= payload請求附帶參數
#httpbin.org:測試網站Request(請求)及Response(回應)的服務
    #請求網址:http:httpbin.org/get
           #http://httpbin.org/post
    #若帶有參數請求則以?&合併於網址後
print(html.text)
print(html.url)

'''
session / cookie

client 拜訪=> server 產生憑證(識別用 存在用戶cookie 存在伺服器session) => client

建立session: requests.session()
    身分認證通常搭配session使用，網頁結取(在身分認證畫面理)
    建立seesion以post方式帶入參數登入，再使用cookies帶入參數進入畫面
    

'''

import requests
from bs4 import BeautifulSoup
#查詢網頁傳頌表單的方法為post,按鈕的value值為'yes',用python寫出進入網址按下的按鈕值
# <form action="/ask/over18" method="post">
#<button class="btn-big" type="submit" name="yes" value="yes">我同意，我已年滿十八歲<br><small>進入</small></button>
payload = {
    'from': 'https://www.ptt.cc/bbs/Gossiping/index.html',
    'yes': 'yes' #第2個yes隨便打一個值都可以，代表按下yes按鈕
    }
#讓程式去模擬瀏覽器操作，騙過伺服器防護
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)'\
    'AppleWebkit/537.36 (KHTML, like Gecko) chrome/56.0.2924.87 Safari/537.36'
    }

rs = requests.Session() #建立rs物件
rs.post('https://www.ptt.cc/ask/over18',data = payload , headers = headers)
#rs認證畫面用post代參數項伺服器請求，經過這行就會產生伺服器所屬的cookie
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html',headers = headers)
#用get取得網頁內容

soup = BeautifulSoup(res.text, 'html.parser')
items = soup.select('.r-ent') 
for item in items:
    print(item.select('.date')[0].text, item.select('.author')[0].text,\
          item.select('.title')[0].text)

-----------------------------
html = '''
<html><head><title>網頁標題</title></head></html>
<p class = "header"><h2>文件標題</h2></p>
<div class="content">
    <div class="item1">
        <a href="http://example.com/one" class="red" id="link1">First</a>
        <a href="http://example.com/two" class="red" id="link2">Second</a>
    </div>
    <a href ="http://example.com/three" class="blue" id="link3">
       <img src = "http://example.com/three.jpg">Third
    </a>
</div>
'''

from bs4 import BeautifulSoup
sp = BeautifulSoup(html , 'html.parser') #sp就是網頁內容
print(sp.title)#sp.title 可以取得title標籤的內容
print(sp.find('h2'))#找出h2的標籤
print(sp.find_all('a'))#找出所有a標籤的並放入一個串列
print(sp.find_all('a',{'class':'red'})) #找所有a標籤且屬性'class'='red'的
data1 = sp.find('a',{'href':"http://example.com/one"})#找出第一個a標籤屬性href=網址的標籤
print(data1.text)#只印出標籤的內容
data2 = sp.select('#link1') #找到屬性id = link1的內容 (#)代表id,傳回是一個串列(標籤)
print(data2)
print(data2[0].text)      
print(data2[0].get('href'))   #找出屬性值可以用get或以下方法 
print(data2[0]['href'])
print(data2[0]['class'])         
print(sp.find_all(['title','h2']))#用此方法找出所有標籤為title和h2的     
print(sp.select('div img')[0]['src'])#找出在div標籤中的img標籤中的第一筆資料的src屬性     
print(sp.select('div img')[0])      
      
      
'''
瀏覽器自動化操作:Selenium，藉由指令自動操作頁面

1.安裝selenium
2.去網路下載解壓縮 chrome webDriver







'''      
#pip install selenium      
from selenium import webdriver

driver_path = r'C:\Users\ASUS\Desktop\chromedriver.exe'
url = 'https://www.facebook.com'
email = ' '
password=' '
driver = webdriver.Chrome(driver_path)

driver.maximize_window() #視窗
driver.get(url)#取得網址

driver.find_element_by_id('email').send_keys(email)  #元素id
driver.find_element_by_id('pass').send_keys(password)#元素名稱  
driver.find_element_by_id('loginbutton').click()

#driver.find_element_by_id 元素ID
#driver.find_element_by_name 元素名稱
#driver.find_element_by_tag_name 元素標簽名
#driver.find_element_by_css_selector 元素CSS選擇器
#find_element_by_link_text('衛星')

-------------------------
      
from selenium import webdriver
import time
driver_path = r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\chromedriver.exe'
web = webdriver.Chrome(driver_path)
web.get('http://www.cwb.gov.tw/V7/')
web.set_window_position(0,0) #原點0,0再畫面左上角
web.set_window_size(700,700)  #設定網頁式窗大小    
time.sleep(5) #停5秒
web.find_element_by_link_text('衛星').click() #找到連結叫衛星的點一下
time.sleep(5)
web.close() #關閉瀏覽器  




----------------------------------

from selenium import webdriver
url="https://tw.yahoo.com/"
driver_path=r"C:\Users\ASUS\Documents\Python-SQL\python\練習資料\chromedriver.exe"
browser=webdriver.Chrome(driver_path)
browser.get(url)#開啟瀏覽器

element=browser.find_element_by_id("UHSearchBox")
element.send_keys("Hello word")
sumbit=browser.find_element_by_id("UHSearchWeb").clock()

-------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver_path = r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get('http://www.python.org')
print(driver.title)
assert 'Python' in driver.title
elem = driver.find_element_by_name('q')
elem.clear()
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN) #搜尋結果傳回來
assert 'No results found.' not in driver.page_source
print(driver.page_source)   
driver.close()      
      
------------------------------------    


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver_path = r"C:\Users\ASUS\Documents\Python-SQL\python\練習資料\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get('http://www.imdb.com/')
search_elem=driver.find_element_by_css_selector("#navbar-quercy")
search_elem.send_keys("The Shape of water")
time.sleep(3)
search_button_elem=driver.find_element_by_css_selector("#navbar-submit-button .navbarSprite")
search_button_elem.click()
time.sleep(3)
first_result_elem=driver.find_element_by_css_selector("#findSubHeade+ .findSection .odd:nth-child(1) .result_text a")
first_result_elem.click()
time.sleep(3)
rating_elem=driver.find_element_by_css_selector("strong span")
rating=float(rating_elem.text)
cast_elem=driver.find_element_by_css_selector(".itemprop .itemprop")
cast_list=[cast.text for cast in cast_elem]
driver.close()
print(rating,cast_list)    
    
    
    

    
    
    
    
    
    
    
    
    
    
    



