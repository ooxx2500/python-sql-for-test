# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:25:48 2020

@author: ASUS
"""
#第一題
def computer(lst, a=3):
    b=[]
    lst.sort()
    lst.reverse()
    for i in range(0,a):        
        b.append(lst[i])        
    return print(b)

def main():
    lst = []
    for i in range(1,11):
        num = eval(input("請輸入第%d次數字:"%i))
        lst.append(num)

    print(lst)
    print(computer(lst))
    
main()
      
        
        
-------------------------------
#第一題

def computer(lst, a=3):
    lst.sort()
    ans = []
    for i in range(-1,-a-1,-1):
        ans.append(lst[i])
    return ans

def main():
    lst = []
    for i in range(10):
        num = eval(input("請輸入數值:"))
        lst.append(num)
    print(lst)
    print(computer(lst))
main()

-------------------------------------------
#第2提

def lotto():
    import random
    num = []
    while len(num)<6:
        n = random.randint(1,49)
        if n in num:
            continue
        else:
            num.append(n)
    num.sort()        
    print(num)             
  
def main():
    for i in range(5):
        lotto()
main()
-----------------------------------------------------
#第2提
import random
def lotto():
    lottoLst = []
    count = 0
    while count <6:
        lottoNum = random.randint(1,49)
        if lottoNum not in lottoLst:
            lottoLst.append(lottoNum)
            count +=1
    lottoLst.sort()
    print(lottoLst)
    
def main():
    for i in range(5):
        lotto()
main()


-------------------------------------
#第三題 可重複
import random

def find(a=2):
    randLst = [random.randint(1,1000) for x in range(100)]
    randLst.sort()
    max2=randLst[-a]
    min2=randLst[a-1]
    for i in range(1,len(randLst)+1):
        if i %10==0:
            print("%4d"%randLst[i-1])
        else:
            print("%4d"%randLst[i-1], end="")    
    print()
    print("第%d大是%d,第%d小是%d"%(a,max2,a,min2) )


find()




-----------------------------------
import random
randLst=[]
for i in range(100):
    randNum = random.randint(1,1000)
    randLst.append(randNum)

randLst.sort()
for j in range(1,101):
    if j%10==0:
        print('%4d'%(randLst[j-1]))
    else:
        print("%4d"%(randLst[j-1]),end =""   )

print()
print(randLst[1])
print(randLst[len(randLst)-2])


-------------------------------
#不可重複
import random

def find(a=2):
    randLst=[]
    while len(randLst) <100:
        num = random.randint(1,1000)
        if num in randLst:
            continue
        else:
            randLst.append(num)
    randLst.sort()
    max2=randLst[-a]
    min2=randLst[a-1]
    for i in range(1,len(randLst)+1):
        if i %10==0:
            print("%4d"%randLst[i-1])
        else:
            print("%4d"%randLst[i-1], end="")    
    print()
    print("第%d大是%d,第%d小是%d"%(a,max2,a,min2) )


find()






