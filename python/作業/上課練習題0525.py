# -*- coding: utf-8 -*-
"""
Created on Mon May 25 23:00:48 2020

@author: 莫再提
"""


opf = open('C:\\Users\\莫再提\\Desktop\\python\\students.dat','w')

name = input("輸入姓名")
math = input("輸入微積分")
acc = input("輸入會計")
while  name != 'none':
    opf.write(name)
    opf.write(' ')
    opf.write(math)
    opf.write(' ')
    opf.write(acc)
    opf.write(' ')
    opf.write('\n')
    name = input("輸入姓名")
    math = input("輸入微積分")
    acc = input("輸入會計")
opf.close()
--------------------------------------------------------------

readf=open('C:\\Users\\莫再提\\Desktop\\python\\students.dat','r')

line = readf.readline()

while line != '':
    lst = line.split(' ')
    print(lst)
    name = lst[0]
    math = eval(lst[1])
    acc = eval(lst[2])
    print('%3s的平均成績是%.2f'%(name,math*0.6+acc*0.4))
    line = readf.readline()
------------------------------------------------------

readf=open('C:\\Users\\莫再提\\Desktop\\python\\students.dat','r')

line = readf.readline()
maxmath=0
n=''
while line != '':
    lst = line.split(' ')
    name = lst[0]
    math = eval(lst[1])
    if math > maxmath:
        maxmath = math
        n = name
    line = readf.readline()
print('微積分最高是%3s %d分' % (name,maxmath))



---------------------------------------------------------
