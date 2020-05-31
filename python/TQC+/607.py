# -*- coding: utf-8 -*-
"""
607

請撰寫一程式，讓使用者輸入三位學生各五筆成績，接著再計算並輸出每位學生的總分及平均分數。

    提示：平均分數輸出到小數點後第二位。

3. 輸入輸出：
輸入說明

三位學生各五筆成績
輸出說明

格式化輸出每位學生的總分及平均分數
輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示

The 1st student:
78
89
88
70
60
The 2nd student:
90
78
66
68
78
The 3rd student:
69
97
70
89
90
Student 1
#Sum 385
#Average 77.00
Student 2
#Sum 380
#Average 76.00
Student 3
#Sum 415
#Average 83.00
"""



lst=[]
s = ['1st','2nd','3rd']
for i in range(3):
    lst.append([])
    print('The %s student:'% s[i])   
    for ii in range(5):
        n = eval(input())
        lst[i].append(n)
    
for i in range(1,4):
    print('Student %d' % i)
    print('#Sum %d'% sum(lst[i-1]))         
    print('#Average %.2f'% (sum(lst[i-1])/len(lst[i-1])))    
     






















    
        
        