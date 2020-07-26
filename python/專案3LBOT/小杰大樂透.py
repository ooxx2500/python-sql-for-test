# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:21:48 2020

@author: ASUS
"""



def biglotto():
    list1 = [x for x in range(1,50)]
    random.shuffle(list1)    
    loto=list1[:6]
    loto.sort()
    retext ='預測號碼是:'
    for i in loto:
        retext+=str(i)+" "
    return retext


def powerlotto(): 
    list1 = [x for x in range(1,39)]   
    random.shuffle(list1)    
    list2 = [x for x in range(1,9)]    
    random.shuffle(list2)    
    loto1=list1[:6]
    loto2=list2[0]
    loto1.sort()
    retext="預測號碼第一區:"
    for i in loto1:
        retext+=str(i)+" "
    retext+="特別號:"+str(list2[0])
    return retext
import random    

intext=input('輸入:') #使用者輸入
if intext=="我要威力彩":
    retext=powerlotto()
    print(retext)
elif intext=="我要大樂透":
    retext=biglotto()
    print(retext)
else:
    retext='無法識別'
    print(retext)












