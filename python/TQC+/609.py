# -*- coding: utf-8 -*-
"""

"""
def area():
    lst=[]
    for i in range(1,3):
        lst.append([])
        for ii in range(1,3):
            n=eval(input('[%d, %d]: '% (i,ii)))
            lst[i-1].append(n)
    return lst

print('Enter matrix 1:')
s1=area()
print('Enter matrix 2:')
s2=area()

print('Matrix 1:')
print('%d %d '% (s1[0][0],s1[0][1]))
print('%d %d '% (s1[1][0],s1[1][1]))
print('Matrix 2:')
print('%d %d '% (s2[0][0],s2[0][1]))
print('%d %d '% (s2[1][0],s2[1][1]))
print('Sum of 2 matrices:')
print('%d %d '% (s1[0][0]+s2[0][0],s1[0][1]+s2[0][1]))
print('%d %d '% (s2[1][0]+s1[1][0],s2[1][1]+s1[1][1]))





