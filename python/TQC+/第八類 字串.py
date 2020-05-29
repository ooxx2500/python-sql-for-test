# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:30:08 2020

@author: ASUS
"""

'''
802
設計說明：
請撰寫一程式，要求使用者輸入一字串，顯示該字串每個字元的對應ASCII碼及其總和。

3. 輸入輸出：
輸入說明
一個字串

輸出說明
依序輸出字串中每個字元對應的ASCII碼
每個字元ASCII碼的總和

輸入輸出範例
範例輸入
Kingdom
範例輸出
ASCII code for 'K' is 75
ASCII code for 'i' is 105
ASCII code for 'n' is 110
ASCII code for 'g' is 103
ASCII code for 'd' is 100
ASCII code for 'o' is 111
ASCII code for 'm' is 109
713
'''
total = 0
string = input()

for i in range(0,len(string)):
    num = ord(string[i])  #ord(c):c為字元參數,取得其UNICODE碼
    print("ASCII code for '%s' is %d" % (string[i],num)) # " '' " 印出''
    total += num

print(total)



'''
804
請撰寫一程式，讓使用者輸入一字串，分別將該字串轉換成全部大寫以及每個字的第一個字母大寫。

3. 輸入輸出：
輸入說明
一個字串

輸出說明
全部大寫
每個字的第一個字母大寫

輸入輸出範例
範例輸入
learning python is funny
範例輸出
LEARNING PYTHON IS FUNNY
Learning Python Is Funny
'''
st = input()
str1 = st.upper()
print(str1)

str2 = st.title()
print(str2)


'''
806
請撰寫一程式，讓使用者輸入一字串和一字元，並將此字串及字元作為參數傳遞給名為compute()
的函式，此函式將回傳該字串中指定字元出現的次數，接著再輸出結果。

3. 輸入輸出：
輸入說明
一個字串和一個字元

輸出說明
字串中指定字元出現的次數

輸入輸出範例
範例輸入
Our country is beautiful
u
範例輸出
u occurs 4 time(s)
'''

def compute(sentence, w):
    return sentence.count(w) #用count()函式

sentence = input()
word = input()
print(word, "occurs",compute(sentence,word),'time(s)')

'''
808
請撰寫一程式，提示使用者輸入一個社會安全碼SSN，格式為ddd-dd-dddd，d表示數字。若格式
完全符合（正確的SSN）則顯示【Valid SSN】，否則顯示【Invalid SSN】。

3. 輸入輸出：
輸入說明
一個字串（格式為ddd-dd-dddd，d表示數字）

輸出說明
判斷是否符合SSN格式

輸入輸出範例
範例輸入1
329-48-4977
範例輸出1
Valid SSN
範例輸入2
837-a3-3000
範例輸出2
Invalid SSN
'''

s = input()

isSSN =(len(s)==11) #True or False
if isSSN:
    for i in range(len(s)):
        if i ==3 or i==6:    #測試是否為'-'號
            if s[i] != '-':
                isSSN = False
                break
        elif not s[i].isdigit(): #除了 3 6其他會來到這判定，用isdigit()判斷是否為數字
            isSSN = False    #如果不是數字會改成False
            break
if isSSN:
    print('Valid SSN')
else:
    print('Invalid SSN')
                
'''
810
請撰寫一程式，首先要求使用者輸入正整數k（1 <= k <= 100），代表有k筆測試資料。每一
筆測試資料是一串數字，每個數字之間以一空白區隔，請找出此串列數字中最大值和最小值之間的差。

提示：差值輸出到小數點後第二位。

3. 輸入輸出：
輸入說明
先輸入測試資料的筆數，再輸入每一筆測試資料（一串數字，每個數字之間以空白區隔）

輸出說明
每個串列數字中，最大值和最小值之間的差

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
4
94 52.9 3.14 77 46
90.86
-2 0 1000.34 -14.4 89 50
1014.74
87.78 33333 29.3
33303.70
9998 9996 9999
3.00
'''               
k = eval(input()) 

for i in range(k):
    str_num = input()
    str_num_list = str_num.split(' ')
    str_num_list = [eval(x) for x in str_num_list]#!!經典必學!!把文字串列轉為數字 
    print('%.2f' % (max(str_num_list)-min(str_num_list)))      

--------------------------------------
a='-2 34 18 29 -56' ##!!經典必學!!把文字串列轉為數字        
b=a.split(' ')
print(b)       
c=[eval(x)for x in b ]
print(c)         
--------------------------------------                
                

