# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入二個分數，分別是x/y和m/n（其中x、y、m、n皆為正整數），計算這兩個分數
的和為p/q，接著將p和q傳遞給名為compute()函式，此函式回傳p和q的最大公因數（
Greatest Common Divisor, GCD）。再將p和q各除以其最大公因數，最後輸出的結果必須以最簡分數表示。
3. 輸入輸出：
輸入說明

四個正整數（以半形逗號分隔）
x,y
m,n
輸出說明

兩個分數和的最簡分數
輸入輸出範例

無
範例輸入1

1,2
1,6

範例輸出1

1/2 + 1/6 = 2/3

範例輸入2

12,16
18,32

範例輸出2

12/16 + 18/32 = 21/16
"""







def compute(p,q):
    if q < p:
        maxi=1
        for i in range(2,q+1):
            if p % i ==0 and q % i==0:
                maxi=i
    elif q > p:      
        maxi=1
        for i in range(2,p+1):
            if p % i ==0 and q % i==0:
                maxi=i
    return maxi

x , y = eval(input())
m , n = eval(input())


up =x*n+y*m
down = y*n



 
ansup=up//compute(up,down)
ansdown=down//compute(up,down)



print('%d/%d + %d/%d = %d/%d'%(x,y,m,n,ansup,ansdown))













    