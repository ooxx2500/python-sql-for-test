# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
--------------------------------------------------------
選擇敘述
1.
def funtion(a , b , c):      
    import math   
    if (b**2-4*a*c) >0:
        ans1 = (-b+math.sqrt(b**2-4*a*c))/2/a
        ans2 = (-b-math.sqrt(b**2-4*a*c))/2/a
        print( "方程式的解為%f與%f" % (ans1 ,ans2 ))
    elif (b**2-4*a*c) ==0:
        ans1 = (-b+math.sqrt(b**2-4*a*c))/2/a
        print( "方程式的解為%f" % ans1)
    else:
        print("無解")
  


    
a , b , c = eval(input("輸入a ,b ,c")) 
funtion(a , b ,c) 

funtion(2,-8,6)
funtion(1 ,-4,4)
funtion(2,1,1)         

2.

def center(x , y):
    import math
    
    c = math.sqrt(x**2+y**2)
    if c >8:
        print("此點在園外")
    else:
        print("此點在園內")
    
center(3,6)
center(8,9)

3.

def randomnum():
    import random
    num = random.randint(1 , 100)
    if num % 15 == 0:
        print("%d是3和5的倍數" % num)
    elif num % 5 == 0:
        print("%d是5的倍數" % num)
    elif num % 3 == 0:
        print("%d是3的倍數" % num)
    else:
        print("%d不是3和5的倍數" % num)    
randomnum()    
    
4.

num = input("輸入16進為字元")

if ord(num.upper()) < 71:

    a = eval("0x" + num.lower())

    print(a)
else:
    print("超過範圍")

#ord("G")



5.

num = eval(input("輸入整數:"))

if num % 40 == 0:
    print("%d可以被8,5整除"%num)
elif num % 8 == 0:
    print("%d可以被8整除" %num)
elif num % 5 == 0:
    print("%d可以被5整除" %num)
else:
    print("%d不可以被5及8整除" %num)


------------------------------------------------------------
基本語法
1.
def degree(ws):
    c = (ws - 32)*5/9
    return c , ws



def main():    
    temp = eval(input("輸入華氏溫度:"))   
    a , b = degree(temp)
    print("華氏為%6.2f------>攝氏為%6.2f" % (b , a))

main()



2.
def fivearea(r):
    import math
    s = 2*r* math.sin(math.pi/5)
    area = 5*s**2/(4*math.tan(math.pi/5)) 
    print("面積是",area)
    
rr= eval(input("請輸入半徑:"))   
    
fivearea(rr)


3.
def long (v ,a):
    length = v**2 / (2*a)
    print("最小長度為%5.2f公尺" % length)


def main():    
    meter , a = eval(input("輸入公尺/秒的速度: 及加速度: "))   
    long(meter , a )

main()



4.
def calories(m , f ,i  ):
    Q =abs( m * (f - i ) *4184)
    print("Q=%5.2f焦耳" %Q)

def main():    
    m , f , i= eval(input("輸入熱水量(公斤)、起始溫度、最終溫度:"))   
    calories( m, f , i )

main()

5.
def area(r ,h ):
    import math
    area = r**2 * math.pi
    volume = area * h
    print("area:%4.2f , volume:%4.2f" % (area , volume))

def main():    
    r , h = eval(input("輸入半徑、高度:"))   
    area( r, h)
main()

