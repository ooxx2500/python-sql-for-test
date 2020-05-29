# -*- coding: utf-8 -*-
"""
705
2. 設計說明：
請撰寫一程式，依序輸入五個、三個、九個整數，並各自儲存到集合set1、set2、set3中。接著
回答：set2是否為set1的子集合（subset）？set3是否為set1的超集合（superset）？

3. 輸入輸出：
輸入說明
依序分別輸入五個、三個、九個整數

輸出說明
顯示回覆：
set2是否為set1的子集合（subset）？
set3是否為set1的超集合（superset）？

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
Input to set1:
3
28
-2
7
39
Input to set2:
2
77
0
Input to set3:
3
28
12
99
39
7
-1
-2
65
set2 is subset of set1: False
set3 is superset of set1: True
"""
s1=set()
s2=set()
s3=set()
print('Input to set1:')
for i in range(5):
    n = input()
    s1.add(n)
print('Input to set2:')
for i in range(3):
    n = input()
    s2.add(n)
print('Input to set3:')
for i in range(9):
    n = input()
    s3.add(n)
    
print('set2 is subset of set1:',s2<=s1)
print('set3 is superset of set1:' ,s3>=s1)













