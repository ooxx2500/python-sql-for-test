# -*- coding: utf-8 -*-
"""

主題:
1.資料處理
2.網頁資料擷取與轉換:必須會網頁結構，網頁設計(HTML5,CSS3)
3.資料分析
4.資料視覺化
5.產出報告    

python第三方函式庫:(版本區分)
    python官方
    協力廠商開發

安裝PYTHON的函式庫:以命令ANACODA 輸入: pip install 函式名稱

open data開放資料 建議格式:JSON XML、試算表MS Excel xlsx、CSV(資料用逗號分隔的)
                 文書(PDF.word.ODF....)、純文字*.txt
    
    jieba:中文分詞函式庫:使用於中文自然語言處理(Nature Language Processing NLP)
          人工智慧運用，功能是分析文章主題，分析文章內容，文章分數關聯，分析作者撰寫習慣
     步驟:1.取得文章(注意版權)
         2.將內容切割為一個個字詞
         3.tf-idf (term frequency 字詞頻率)衡量每個字詞的重要性
              字詞出現的次數 / 所有字詞總合出現次數 :字詞在文章中的重要性，越高越重要
         4.idf:(inverse document frequency 逆向檔案頻率)
              總文章數 / 某詞出現的文章數 :越高越不重要
              
    HTML轉PDF 1.安裝 pip install pdfkit
        pdfkit.from_url(網址 , 轉存的PDF位置 ,組態 ) 
        pdfkit.from_string(字串 , 轉存的PDF位置 ,組態 )
        pdfkit.from_file(檔案, 轉存的PDF位置 ,組態 )  



    HTML結構

    <table>:建立表格        
        <tr>:欄             <tr>
            <td>:欄             <td>123</td>
        <tr>:列                 <td>456</td>
    </table>               </tr>


    pypdf2:安裝pip install pypdf2
       執行PDF讀取 寫入 合併 分割


"""

#練習找文字檔西遊記的字詞
#要安裝pip install jieba
import jieba
import jieba.analyse
f = open(r'C:\Users\ASUS\Documents\Python-SQL\python\article.txt','r',encoding = 'utf8')
article = f.read()  #extract_tags(文章,取幾個出現最多的)               
tags = jieba.analyse.extract_tags(article,10) #提取字詞分析權重最大值的傳回數
print('最重要字詞:',tags) #分析出文章最重要的十個字詞

-----------------------------------------------------
#安裝pip install pdfkit
#轉PDF檔  先去安裝wkhtmltopdf
import pdfkit

config = pdfkit.configuration(wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
#使用前下載安裝wkhtmltopdf軟體 他安莊所在位置

pdfkit.from_url('https://www.csf.org.tw/main/index.asp',\
                r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\out1.pdf',configuration = config)
#將網頁轉乘PDF (網址 , 轉存的PDF位置 ,組態 )              
pdfkit.from_string('Hello world', \
                   r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\out2.pdf',configuration = config) 
#將文字轉PDF (字串 , 轉存的PDF位置 ,組態 )
pdfkit.from_file(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\CSF.html' ,\
                 r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\out3.pdf',configuration = config )    
#獎檔案轉為PDF檔 (檔案, 轉存的PDF位置 ,組態 )            

pdfkit.from_file(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\test01.html' ,\
                 r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\out4.pdf',configuration = config )
#將html檔案做成PDF


-----------------------------------------------------
#安裝pip install pdfkit
from PyPDF2 import PdfFileReader , PdfFileWriter
readFile = r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\water.pdf'

PdfFileReader = PdfFileReader(readFile)
#讀取PDF檔案

documentInfo = PdfFileReader.getDocumentInfo()
print('documentInfo = %s' % documentInfo)
#取得頁面資訊

pageLayout = PdfFileReader.getPageLayout()
print('pageLayout = %s' % pageLayout)
#取得頁面配置

pageMode = PdfFileReader.getPageMode()
print('pageMode = %s' % pageMode)
#取得頁面模式

xmpMetadata = PdfFileReader.getXmpMetadata()
print('xmpMetadata = %s'% xmpMetadata)
#取得檢索資料

pageCount = PdfFileReader.getNumPages()
print('pageCount = %s' % pageCount)
#取得頁數

-----------------------
from PyPDF2 import PdfFileReader , PdfFileWriter
#新增一個PDF最後加上空白頁
readFile = r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\health.pdf'
pdfFileReader = PdfFileReader(readFile , strict = False)
#即為health.pdf

documentInfo = pdfFileReader.getDocumentInfo()
outFile = r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\health_output.pdf'
#即為輸出檔 output
pdfFileWriter = PdfFileWriter()
numPages = pdfFileReader.getNumPages() #取得總頁數
for index in range(0,numPages):
    pageobj = pdfFileReader.getPage(index) #取得頁面索引頁，依照索引取完每頁
    
    pdfFileWriter.addPage(pageobj)  #增加寫入頁，寫入讀取每頁的頁面，通常由pdfFileReader讀取取得
    PdfFileWriter.write(open(outFile,'wb'))#將每次讀取的頁面寫入output檔
    
pdfFileWriter.addBlankPage() #新增一頁空白頁
pdfFileWriter.write(open(outFile,'wb')) #再將空白頁寫入output


------------------
#將PDF分割 3頁 後面是三頁之後的頁數
from PyPDF2 import PdfFileReader , PdfFileWriter

readFile = r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\health.pdf'
pdfFileReader = PdfFileReader(readFile , strict = False)
documentInfo = pdfFileReader.getDocumentInfo()
pdfFileWriter = PdfFileWriter()
outFile = r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\health_cut.pdf'
numPages = pdfFileReader.getNumPages()
if numPages >3:
    
    for index in range(3,numPages):
        pageobj = pdfFileReader.getPage(index) #頁數索引從0開始，將頁面取出來
        pdfFileWriter.addPage(pageobj)
    
    pdfFileWriter.write(open(outFile, 'wb')) #最後才用write寫入



import PyPDF2
#合併三頁PDF
pdfFiles = [r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\out1.pdf',\
           r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\out2.pdf',\
           r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\out3.pdf']

pdfWriter = PyPDF2.PdfFileWriter()#將寫入方法給此變數
pdfOutput = open(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\comb.pdf','wb')    
for fileNum in pdfFiles:#依續開啟三個檔案
    pdfReader = PyPDF2.PdfFileReader(open(fileNum,'rb'))#用讀取開起三ㄍ檔
    for pageNum in range(pdfReader.numPages):#看此檔有幾頁
        print(pdfReader.getPage(pageNum))#依照索引值取頁面資訊
        pdfWriter.addPage(pdfReader.getPage(pageNum))#依照索引值取頁面資訊，加入PDF
pdfWriter.write(pdfOutput)
pdfOutput.close()


--------------------------------------------------------------------
#作txt的讀取，練習score 統計分數共幾人
f = open(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\score.txt')#唯讀 沒加參數
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
print('90分以上%d人' % c[0],end=',' )
print('89-80分以上%d人' % c[1],end=',' )
print('79-70分以上%d人' % c[2],end=',' )
print('69-60分以上%d人' % c[3],end=',' )
print('59-40分以上%d人' % c[4],end=',' )
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
            
-------------------------------------
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
        
---------------------------------------------------
#用PY建立JASON檔
#JSON：JavaScritp Object Notation
#→JavaScript 開放資料交換格式
#→JSON 為JavaScript程式的一個子集合
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
JSON型態轉換到Python型態的對照：
object→dict
array→list
string→unicode
number(int)→int,long
number(real)→float
true→True
false→False
null→None
'''
----------------------------------------
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

'''
#XML：eXtensible Markup Language；可延伸標記語言
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

import xml.etree.ElementTree as et

tree = et.parse(r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\country_data.xml')
root = tree.getroot()
print('country_data.xml的根結點:'+root.tag)
print('根結點標籤裡的屬性和屬性值:'+str(root.attrib))

for child in root:
    print(child.tag, child.attrib)
print('排名'+root[0][0].text ,'國內生產總值:'+root[0][2].text) 

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name,rank)
    
    





















