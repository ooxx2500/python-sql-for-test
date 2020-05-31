# -*- coding: utf-8 -*-
"""
505
請撰寫一程式，將使用者輸入的三個參數，變數名稱分別為a（代表字元character）、x（代表個數）、y（代表列數），作為參數傳遞給一個名為compute()的函式，該函式功能為：一列印出x個a字元，總共印出y列。

    提示：輸出的每一個字元後方有一空格。

3. 輸入輸出：
輸入說明

三個參數，分別為a（代表字元character）、x（代表個數）、y（代表列數）
輸出說明

一列印出x個a字元，總共印出y列
輸入輸出範例
範例輸入

e
5
4

範例輸出

e e e e e 
e e e e e 
e e e e e 
e e e e e 

"""
def compute(a,x,y):
    for i in range(y):
        for ii in range(x):
            print(a,end=' ')
        print()




chra =input()
col =eval(input())
row =eval(input())

compute(chra,col,row)