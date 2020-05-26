# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:46:39 2020

@author: ASUS
"""

'''
201
2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是否為偶數（even）。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
判斷是否為偶數

輸入輸出範例
範例輸入1
56
範例輸出1
56 is an even number.
範例輸入2
21
範例輸出2
21 is not an even number.
'''

"""
_ is an even number.
_ is not an even number.
"""

num = int(input())

if num % 2 ==0:
    print('%d is an even number.' % num)
else:
    print('%d is not an even number.' % num)



'''
202
請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是3或5的倍數，顯示【x is a multiple of 3.】或【x is a multiple of 5.】；
若此數值同時為3與5的倍數，顯示【x is a multiple of 3 and 5.】；如此數值皆不屬於3或5的倍數，顯示【x is not a multiple of 3 or 5.】，將使用者輸入的數值代入x。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
判斷是否為3或者是5的倍數

輸入輸出範例
範例輸入1
55
範例輸出1
55 is a multiple of 5.
範例輸入2
36
範例輸出2
36 is a multiple of 3.
範例輸入3
92
範例輸出3
92 is not a multiple of 3 or 5.
範例輸入4
15
範例輸出4
15 is a multiple of 3 and 5.
'''

"""
_ is a multiple of 3 and 5.
_ is a multiple of 3.
_ is a multiple of 5.
_ is not a multiple of 3 or 5.
"""
a = int(input())
if a % 3 ==0 and a % 5 ==0:
    print('%d is a multiple of 3 and 5.' % a)
elif a % 3==0:
    print('%d is a multiple of 3.'% a)
elif a % 5==0:    
    print('%d is a multiple of 5.'% a)
else:
    print('%d is not a multiple of 3 or 5.' % a)


'''
203
2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個西元年份，然後判斷它是否為閏年（leap year）
或平年。其判斷規則為：每四年一閏，每百年不閏，但每四百年也一閏。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
判斷是否為閏年或平年

輸入輸出範例
範例輸入1
1992
範例輸出1
1992 is a leap year.
範例輸入2
2010
範例輸出2
2010 is not a leap year.
'''

"""
_ is a leap year.
_ is not a leap year.
"""
#除400等於0 除100等於0 除4等於0
year = int(input())

if year %400==0 or (year%4 ==0 and year % 100 !=0):
    print(year,'is a leap year.')
else:
    print(year,'is not a leap year.')







'''
204
2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入兩個整數a、b，然後再輸入一算術運算子 (+、-、*、/、//、%） ，輸出經過運算後的結果。

3. 輸入輸出：
輸入說明
兩個整數a、b，及一個算術運算子 (+、-、*、/、//、%）

輸出說明
運算結果 (無須做格式化)

輸入輸出範例
範例輸入
30
20
*
範例輸出1
600
'''

# TODO

a =int(input()) 
b =int(input()) 
opr = input()
ans = 0
if opr == '+': ans=a+b
elif opr == '-': ans=a-b
elif opr == '*': ans=a*b
elif opr == '/': ans=a/b
elif opr == '//': ans=a//b
elif opr == '%': ans=a%b
print(ans)








'''
205
2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個字元，判斷它是包括大、小寫的英文字母（alphabet）、數字（number）、或者其它字元（symbol）。例如：a為英文字母、9為數字、$為其它字元。

3. 輸入輸出：
輸入說明
一個字元

輸出說明
判斷是英文字母（包括大、小寫）、數字、或者其它字元

輸入輸出範例
範例輸入1
P
範例輸出1
P is an alphabet.
範例輸入2
@
範例輸出2
@ is a symbol.
範例輸入3
7
範例輸出3
7 is a number.
'''

"""
_ is an alphabet.
_ is a number.
_ is a symbol.
"""
c = input()
if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
    print(c,'is an alphabet.')
elif ('0' <= c <= '9'):
    print(c,'is a number.')
else:
    print(c,'is a symbol.')



'''
!!!!!!!!!!!!!!!!!!!!!!
206
2. 設計說明：
請使用選擇敘述撰寫一程式，根據使用者輸入的分數顯示對應的等級。標準如下表所示：

分　數	等級
80 ~ 100  A
70 ~ 79	  B
60 ~ 69	   C
<= 59	   F
3. 輸入輸出：
輸入說明
一個整數

輸出說明
判斷輸入值所對應的等級

輸入輸出範例
範例輸入
79
範例輸出
B
'''

# TODO
score = eval(input())

if 100>= score >=80:
    print('A')
elif 79 >= score >=70:
    print('B')
elif 69>= score >=60:
    print('C')
elif 59>= score:
    print('F')








'''
207
2. 設計說明：
請使用選擇敘述撰寫一程式，要求使用者輸入購物金額，購物金額需大於8,000（含）以上，並顯示折扣優惠後的實付金額。購物金額折扣方案如下表所示：

金　　額	折　扣
8,000（含）以上	9.5折
18,000（含）以上	9折
28,000（含）以上	8折
38,000（含）以上	7折
3. 輸入輸出：
輸入說明
一個數值，需大於8,000（含）以上

輸出說明
顯示折扣優惠後的實付金額（輸出不需指定小數點位數）

輸入輸出範例
範例輸入
12000
範例輸出
11400.0
'''

# TODO
cost = eval(input())
if cost >=38000:
    pay = cost*0.7
elif cost>=28000:
    pay = cost*0.8
elif cost >=18000:
    pay = cost*0.9
elif cost >=8000:
    pay = cost*0.95
print(pay)



'''
!!!!!!!!!!!!!!!!!!
208
2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個十進位整數num(0 ≤ num ≤ 15)，將num轉換成十六進位值。

提示：轉換規則 = 十進位0~9的十六進位值為其本身，十進位10~15的十六進位值為A~F。

3. 輸入輸出：
輸入說明
一個數值

輸出說明
將此數值轉換成十六進位值

輸入輸出範例
範例輸入1
13
範例輸出1
D
範例輸入2
8
範例輸出2
8
'''


num = eval(input())#

# TODO
if 0<= num <=9: hex_num = num
elif num == 10: hex_num = 'A' 
elif num == 11: hex_num = 'B' 
elif num == 12: hex_num = 'C' 
elif num == 13: hex_num = 'D'  
elif num == 14: hex_num = 'E' 
elif num == 15: hex_num = 'F' 
print(hex_num)




'''
209
2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個點的平面座標x和y值，判斷此點是否與點(5, 6)的距離小於或等於15，如距離小於或等於15顯示【Inside】，反之顯示【Outside】。

提示：計算平面上兩點距離的公式： 

3. 輸入輸出：
輸入說明
兩個數值x、y

輸出說明
小於或等於15輸出Inside；大於15輸出Outside

輸入輸出範例
範例輸入1
7
20
範例輸出1
Inside
範例輸入2
30
35
範例輸出2
Outside
'''

x = eval(input())#
y = eval(input())#

# TODO
dist = ((x-5)**2+(y-6)**2)**0.5
if dist <=15:
    print('Inside')
else:
    print('Outside')



"""
Inside
Outside
"""





'''
210
設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入三個邊長，檢查這三個邊長是否可以組成一個三角形。若可以，則輸出該三角形之周長；否則顯示【Invalid】。

提示：檢查方法 = 任意兩個邊長之總和大於第三邊長。

3. 輸入輸出：
輸入說明
三個正整數

輸出說明
可以組成三角形則輸出周長；否則顯示Invalid

輸入輸出範例
範例輸入1
5
6
13
範例輸出1
Invalid
範例輸入2
1
1
1
範例輸出2
3
'''


side1 = eval(input())#
side2 = eval(input())#
side3 = eval(input())#

#TODO
if side1+side2 > side3 \
    and side1+side3 >side2 \
    and side2+side3 >side1:
    print(side1+side2+side3)
else:
    print('Invalid')



"""
Invalid
"""




