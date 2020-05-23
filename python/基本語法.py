# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:58:13 2020

@author: ASUS
"""

'''
單行註解#
多行註解'''     '''
      """      """
程式須區分大小寫
程式分行: \ + 空白建(但要在夸號內)
程式敘述以單行為主(一個完整的敘述與法)
若須在單行撰寫兩個以上的完整與法其間以;隔開一個完整的敘述)

變數定義:程式中儲存資料供程式使用隨程式執行而變動其值
變數命名規則:
    1.第一個字元可以是英文大小寫底線符號 _ 中文(但不建議使用中文)
    2.其他字元可以是英文大小寫底線符號 數字 中文(但不建議使用中文)
    3.英文大小寫視為不同的變數名稱
    4.不可以使用PYTHON定義的關鍵字、內建的含式、內建類別名稱
    5.建議:盡量以該變數在程式中代表的功能意義去命名 EX age命名年齡變數
    6.錯誤的變數名稱 class (內建的資料) abc@123 (@不合法 唸at)
                  7ava (第一個字不能數字) !name(第一個不能有符號除了底線)
                  my name(不能有空格)
    7.直接寫出不需要宣告，不須宣告變數型態系統會根據變數值自行設定
      a , b , c = 10 , 5.5 , "mona" 依序設定abc為整數 浮點 字串
    
資料型態:PYTHON會動態型別(不須先宣告)
另有強制型別宣告 int(數值) str("字串"-要用雙引號) bool(布林) float(浮點數)
相同型別資料才可以運算
PYTHON具備自動轉換型別功能，但若無法自動轉換則需要使用強制轉換型別(函數)
int(資料) str(資料) float(資料)
資料型別:type(資料) :查詢資料型態      
int:預設為十進位
另有二進位:數值前加上0b(零b) bin(資料)
   八進位:數值前加上0o(零o)  cot(資料)
   十六進位:數值前加上0x(零x)  hex(資料)

'''
a = 1
b = 100
print("sum=",a+b)

===========================
num1 = int(input("請輸入第1個數值:"))
num2 = int(input("請輸入第2個數值:"))
if num1<num2:
    tmp_num=num1
    num1=num2
    num2=tmp_num

while num2 !=0:
    tmp_num = num1 % num2
    num1=num2
    num2=tmp_num
print("最大公因數=", num1)
=========================

a = b = c = 12
y = a + \
    b + \
    c + \
    20   
print("total=", \
      y)

a = b = c = 12
y = (a +
    b +
    c +
    20)   
print("total=", 
      y)

a = 10
b = 20
print(a+b)

a = 10 ; b = 20 ; print(a+b)
    
==========================
x = 10
y = x / 3 
print(x)
print(type(x))  
print(y)
print(type(y))

==================
x = 10
x = x + 5.5

print(x)
print(type(x))

======================

x = 0b01000001
print(x)
y = 65
print(bin(y))

========================
x = 0o101
print(x)
y = 65
print(oct(y))

===================
x = 0x41
print(x)
y = 65
print(hex(y))
==========================十進位轉換其他進位
print(hex(255))
print(oct(255))
print(bin(255))


'''
運算式:由運算元運算子組成
    運算元:進行運算的資料 變數 a b c
    運算子:執行運算的動作 + - * /
      單一運算子:運算元只有一個 ex: -100  ,  not a
      二元運算子:運算元有兩個,運算子放在兩個運算元之間 EX: a+b , 100+50
      a+=1  a=a+1
      a==b  即ab相等
函式:function
內建函式:將特定功能包裝並以參數帶入資料運算執行，PYTHON已經定義完成直接依功能使用
函式格式:函式名稱(參數)
EX: 
input() 供使用者輸入資料使用
格式: 變數 = input([提示字串-告之使用者輸入啥東西)
     輸入時按下ENTER即表示輸入完畢，將輸入的資料存到變數中,檔案為字串
      
eval(): 將字串轉換為數值
格式:eval(資料)

print():輸出(格式化)
格式: print(資料 , 資料 , .... sep=分隔字元(預設為空白) ,end = '結束字元'(預設為\n 換行)) 
      sep = 'XX' end = 'YY' 都要放在最右邊
逸脫字元 \n \t
print('\n') = print() #都是換行

格式化輸出(很重要!!)
print(格式參數1 格式參數2 % 資料1 資料2)   資料可以用()誇起來()資料1 資料2
意思資料一對上格式參數1 2對2

格式參數有三種
%s  字串 
%d  整數
%f  浮點

格式參數例子
%5s :輸出5個字元
     如果小於5於左方填入空格
     如果大於5則全部輸出
    
%5d:輸出5位整數
    如果小於5於左方填入空格
    如果大於5則全部輸出

%8.2f:輸出8位數字(含小數點)有兩位小數
      若整數位小於5位  8-2(兩位小數)-1(小數點)=5
      則在數字左方填入空白
      整數大於5全部輸出,
      若小數小於兩位則在右方填入0
      + :於格式數值前方加入若數值為正則在資料左方加上"+"
      - :輸出格式資料前方有多餘時資料靠左對齊


'''
===============================

score = input("請輸入成績")
print(score) 

type(score)

score = input("請輸入成績")
sum = score + 20
print(sum)


score = eval(input("請輸入成績")) #字串轉化為數字
sum = score + 20
print(sum)
       
sum = 1 
score = 2
a = 7
b = 8                                                                                                     
print(sum , score ,a+b,end='\t',sep = '?')

print("學習程式活絡筋骨")
print(100, "python" ,200, end = "\t")
print(100, "python" ,200 , sep="&")
=================================================
格式參數例子

a = 100
print("a=/%-6d/" % a)   #x用前面格式輸出

b = 12.3
print("b = /%-7.2f/" % b)

c = "deep"
print("c=/%-6s/" % c) 

d = 50
print("d =/%+6d/" % d)

e = 13.3
print("e=/%+6.2f/" % e)

=========================================
a = eval(input("請輸入國文成績:"))
b = eval(input("請輸入英文成績:"))
c = eval(input("請輸入數學成績:"))

total = a+b+c

av = total/3

print("總成績:","%3d" % total ,"平均成績","%5.2f " % av , sep="")
print("總成績:%d平均成績:%5.2f" % (total , av))  #老師的解法後面有多個變數要用()

=====================================
'''
流程控制:以特定結構控制程式的執行方式

條件式:依定要用縮排進行程式的結構化(條件底下的敘述式一定要往右縮排)

if 條件式:       當條件式成立執行縮徘的敘述，結果是布林植 true or false        
 (縮排)敘述式

if 條件式1:       當條件成立執行敘述1，否則執行敘述2
      敘述式1
else:
      敘述式2
    
if 條件式1:  逐一判斷條件若成立責執行該敘述，執行後離開if,當所有條件不成立則執行敘述n+1
    敘述1
elif 條件2:
    敘述2
else:
    敘述3


'''

=============
print()
num = eval(input("請輸入整數:"))
if (int(num)<0):
    num = abs(num)    #絕對值
print("絕對值是%d" % num)
    
===============


num = eval(input("請輸入一個數值:"))
rem = num % 2  #取餘數
if rem == 0:
    print("偶數")
else:
    print("奇數")
    
=======================
EX: 輸入圓半徑去計算圓面積

pi = 3.14
r = eval(input("請輸入圓半徑:"))
area = r *r *pi


if r < 0:
    print("不能負數")
else:
    print("圓半徑=",r,"圓面積=",area)
    print("圓半徑=%2d 圓面積=%2.2f" % (r , area))
=================================
a ,b, c = eval(input("輸入a,b,c的值:")) #要KEY 1, 5, 8

d = b**2 - 4*a*c

if d > 0 :
    print("此一元二次方程式有兩個以上解")
elif d == 0:
    print("此一元二次方程式有一個解")
else:
    print("此一元二次方程式無解")



b=16**0.5 #開根號是**0.5

print(b)
======================================


score = eval(input("輸入分數:"))

if score > 100 or score < 0 :
    print("錯誤")
elif score >= 90:
    print("優等")
elif score >=80:
    print("甲等")
elif score >=70:
    print("乙等")
elif score >=60:
    print("丙等")
else:
    print("不及格")
==========================================

x = eval(input("輸入1-5:"))

if x == 1:
    print("one")
elif x == 2:
    print("two")
elif x == 3:
    print("three")
elif x == 4:
    print("four")
elif x == 5:
    print("five")
else:
    print("error")

'''
巢狀if:

if 條件1:
    if 條件2:  (敘述式)
       if 條件3:   (敘述式)

'''

========================================
score = eval(input("輸入分數:"))


if score>100 or score <0:
    print("error")
else:
    if score >=90:
        print("優等")
    else:
        if score >=80:
            print("甲等")
        else:
            if score >=70:
                print("乙等")
            else:
                if score >=60:
                    print("丙等")
                else:
                    print("不及格")
==========================================

x = eval(input("輸入1-4:"))

if x==1:
    print("one")
else:
    if x==2:
        print("two")
    else:
        if x==3:
            print("three")
        else:
            if x==4:
                print("four")
            else:
                print("error")
                
==================================================

'''
迴圈:重複執行的敘述
1.for:
                                                       迴圈執行時不包含終止值
for 變數 in iterator(使用range()函式) :    #range(起始值 , 終止值 ,間隔值)
    敘述式                                       預設0          預設1
                                          range(10) 0 1 2 3 4 5 6 7 8 9

2.while:當條件成立則執行敘述
    
while 條件式:
    敘述式
    




'''


for i in range(0,11):
    print(i , end=" ")

============================
#計算1+2+3+....100
sum = 0
for i in range(1,101):
    sum += i
    
print("sum=",sum)

#此為執行完for迴圈後才執行敘述二(else)
sum = 0
for i in range(1,101): #敘述一
    sum += i
else:    
    print("sum=",sum) #敘述二

========================

sum = 0

r = eval(input("輸入幾次"))

for i in range(1 ,r+1):
    sum += i
else:
    print(sum)                

=============================
#4+9+13+18+22....+85+90+94+99
sum = 0
for i in range(9,100,9):
    sum += i
for i in range(4,95,9):
    sum +=i
print(sum)

#每個a值後面的另一個序列都多5
sum = 0
for a in range(4,95,9):
    sum = sum + a +(a+5)
print(sum)

==================================
請輸入正整數:6 
6!=720   階乘 6*5*4*3*2*1

sum = 1
r = eval(input("輸入幾次"))
for i in range(1,r+1):
    sum*= i

print(sum)

==================
印出0-10

i = 0

while i <11:
    print(i)
    i=i+1

==============================
成績登入系統
請輸入第0位學生成績輸入(結束):

結果本班總成績00分 平均00分

輸入-1可以結束


score = 0
total = 0
n=0
while score != -1:
   total = total +score
   n=n+1
   score = eval(input("請輸入第%d位成績" %n))
                
avg = total / (n-1)
print("總成績", total ,"平均" ,avg ,"總人數=", n-1)





========================
total = score = person = 0
while score!= -1:
    person +=1
    total += score
    score = int(input("輸入第%d位成績" %person))

avg = total / (person-1)
print("總成績", total ,"平均" ,avg)
===========================================

ans = input("請輸入電腦的英文")

while ans.upper() !="COMPUTER":
    ans = input("請重新輸入")
else:
    print("good")


=================
輸入年齡計算票價
票價100
若小於6歲 或 大於70歲 打2折
若7~12歲 或 是60~69歲 則 打5折

======================================

age = 0
  
while age != -1:
    ticket = 100  
    age = int(input("請輸入年齡0-100, -1為結束程式:"))      
    if age == -1:
        continue

    elif -1 > age or age >100:
        print("打錯瞜給我重打")
        continue
 
    elif age <= 6 or age >= 70:
        ticket *=0.2
        print("票價為%d" % ticket)
        
    elif 7 < age <12 or  60< age < 70:
        ticket *= 0.5
        print("票價為%d"% ticket)
        
    else:
        print("票價為%d"% ticket)
        
else:
    print("已結束程式")



#1+到100
sum = 0
for i in range(1 ,101):
    sum += i
print(sum)


#99乘法表

for a in range(1,10):
    for b in range(1,10):
        c = a*b
        print( "%2d"   %c , end=" ")
    print()
        
        
        
#輸入英文MONA答對 其他請重新輸入
    
ans = input("請打中文")
while ans.upper() != "MONA":
    input("重打")
print("GOOD")    

# !6

num = 1

for i in range(1,7):
    num *= i
    
print(num)
===================================
成績登入系統
請輸入第0位學生成績輸入(結束):

結果本班總成績00分 平均00分

輸入-1可以結束


people = 0
score = 0
total = 0
while score != -1:
    people += 1
    total = total + score
    score = eval(input("地%d的成績" % people))
    
avg = total / (people - 1)

print("總成績" ,total ,"平均" , avg)
==========================================
for a in range(2 ,2):   #起始執中紙質依樣是空的
    print(a)
    
    
=============================

p = 2
x = int(input("輸入整數:"))
while p <= x :
    flag = True
    for i in range (2 , p):
        if p % i == 0:
            flag = False
            break
    if flag == True:
        print(p ,end = " ")
    p= p+1        
=============================

a=1
x = eval(input("請輸入:"))

while a <= x:
    for i in range(1,a+1):
        print(i , end = "")
    for ii in range(1 , x-a+1):
        print("*" , end="")
    print()            
    a+=1    
===============================


a=1

while a <=3:
    for i in range(1 , 3 - a+1 ):
        print("*" , end = "")
    for ii in range(1 ,a+1):
        print(ii , end = "")

    print()

    a+=1
****************************************

a = 1
x = eval(input("請輸入:"))
while a <= x:
    for i in range( 1,x-a+1 ):
        print("*" , end = "")
    for ii in range(1,  a+1 ):
        print(ii , end = "")
    print()
    a +=1
=============================================





