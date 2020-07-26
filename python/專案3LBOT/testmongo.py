# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:21:48 2020

@author: ASUS
"""

intext="我要大樂透"

import random 
list1 = [x for x in range(1,50)]
print(list1)
print()
random.shuffle(list1) 
print(list1)

loto=list1[:6]
print(loto) 
retext ='預測號碼是:'
for i in loto:
    retext+=str(i)+" "
print(retext)#回負的號碼6個隨機
-----------------------------------------------------
intext="我要威力彩"

import random 
list1 = [x for x in range(1,39)]
print(list1)
print()
random.shuffle(list1) 
print(list1)

list2 = [x for x in range(1,9)]
print(list2)
print()
random.shuffle(list1) 
print(list2)



loto1=list1[:6]
loto2=list2[0]
print("第一區號碼:",loto1)  #回負的號碼6個隨機
print(loto2)
print()
retext="預測號碼第一區:"
for i in loto1:
    retext+=str(i)+" "
retext+="特別號:"+str(list2[0])
print(retext)#回負的號碼6個隨機