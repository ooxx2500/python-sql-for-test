# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:51:28 2020

@author: 莫再提
"""


1.

n = 1
while n<=9:
    nn = 1
    while nn<=9:
        t = n*nn
        print('%d*%d=%2d' % (n,nn,t ),end=" ")
        nn+=1
    print()    
    n+=1
    
2. 

num = eval(input('輸入<100正整數'))

for i in range(1,num+1):
    for ii in range(1,i+1):
        print('%-4d' % ii, end='')
    print()
    
3.

a = eval(input('輸入正整數a (a<b)'))
b = eval(input('輸入正整數b (a<b)'))

total =0
for i in range(a,b+1):
    if i %2 ==0:
        total+= i
print('total=',total)


4.

num = eval(input('輸入<100正整數'))

for i in range(1,num+1):
    for ii in range(1,num-i+2):
        print('%-4d' % ii, end='')
    print()


5.

num = eval(input('輸入正整數'))

total=1
for i in range(1,num+1):
    total *= i
    print('%d! = %d' % (i,total))
    








