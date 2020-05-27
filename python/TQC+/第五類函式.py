'''
502
設計說明：
請撰寫一程式，將使用者輸入的兩個整數作為參數傳遞給一個名為compute(x, y)的函式，此函式將回傳x和y的乘積。

3. 輸入輸出：
輸入說明
兩個整數

輸出說明
兩個整數相乘之乘積

輸入輸出範例
範例輸入
56
11
範例輸出
616
'''
#def 函式名稱(參數...):
#呼叫

def compute(a,b):
    return a*b
num1 = eval(input())
num2 = eval(input())
print(compute(num1,num2))


'''
504
2. 設計說明：
請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳 
a
b
 的值。

3. 輸入輸出：
輸入說明
兩個整數

輸出說明
a
b
 的值

輸入輸出範例
範例輸入
14
3
範例輸出
2744
'''
def compute(a,b):
    return a**b
num1 = eval(input())
num2 = eval(input())
print(compute(num1,num2))


'''
506
設計說明：
請撰寫一程式，將使用者輸入的三個整數（代表一元二次方程式  
a
x
2
+
b
x
+
c
=
0
  的三個係數a、b、c）作為參數傳遞給一個名為compute()的函式，該函式回傳方程式的解，如無解則輸出【Your equation has no root.】

提示：輸出有順序性

3. 輸入輸出：
輸入說明
三個整數，分別為a、b、c

輸出說明
代入一元二次方程式，回傳方程式解；如無解則輸出【Your equation has no root.】

輸入輸出範例
範例輸入1
2
-3
1
範例輸出1
1.0, 0.5
範例輸入2
9
9
8
範例輸出2
Your equation has no root.
'''
def compute(a,b,c):
    delta = b**2-4*a*c
    
    if delta <0:
        return None
    elif delta ==0:
        return -b/(2*a)
    else:
        res1 =(-b+delta**0.5)/(2*a)
        res2 =(-b-delta**0.5)/(2*a)
        return str(res1)+', '+str(res2)
        
a = eval(input())
b = eval(input())
c = eval(input())
result = compute(a,b,c)
if result == None:
    print('Your equation has no root.')
else:
    print(result)


'''
508
請撰寫一程式，讓使用者輸入兩個正整數x、y，並將x與y傳遞給名為compute()的函式，此
函式回傳x和y的最大公因數。

3. 輸入輸出：
輸入說明
兩個正整數（以半形逗號分隔）

x,y

輸出說明
最大公因數

輸入輸出範例
範例輸入1
12,8
範例輸出1
4
範例輸入2
4,6
範例輸出2
2
'''
def compute(a,b):
    gcd = 1
    k = 1
    if a > 0 and b > 0:
        while k <=a and k<=b:
            if a %k ==0 and b%k ==0:
                gcd = k
            k+=1
        return gcd
    
x ,y = eval(input())
gcd = compute(x,y)
print(gcd)




'''
510
設計說明：
請撰寫一程式，計算費氏數列（Fibonacci numbers），使用者輸入一正整數num (num>=2)，並將它傳遞給名為compute()的函式，此函式將輸出費氏數列前num個的數值。

提示：費氏數列的某一項數字是其前兩項的和，而且第0項為0，第一項為1，表示方式如下：

 
3. 輸入輸出：
輸入說明
一個正整數num (num>=2)

輸出說明
依輸入值num，輸出費氏數列前num個的數值（每個數值後方為一個半形空格）

輸入輸出範例
範例輸入1
10
範例輸出1
0 1 1 2 3 5 8 13 21 34 
範例輸入2
20
範例輸出2
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 
'''

def compute(n):
    n1 = 0
    n2 = 1
    print('%d %d' % (n1,n2), end=' ')
    for i in range(3,n+1):
        n3 = n2+n1
        print("%d" % n3,end=' ')
        n1 = n2
        n2 = n3
        
num = int(input())
compute(num)