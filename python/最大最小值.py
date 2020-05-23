# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:20:30 2020

@author: 莫再提
"""

import random

list1=[random.randint(1,100) for x in range(101)]
sort1=[]
while len(list1)!= 1:
    a = list1[0]
    type(a)
    for i in range(len(list1)):
       
        if list1[i] > a:
            a= list1[i]

        else:
            continue
    c=list1.index(a)
    b=list1.pop(c)
    sort1.append(b)
    
for i in range(len(sort1)):
    if (i+1) %10==0:
        print("%3d"%sort1[i])
    
    else:
        print("%3d"%sort1[i] , end=" ")
    
    
print()    
    
reverse1=sort1[::-1]
    
    
for i in range(len(reverse1)):
    if (i+1) %10==0:
        print("%3d"%reverse1[i])
    
    else:
        print("%3d"%reverse1[i] , end=" ")