# -*- coding: utf-8 -*-
"""
Created on Tue May 26 09:14:21 2020

@author: ASUS
"""
'''
101
1. 題目說明:
請開啟PYD101.py檔案，依下列題意進行作答，輸入整數及進行格式化輸出，使輸出值符合題意要求。作答完成請另存新檔為PYA101.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入四個整數，然後將這四個整數以欄寬為5、欄與欄間隔一個空白字元，再以每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

3. 輸入輸出：
輸入說明
四個整數

輸出說明
格式化輸出

輸入輸出範例
範例輸入
85
4
299
478
範例輸出
|   85     4|
|  299   478|
|85    4    |
|299   478  |
4. 評分項目：
項目	配分	得分
(1) 符合設計說明輸出正確格式	10	0
總 分	10	0
'''
#TODO
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())


#向右靠齊
#TODO
print('|%5d %5d|' % (num1,num2) )

print('|%5d %5d|' % (num3,num4) )

#向左靠齊
#TODO
print('|%-5d %-5d|' % (num1,num2) )
print('|%-5d %-5d|' % (num3,num4) )



'''
102
2. 設計說明：
請撰寫一程式，輸入四個分別含有小數1到4位的浮點數，然後將這四個浮點數以欄寬為7、欄與欄間隔一個空白字元、每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

提示：輸出浮點數到小數點後第二位。

3. 輸入輸出：
輸入說明
四個浮點數

輸出說明
格式化輸出

輸入輸出範例
範例輸入
23.12
395.3
100.4617
564.329
範例輸出
|  23.12  395.30|
| 100.46  564.33|
|23.12   395.30 |
|100.46  564.33 |

'''


#TODO
num1 = eval(input())
num2 = eval(input())
num3 = eval(input())
num4 = eval(input())


#向右靠齊
#TODO
print('|%7.2f %7.2f|' % (num1,num2) )

print('|%7.2f %7.2f|' % (num3,num4) )

#向左靠齊
#TODO
print('|%-7.2f %-7.2f|' % (num1,num2) )
print('|%-7.2f %-7.2f|' % (num3,num4) )



'''
103
2. 設計說明：
請撰寫一程式，輸入四個單字，然後將這四個單字以欄寬為10、欄與欄間隔一個空白字元、每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

3. 輸入輸出：
輸入說明
四個單字

輸出說明
格式化輸出

輸入輸出範例
範例輸入
I
enjoy
learning
Python
範例輸出
|         I      enjoy|
|  learning     Python|
|I          enjoy     |
|learning   Python    |
'''

# TODO
world1 = input() 
world2 = input() 
world3 = input() 
world4 = input() 

# 靠右對齊
# TODO
print('|%10s %10s|' % (world1,world2))
print('|%10s %10s|' % (world3,world4))
# 靠左對齊
# TODO
print('|%-10s %-10s|' % (world1,world2))
print('|%-10s %-10s|' % (world3,world4))

'''
104-!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
2. 設計說明：
請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）。

提示1：需import math模組，並使用math.pi。
提示2：輸出浮點數到小數點後第二位。

3. 輸入輸出：
輸入說明
半徑

輸出說明
半徑
周長
面積

輸入輸出範例
範例輸入1
10
範例輸出1
Radius = 10.00
Perimeter = 62.83
Area = 314.16
範例輸入2
2.5
範例輸出2
Radius = 2.50
Perimeter = 15.71
Area = 19.63
'''

import math
PI = math.pi

# TODO
radius = eval(input()) #
# TODO
print('Radius = %.2f' % radius)
print('Perimeter = %.2f' % (2*PI*radius))
print('Area =% .2f' % (pow(radius,2)*PI))


"""
Radius = _
Perimeter = _
Area = _
"""



'''
105
2. 設計說明：
請撰寫一程式，輸入兩個正數，代表一矩形之寬和高，計算並輸出此矩形之高（Height）、寬（Width）、周長（Perimeter）及面積（Area）。

提示：輸出浮點數到小數點後第二位。

3. 輸入輸出：
輸入說明
高、寬

輸出說明
高
寬
周長
面積

輸入輸出範例
範例輸入
23.5
19
範例輸出
Height = 23.50
Width = 19.00
Perimeter = 85.00
Area = 446.50
'''

h = eval(input()) #
w = eval(input()) #
# TODO
peri = (h+w)*2
area = h*w
print('Height = %.2f' % h)
print('Width = %.2f' % w)
print('Perimeter = %.2f' % peri)
print('Area = %.2f' % area)


"""
Height = _
Width = _
Perimeter = _
Area = _
"""

'''
106
2. 設計說明：
假設一賽跑選手在x分y秒的時間跑完z公里，請撰寫一程式，輸入x、y、z數值，
最後顯示此選手每小時的平均英哩速度（1英哩等於1.6公里）。

提示：輸出浮點數到小數點後第一位。

3. 輸入輸出：
輸入說明
x（min）、y（sec）、z（km）數值

輸出說明
速度

輸入輸出範例
範例輸入
10
25
3
範例輸出
Speed = 10.8
'''
x = eval(input())#
y = eval(input())#
z = eval(input())#
# TODO
avg_speed = (z/1.6)/(60*x+y)*60*60 #轉英里 轉秒
print('Speed = %.1f' % avg_speed)

"""
Speed = _
"""

'''
107
2. 設計說明：
請撰寫一程式，讓使用者輸入五個數字，計算並輸出這五個數字之數值、總和及平均數。

提示：總和與平均數皆輸出到小數點後第1位。

3. 輸入輸出：
輸入說明
五個數字

輸出說明
輸出五個數字
總和
平均數

輸入輸出範例
範例輸入1
20
40
60
80
100
範例輸出1
20 40 60 80 100
Sum = 300.0
Average = 60.0
範例輸入2
88.7
12
56
132.55
3
範例輸出2
88.7 12 56 132.55 3
Sum = 292.2
Average = 58.5
'''

num1 = eval(input())#
num2 = eval(input())#
num3 = eval(input())#
num4 = eval(input())#
num5 = eval(input())#
# TODO
total = num1+num2+num3+num4+num5
avg = total / 5
print(num1,num2,num3,num4,num5)
print('Sum = %.1f' % total)
print('Average = %.1f' % avg)

"""
Sum = _
Average = _
"""

'''
108
2. 設計說明：
請撰寫一程式，讓使用者輸入四個數字x1、y1、x2、y2，分別代表兩個點的座標(x1, y1)、(x2, y2)。計算並輸出這兩點的座標與其歐式距離。

提示1：歐式距離  


提示2：兩座標的歐式距離，輸出到小數點後第4位

3. 輸入輸出：
輸入說明
四個數字x1、y1、x2、y2

輸出說明
座標1
座標2
兩座標的歐式距離

輸入輸出範例
範例輸入
2
1
5.5
8
範例輸出
( 2 , 1 )
( 5.5 , 8 )
Distance = 7.8262
'''

x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())

dist = ((x2-x1)**2+(y2-y1)**2)**0.5
print('(',x1,',',y1,')')
print('(',x2,',',y2,')')
print('Distance = %.4f' % dist)


'''
109
請撰寫一程式，讓使用者輸入一個正數s，代表正五邊形之邊長，計算並輸出此正五邊形之面積（Area）。

提示1：建議使用import math模組的math.pow及math.tan
提示2：正五邊形面積的公式：  

 
提示3：輸出浮點數到小數點後第四位。

3. 輸入輸出：
輸入說明
正數s

輸出說明
正五邊形面積

輸入輸出範例
範例輸入
5
範例輸出
Area = 43.0119
'''
# TODO
import math
s = eval(input())#

# TODO
area = (5*math.pow(s,2))/(4*math.tan(math.pi/5))

print('Area = %.4f'% area)



'''
110
2. 設計說明：
請撰寫一程式，讓使用者輸入兩個正數n、s，代表正n邊形之邊長為s，計算並輸出此正n邊形之面積（Area）。

提示1：建議使用import math模組的math.pow及math.tan
提示2：正n邊形面積的公式如下： 
 
提示3：輸出浮點數到小數點後第四位

3. 輸入輸出：
輸入說明
正數n、s

輸出說明
正n邊形面積

輸入輸出範例
範例輸入
8
6
範例輸出
Area = 173.8234
'''

import math
# TODO

n = eval(input())
s = eval(input())

# TODO

area = (n*s**2)/(4*math.tan(math.pi/n))
print('Area = %.4f' % area)




"""
Area = _
"""













