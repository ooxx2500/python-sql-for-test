# -*- coding: utf-8 -*-
"""
Created on Tue May 26 16:24:14 2020

@author: ASUS
"""
'''
401
請撰寫一程式，由使用者輸入十個數字，然後找出其最小值，最後輸出最小值。

3. 輸入輸出：
輸入說明
十個數值

輸出說明
十個數值中的最小值

輸入輸出範例
範例輸入
23
57
48
2
99
70
9
65
35
88
範例輸出
2
'''
# TODO
total = 10
min_num = eval(input())
for i in range(total-1):
    num = eval(input())
    if num < min_num:
        min_num = num
print(min_num)



'''
402
. 設計說明：
請撰寫一程式，讓使用者輸入數字，輸入的動作直到輸入值為9999才結束，然後找出其最小值，並輸出最小值。

3. 輸入輸出：
輸入說明
n個數值，直至9999結束輸入

輸出說明
n個數值中的最小值

輸入輸出範例
範例輸入
29
100
948
377
-28
0
-388
9999
範例輸出
-388
'''

num = eval(input())
min_num = num
while num !=9999:
    num = eval(input())
    if num < min_num:
        min_num = num
print(min_num)
# TODO







'''
出題機率低
403
2. 設計說明：
請撰寫一程式，讓使用者輸入兩個正整數a、b（a<=b），輸出從a到b（包含a和b）之間4或9的倍數
（一列輸出十個數字、欄寬為4、靠左對齊）以及倍數之個數、總和。

3. 輸入輸出：
輸入說明
兩個正整數a、b（a<=b）

輸出說明
格式化輸出兩個正整數之間4或9之倍數（包含a和b）
倍數個數
倍數總合

輸入輸出範例
範例輸入1
5
55
範例輸出1
8   9   12  16  18  20  24  27  28  32  
36  40  44  45  48  52  54  
17
513
範例輸入2
4
9
範例輸出2
4   8   9   
3
21
'''
#TODO
a = int(input())
b = int(input())
count = total_sum = 0
time =10

for i in range(a,b+1):
    if i % 4==0 or i %9==0:
        print('%-4d'%i,end = '')
        total_sum +=i
        count += 1
        if count%time ==0: #每十個換行
            print()
if count>0 and count%10 !=0:#不足十個要幫它換行
    print()
print('%d' % count)
print(total_sum)







'''
404
設計說明：
請撰寫一程式，讓使用者輸入一個正整數，將此正整數以反轉的順序輸出，並判斷如輸入0，則輸出為0。

3. 輸入輸出：
輸入說明
一個正整數或0

輸出說明
正整數反轉輸出。如輸入數值為0，輸出為0

輸入輸出範例
範例輸入1
31283
範例輸出1
38213
範例輸入2
0
範例輸出2
0
範例輸入3
135790

範例輸出3
097531
'''
# TODO

number = eval(input())
if number == 0:
    print(number)
else:
    while number !=0:
        print(number%10, end='')
        number //=10









'''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
405
設計說明：
請撰寫一程式，以不定數迴圈的方式輸入一個正整數（代表分數），之後根據以下分數與GPA的對照表，印出其所對應的GPA。假設此不定數迴圈輸入-9999則會結束此迴圈。標準如下表所示：

分　數	GPA
90 ~ 100	A
80 ~ 89	B
70 ~ 79	C
60 ~ 69	D
0 ~ 59	E
3. 輸入輸出：
輸入說明
一個正整數，直至-9999結束輸入

輸出說明
依輸入值，輸出對應的GPA

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
75
C
39
E
100
A
85
B
65
D
-9999
'''
# TODO
n = eval(input(""))
while n !=-9999:
    if 100>= n >=90:
        print('A')
    elif 89>= n >=80:
        print('B')
      
    elif 79>= n >=70:
        print('C')
       
    elif 69>= n >=60:
        print('D')
       
    elif 59>= n:
        print('E')
    n = eval(input(""))

'''
406
2. 設計說明：
請撰寫一程式，以不定數迴圈的方式輸入身高與體重，計算出BMI之後再根據以下對照表，印出BMI
及相對應的BMI代表意義（State）。假設此不定數迴圈輸入-9999則會結束此迴圈。標準如下表所示：

BMI值	代表意義
BMI < 18.5	under weight
18.5 <= BMI < 25	normal
25.0 <= BMI < 30	over weight
30 <= BMI	fat
提示： 
BMI=體重(kg)/身高2(m)
 ，輸出浮點數到小數點後第二位。 不需考慮男性或女性標準。

3. 輸入輸出：
輸入說明
兩個正數（身高cm、體重kg），直至-9999結束輸入

輸出說明
輸出BMI值
BMI值代表意義

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
176
80
BMI: 25.83
State: over weight
170
100
BMI: 34.60
State: fat
-9999
'''

"""
fat
over weight
normal
under weight
BMI: _
State: _
"""
#BMI是公尺 身高是CM 
state ='' #題目有要求所以要打
height = eval(input())
while height !=-9999: #-9999是兩個都能停止
    weight = eval(input())
    bmi = weight/(height/100*height/100)
    if weight ==-9999:
        break
    elif bmi>=30:
        state = 'fat'
    elif bmi>=25 and bmi <29.9:
        state = 'over weight'
    elif bmi>=18.5 and bmi <24.9:
        state = 'normal'
    elif bmi<18.5:
        state = 'under weight'
    print('BMI: %.2f'%bmi)
    print('State: %s'% state)

    height = eval(input())





'''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
407
2. 設計說明：
(1) 請撰寫一程式，以不定數迴圈的方式讓使用者輸入西元年份，然後判斷它是否為閏年
（leap year）或平年。其判斷規則如下：每四年一閏，每百年不閏，但每四百年也一閏。
(2) 假設此不定數迴圈輸入-9999則會結束此迴圈。

3. 輸入輸出：
輸入說明
一個正整數，直至-9999結束輸入

輸出說明
判斷是否為閏年或平年

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
2017
2017 is not a leap year.
2000
2000 is a leap year.
2016
2016 is a leap year.
2009
2009 is not a leap year.
2018
2018 is not a leap year.
-9999
'''

"""
_ is a leap year.
_ is not a leap year.
"""

y = eval(input())
while y !=-9999:
    if y %400==0 or (y%4==0 and y%100 !=0):
        print(y,"is a leap year.")
    else:
        print(y,"is not a leap year.")
    y = eval(input())



'''
408
2. 設計說明：
請撰寫一程式，讓使用者輸入十個整數，計算並輸出偶數和奇數的個數。

3. 輸入輸出：
輸入說明
十個整數

輸出說明
偶數的個數
奇數的個數

輸入輸出範例
範例輸入
69
48
19
91
83
22
18
37
82
40
範例輸出
Even numbers: 5
Odd numbers: 5
'''


"""
Even numbers: _
Odd numbers: _
"""
#判斷除2是否為0
even = odd = 0

for i in range(10):
    a = int(input())
    if a % 2 ==0:
        even +=1
    else:
        odd +=1
print('Even numbers:',even)
print('Odd numbers:',odd)






'''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
409
2. 設計說明：
某次選舉有兩位候選人，分別是No.1: Nami、No.2: Chopper。請撰寫一程式，輸入五張選票，輸入值如為1即表示針對1號候選人投票；輸入值如為2即表示針對2號候選人投票，如輸入其他值則視為廢票。每次投完後需印出目前每位候選人的得票數，最後印出最高票者為當選人；如最終計算有相同的最高票數者或無法選出最高票者，顯示【=> No one won the election.】。

3. 輸入輸出：
輸入說明
五個正整數（1、2或其他）

輸出說明
每次投完後需印出目前每位候選人的得票數
五張選票投票完成，最後印出最高票者為當選人

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
2
Total votes of No.1: Nami =  0
Total votes of No.2: Chopper =  1
Total null votes =  0
1
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  1
Total null votes =  0
8
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  1
Total null votes =  1
2
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  2
Total null votes =  1
2
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  3
Total null votes =  1
=> No.2 Chopper won the election.

程式執行狀況擷圖
下圖中的 粉紅色點 為 空格
'''

"""
Total votes of No.1: Nami = _
Total votes of No.2: Chopper = _
Total null votes = _

=> No.1 Nami won the election.
=> No.2 Chopper won the election.
=> No one won the election.
"""








'''
410
設計說明：
請撰寫一程式，依照使用者輸入的n，畫出對應的等腰三角形。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
以 * 畫出等腰三角形
（每列最後一個 * 的右方無空白）

輸入輸出範例
範例輸入
7
範例輸出
      *
     ***
    *****
   *******
  *********
 ***********
*************
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	20	0
總 分	20	0
'''
# TODO
n = eval(input())
for i in range(0,n):
    for j in range(n-i,1,-1):
        print('-',end='')
    for k in range(0,i*2+1,1):
        print('*',end='')
    print()


#外迴圈for 換行
#內圈1 印空白
#內圈2 印星號

n = 7

for i in range(1,7+1):
    for ii in range(7-i-1,-1,-1):
        print('-',end='')
    for iii in range(1,2*i,1):
        print('*',end='')
    print()


n = eval(input())


for i in range(0,n+1):
    for iii in range(0,i):
        print(' ',end='')
    for ii in range((n-i-1)*2+1,0,-1):
        print('*',end='')
  
    print()









