# -*- coding: utf-8 -*-
"""
807
請撰寫一程式，要求使用者輸入一字串，該字串為五個數字，以空白隔開。請將此五個數字加總（Total）並計算平均（Average）。

3. 輸入輸出：
輸入說明
一個字串（五個數字，以空白隔開）

輸出說明
總合
平均 (輸出浮點數到小數點後第一位)

輸入輸出範例
範例輸入
-2 34 18 29 -56
範例輸出
Total = 23
Average = 4.6
"""

a = input()
b =a.split(' ')
t=0

for i in b:
    t+=eval(i)
avg=t/len(b)
print('Total = %d'%t)
print('Average = %.1f'%avg)