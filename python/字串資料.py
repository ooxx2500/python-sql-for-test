# -*- coding: utf-8 -*-
"""
Created on Fri May 22 09:36:53 2020

@author: ASUS
"""

"""
字串(str):python並無特別區分字元及字串均以單雙引號前後誇住
    建立空字串:s1= str()  s2= " "
    建立字串:s3='ㄤㄤ你好' s4=str('我找安安')
    
    
函式:len():字串長度(字元數)
    max():字串最大值  (字元碼大小)  
    min():字串最小值
    [位置數值]:取得字串特定字元
    字串名[位置數值] 從0開始算，如果位置是負值請加上字串長度
    [起始值:終止值]取得從起始值到終止值-1的字串
    字串名[起始值:終止值]
    +:串接字串
    *:重複字串
    
字串測式:字串名.函式()
    函式():傳回值為布林值(True False)
    isalnum():字串是否為字元及數值   
    isalpha():字串是否為字元
    isdigit():字串是否為數值
    islower():字串是否為小寫
    isupper():字串是否為大寫
    isspace():字串是否為空白
    
子字串:字串名.函式('子字串')
    endswith('子字串'):字串尾端是否為子字串
    startswith('子字串':)字串開頭是否為子字串
    find('子字串'):字串中子字串的位置最小數值(開頭往右找)
    rfind('子字串'):字串中子字串的位置最大數值(尾巴往前找)
    count('子字串'):字串中子字串的個數
 
字串轉換:
    capitalize():將字串第一個字元轉換為大寫，其他都小寫    字串名.capitalize()      
    lower():將字串變小寫
    upper():將字串變大寫
    swapcase():將字串中大寫轉小寫，小寫轉大寫
    replace(str1,str2):將str1的文字用str2取代
    title():將字串中每一個單字第一個字元轉換為大寫其餘為小寫 字串名.title()
    
空白處理:字串.函式()
    lstrip():刪除字串左側空白
    rstrip():刪除字串右側空白
    strip():刪除左右空白
    
對齊:
    center(寬度值):將字串以寬度值至中對齊
    ljust(寬度值):將字串以寬度值向左對齊
    rjust(寬度值):將字串以寬度值向右對齊    
    
分割:
    split():字串分割，預設以空白字元分割字串，可以設定別的參數分割
    ex:字串.split("-") 以減號為分割字串


a,b = map(int,input("請輸入:").split())
    

"""
s1='ㄤㄤ你好我要去上課'
len(s1)   #s=9
s1[-1]   #9-1=8 找位置8的
s1[-5]
s1[3:6]
s2='mona'
s3='koko'
s4=s2+s3
s4
s5=s2*2
s5
s5.isalnum() #是否為字元及數值
s6='5557)()'
s6.isalnum()
print(s5)
s5.endswith('na')  #尾端是否為mo
s5.startswith(('mo'))

s7='today i want to plAy Computer, Computer'
s7.swapcase()  #大小互換
s7.title()   #每個單字第一碼為大寫其他小寫
s7.capitalize()  #整個字串第一個字為大寫，其他小寫
s7.replace('Computer','ball')  #替代文字

s8 ='   gogo 101   ' #刪除左右空白
s8.lstrip()
s8.strip()

s9='taipei city' #對齊
s9.ljust(20)
s9.center(20)
s11 = 'apple banana kiwi orange' #分割字元
lst = s11.split()
print(lst)
s12 = '05-22-2020'
lst1 = s12.split("-")  #分割字元以'-'減號分割
print(lst1)






