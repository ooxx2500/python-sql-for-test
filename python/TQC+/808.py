# -*- coding: utf-8 -*-
"""
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
"""

s = input()

ssn=1
if s[3]=='-' and s[6]=='-' and len(s)==11:
    for i in s:
        if i=='-':
            continue
        else:
            if not i.isdigit():
                ssn=1
                break
            else:
                ssn=0
if ssn==0:
    print('Valid SSN')
else:
    print('Invalid SSN')