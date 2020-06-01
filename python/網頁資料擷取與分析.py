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
        <th>:欄             <tr>
            <td>:欄             <td>123</td>
        <tr>:列                 <td>456</td>
    </table>               </tr>


    pypdf2:安裝pip install pypdf2
       執行PDF讀取 寫入 合併 分割


"""

#練習找文字檔西遊記的字詞

import jieba
import jieba.analyse
f = open(r'C:\Users\ASUS\Documents\Python-SQL\python\article.txt','r',encoding = 'utf8')
article = f.read()  #extract_tags(文章,取幾個出現最多的)               
tags = jieba.analyse.extract_tags(article,10) #提取字詞分析權重最大值的傳回數
print('最重要字詞:',tags) #分析出文章最重要的十個字詞

-----------------------------------------------------

#轉PDF檔  先去安裝wkhtmltopdf
import pdfkit

config = pdfkit.configuration(wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
#使用前安裝wkhtmltopdf 他安莊所在位置

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


from PyPDF2 import PdfFileReader , PdfFileWriter

readFile = r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\health.pdf'
PdfFileReader = PdfFileReader(readFile , strict = False)
#即為health.pdf

documentInfo = PdfFileReader.getDocumentInfo()
outFile = r'C:\Users\ASUS\Documents\Python-SQL\python\練習資料\health_output.pdf'
#即為輸出檔 output
PdfFileWriter = PdfFileWriter()
numPages = PdfFileReader.getNumPages() #取得總頁數
for index in range(0,numPages):
    pageobj = PdfFileReader.getPage(index) #取得頁面索引頁，依照索引取完每頁
    
    PdfFileWriter.addPage(pageobj)  #增加寫入頁，寫入讀取每頁的頁面，通常由pdfFileReader讀取取得
    PdfFileWriter.write(open(outFile,'wb'))#將每次讀取的頁面寫入output檔
    
PdfFileWriter.addBlankPage() #新增一頁空白頁
PdfFileWriter.write(open(outFile,'wb')) #再將空白頁寫入output













































