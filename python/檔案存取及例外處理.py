# -*- coding: utf-8 -*-
"""
Created on Mon May 25 09:16:12 2020

@author: ASUS
"""

'''
檔案存取及例外處理

檔案運作流程:1.使用open函式開啟檔案及設定模式
          2.使用write()寫入函式寫入檔案，read()讀取函式讀取資料
          3.使用關閉函式close()關閉檔案

開啟檔案:open()函式  格式open(開啟檔案的完整路徑 ,開啟模式'r' 'w' 'a')
開啟模式:r(讀取):檔案指標指向檔案開頭，如檔案不存在，會發生錯誤
       w(寫入):檔案指標指向檔案開頭，並會清除原本檔案的內容，如檔案不存在，w會建立新檔
       a(附加):檔案指標在原檔案的結尾，寫入的檔案會加在原檔後面，如檔案不存在，w會建立新檔
       #若存取的是二進位檔案，則將開啟模式參數後加個b('rb' 'wb' 'ab')
       r+(讀寫模式):
       w+(讀寫模式):要配合seek()函式使用
       a+(讀寫模式):要配合seek()函式使用
       
   seek():移動指標
   格式:seek(offect,where)
       offect:移動的byte數
       where:從哪開始位移(0:開頭 1:目前位置 2:尾巴)
       (python執行寫入檔案後指標會在最後的位置上:檔尾)
       
       
檔案的路徑:檔案路徑若未指定，則以當時執行的系統預設路徑作為存取依據
         若未給路徑，只給檔案名稱，自訂路徑程程式碼撰寫時路徑分隔符號以\\為主
       
讀取與寫入:
寫入模式:write('寫入的字串')
讀取模式:read():讀取所有的內容
        read(n):讀取n個字元
        readlines():也是讀取所有的內容，也就是所有的行
        readline():讀一行
       
repr()函式 印出轉義/逸脫字元，即字串資料包含逸脫字元(\n \\),則不值型轉義字元功能，直接印出        




'''

----------------------------------------------
#寫入檔案，檔案不存在則建立
ad='C:\\Users\\ASUS\\Desktop\\Software\\pytest\\test1.txt'

def main():
    outfile = open(ad,'w')
    outfile.write('Banana\n')
    outfile.write('Grape\n')
    outfile.write('Orange\n')
    outfile.write('芒果\n')
    outfile.write('蘋果\n')
    outfile.close()
main()
-------------------------------------------
#一行一行讀出來 讀取模式
infile =open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\test1.txt','r')
print('使用readline()方法:')
line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()
line4 = infile.readline()
line5 = infile.readlines()
print()
print(repr(line1)) #repr()函式 印出轉義字元
print(repr(line2))
print(repr(line3))
print(repr(line4))
print(repr(line5))
infile.close()
--------------------------------------
#read()
infile =open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\test1.txt','r')
line1=infile.read()
print('使用read()方法:')
print(repr(line1)) #repr()函式 印出轉義字元
print(line1)
infile.close()
#readlines()
infile =open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\test1.txt','r')
print('使用readlines()方法:')
line1=infile.readlines()
print(line1)
infile.close()

--------------------------------------------
#read(n)
infile =open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\test1.txt','r')
print('使用read(3)方法:')
line1=infile.read(3)
print(repr(line1))
print('使用read(8)方法:')
line2=infile.read(8)
print(repr(line2))
infile.close()

----------------------------------------
#用迴圈一次讀一行讀所有內容
def main():
    infile =open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\test1.txt','r')
    line = infile.readline()
    while line!= '':  #一值到不等於空字串
        print(line)
        line = infile.readline()
    infile.close()
main()           
----------------------------------
#分兩次讀寫
def main():
    outfile =open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\test1.txt','w')
    outfile.write('Taipei\n')
    outfile.write('Lonfon\n')
    outfile.write('Coventry\n')
    outfile.close()
    
    infile =open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\test1.txt','r')
    data = infile.read()
    print(data)
    print(repr(data))  
    infile.close()
main()
------------------------------------    
#使用w+讀寫模式
def main():
    outfile =open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\test1.txt','w+')
    outfile.write('Taipei\n')
    outfile.write('Lonfon\n')
    outfile.write('Coventry\n')
    outfile.seek(0,0)
    data = outfile.read()
    print(data)
main()    
    
'''    
二進位檔案存取:載入pickle模組 import pickle
    使用dump函式寫入二進位資料
        pickle.dump(輸入的資料,open('C:\\Users\\ASUS\\...','wb'))
    使用load函式讀取二進位資料
        pickle.load(open('C:\\Users\\ASUS\\...','rb'))
    數值(大量)以二進位模式操作可以加快效率

for:定數迴圈(執行次數固定)
while:不定數迴圈(執行次數不固定)


例外異常處理1:當成是運作異常時處理機制
    try:
        程式執行主體
    except 異常型態:
        處理方式
例外異常處理n
    try:
         程式執行主體
    except 異常型態1:
        處理1
        
    except 異常型態n:
        處理n    
    except:    #當以上異常都未發生時,要怎處理異常  
        處理n+1
    else:
        都未發生異常，要如何處理
    finally:
        不管有無錯誤，最後一定要會執行        
    
SyntaxError:符號錯誤
ZeroDivisionError:除法分母為0的錯誤   
EOFError:檔案結尾讀取錯誤    
    
    
'''
#數入二進位資料印出來
import pickle

def main():
    outbinfile =open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\bintest.dat','wb')
    pickle.dump(123,outbinfile)    
    pickle.dump(77.7,outbinfile)  
    pickle.dump('Python is good programming',outbinfile)  
    pickle.dump([11,22,33],outbinfile) 
    outbinfile.close()
    
    inbinfile=open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\bintest.dat','rb')
    print(pickle.load(inbinfile))    
    print(pickle.load(inbinfile))     
    print(pickle.load(inbinfile))
    print(pickle.load(inbinfile))   
    inbinfile.close()
    
    
main()
--------------------------------------------
#數入二進位資料印出來
import pickle
def main():
    outfile = open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\bintest.dat','wb')
    data = eval(input('請輸入整數，輸入0結束輸入:'))
    while data!=0:
        pickle.dump(data,outfile)
        data = eval(input('請輸入整數，輸入0結束輸入:'))
    outfile.close()
    
    infile = open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\bintest.dat','rb')
    end_of_file = False
    while not end_of_file:
        try:
            print(pickle.load(infile),end = ' ')
        except EOFError: #當出現OUT OF RANGE錯誤時跳出迴圈
            end_of_file = True  #EOF end of file檔案結尾錯誤
    infile.close()
    print("\n所有資料已讀取")
main()

    
------------------------------------------------
#多種例外處理
def main():
    try:
        n1,n2 = eval(input("輸入兩個數值並以,分開"))
        ans = n1 / n2
        print('%d/%d=%d'%(n1,n2,ans))
    except ZeroDivisionError: #
        print('除法分母不可以為0')
    except SyntaxError:
        print('輸入資料須用逗號分開')
    except:
        print("輸入時發生錯誤")
    else:
        print('沒有異常')
    finally:
        print('finally子句被執行')
main()
  
---------------------------    
#題目1
import pickle
name=input("姓名:")
math=input("為積分:")  
count=input("會計:")      
indata =open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\students.dat','w')
while name != 'none':
    if name == 'none':
        break
    indata.write(name)
    indata.write(' ')
    indata.write(math)
    indata.write(' ')
    indata.write(count)
    indata.write('\n')
    name=input("姓名:")
    math=input("為積分:")  
    count=input("會計:")
indata.close()
outdata =open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\students.dat','r')    
print(outdata.read())


---------------------------------------
#解答
outfile = open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\students.dat','w')    
while True:
    name=input("姓名:")
    calculus=input("為積分:")  
    accounting=input("會計:")
    if name == 'none':
        break
    else:
        outfile.write(name)
        outfile.write(" ")
        outfile.write(calculus)
        outfile.write(" ")
        outfile.write(accounting)
        outfile.write(" ")
        outfile.write('\n')
outfile.close()


readfile = open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\students.dat','r')
data1=readfile.readline()
while data1 !='':
    print(data1)
    data1=readfile.readline()
readfile.close()





-------------------------------------------------
#題目2

readfile = open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\students.dat','r')
data1=readfile.readline()

while data1 !='':
    
    lst1 = data1.split(' ')
    acc = eval(lst1[2])
    coun = eval(lst[1])
    avg= acc*0.4+coun*0.6
    print(lst1[0],"平均是",avg)
    data1=readfile.readline()

readfile.close()


        
----------------------------------
#解答2
infile = open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\students.dat','r')
info = infile.readline()
while info !='':
    lst = info.split(' ')
    print(lst)
    calculus = eval(lst[1])
    accounting = eval(lst[2])
    average = calculus*0.6+accounting*0.4
    print('/%10s: %.2f/'%(lst[0],average))
    info = infile.readline()
infile.close()    


--------------------------------------
#題目3

infile = open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\students.dat','r')
info = infile.readline()
fname=''
fmax=0
while info !='':
    lst = info.split(' ')
    print(lst)
    calculus = eval(lst[1])
    if calculus > fmax:
        fmax=calculus
        fname= lst[0]
    accounting = eval(lst[2])
    average = calculus*0.6+accounting*0.4
    print('/%10s: %.2f/'%(lst[0],average))
    info = infile.readline()
infile.close()  

print("為積分最高是%3s%3d" % (fname,fmax))

-------------------------------------
#題目4

infile = open('C:\\Users\\ASUS\\Desktop\\Software\\pytest\\students.dat','r')
info = infile.readline()
fname=''
fmin=100
while info !='':
    lst = info.split(' ')
    print(lst)
    accounting = eval(lst[2])
    if accounting < fmin:
        fmin=accounting
        fname= lst[0]
    accounting = eval(lst[2])
    average = calculus*0.6+accounting*0.4
    print('/%10s: %.2f/'%(lst[0],average))
    info = infile.readline()
infile.close()  

print("會計最低分是%3s%3d" % (fname,fmin))

---------------------------------------------
#題目5

lst1=[]
str1 = input("請輸入字串")
while str1 !='end':
    if str1.find('B')==0:
         lst1.append(str1)  
    str1= input("請輸入字串")
for i in lst1:
    print(i,end=" ")


--------------------------------------------------
#解答

lst=[]
while True:
    str1 = input("請輸入字串")
    if str1 !='end':
        if str1.startswith('B'):
            lst.append(str1)
    else:
        break
print(lst)
            

-------------------------------------------

str1=input("請輸入字串")
fname=input('找的名字')
if str1.find(fname)==-1:
    print("is not found")
else:
    a=str1.replace(fname,'Bright')
    print(a)


----------------------------------------------
a = '\n\n\n\n\t\t\t5555\t\t66666666\n\n'            
b=a.strip()
print(repr(b))







