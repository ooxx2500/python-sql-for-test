# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:04:26 2020

@author: 莫再提
"""


# a=eval(input())
# b=eval(input())
# c=eval(input())
# d=eval(input())
# print('|%7.2f %7.2f|'%(a,b))
# print('|%7.2f %7.2f|'%(c,d))
# print('|%-7.2f %-7.2f|'%(a,b))
# print('|%-7.2f %-7.2f|'%(c,d))



# import math
# a=eval(input())
# per = 2*a*math.pi
# area = a*a*math.pi

# print('Radius = %.2f'%a)
# print('Perimeter %.2f'%per)
# print('Area = %.2f'%area)

# a=eval(input())

# if a % 15==0:    
#     print('%d is a multiple of 3 and 5.'%a)
# elif a % 3==0 : 
#     print('%d is a multiple of 3.'%a)
# elif a % 5 ==0 : 
#     print('%d is a multiple of 5.'%a)
# else:
#     print('%d is not a multiple of 3 or 5.'%a)
    
    
# a=eval(input())
# b=eval(input())
# c=input()

# if c == '+':
#     print(a+b)
# elif c == '-': 
#     print(a-b)
# elif c == '*':     
#     print(a*b)    
# elif c == '/':     
#     print(a/b)    
# elif c == '//':    
#      print(a//b)   
# elif c == '%':    
#     print(a%b)
    
    
# a=eval(input())
# b=eval(input())    
# t=0    
# for i in range(a,b+1):
#     if i % 2==0:
#         t+=i

# print(t)    
    
    
    
# a=eval(input())
# t=0
# for i in range(1,a+1):
#     if i %5==0:
#         t+=i
        
# print(t) 

    
# lst=[]
# while True:    
#     a=eval(input())
#     if a == 9999:
#         break
#     lst.append(a)
    
# lst.sort()
# print(lst[0])    
    
    
    
   
# a=eval(input())

# if a ==0:
#     print(0)
  
# while a:
#     num=a%10
#     print(num,end='')
#     a//=10



# def compute(x, y):
#     return x*y
# x=eval(input())
# y=eval(input())

# print(compute(x, y))





# def compute(x, y):
#     return x**y
# x=eval(input())
# y=eval(input())

# print(compute(x, y))


# lst=[]
# for i in range(5):
#     x=input()
#     if x =='A':
#         lst.append(1)
#     elif x =='J':
#         lst.append(11)
#     elif x =='Q':
#         lst.append(12)
#     elif x =='K':
#         lst.append(13)
#     elif 1 <eval(x) <11:
#         lst.append(eval(x))
# print(sum(lst))

# dic = dict()
# for i in range(10):
#     x=eval(input())
#     if x not in dic:
#         dic[x]=1
#     else:
#         dic[x]+=1
        
# max_c =0
# max_n =0
        
# for i in dic:
#     if dic[i] > max_c:
#         max_c = dic[i]
#         max_n = i

# print(max_n)
# print(max_c) 

   
# t1=tuple()
# t2=tuple()
# print('Create tuple1:')
# while True:
#     n = eval(input())
#     if n == -9999:
#         break
#     else:
#         t1+=(n,)


# print('Create tuple2:')

# while True:
#     n = eval(input())
#     if n == -9999:
#         break
#     else:
#         t2+=(n,)


# t3=t1+t2
# lst=list(t3)
# lst.sort()
# print('Combined tuple before sorting:',t3)

# print('Combined list after sorting:',lst)




# set1=set()

# while True:
#     n = eval(input())
#     if n ==-9999:
#         break
#     else:
#         set1.add(n)
        
# print('Length: %d'%len(set1))
# print('Max: %d'%max(set1))
# print('Min: %d'%min(set1))
# print('Sum: %d'%sum(set1))        



# s = input()
# lst=[]
# for i in s:
#     n = ord(i)
#     print("ASCII code for '%s' is %d"% (i,n))
#     lst.append(n)
    
# print(sum(lst))



# s = input()
# print(s.upper())
# print(s.title())
    


# f = open(r'C:\Users\莫再提\Downloads\read(2).txt','r')
# rf=f.readline()
# lst=rf.strip().split(' ')


# lst=[eval(i) for i in lst]

# print(sum(lst))





# data = []

# with open(r"C:\Users\莫再提\Downloads\read(3).txt","r") as file:
#     rf=file.readline()

#     while rf:
#         lst=rf.strip().split(' ')
#         data.append(lst)
#         print(rf)
#         rf=file.readline()
        
# total_h =0       
# max_h = 0
# name_h = ''
# for i in range(len(data)):
#     total_h += eval(data[i][1])
#     if eval(data[i][1]) >max_h:
#         max_h = eval(data[i][1])
#         name_h = data[i][0]


# total_w  =0      
# max_w = 0
# name_w = ''
# for i in range(len(data)):
#     total_w += eval(data[i][2])
#     if eval(data[i][2]) >max_w:
#         max_w = eval(data[i][2])
#         name_w = data[i][0]

# avg_h=total_h/len(data)    
# avg_w=total_w/len(data)     
    
# print('Average height: %.2f'% avg_h)
# print('Average weight: %.2f'% avg_w)
# print('The tallest is %s with %.2fcm'% (name_h,max_h))
# print('The heaviest is %s with %.2fkg'%(name_w,max_w))    
    
    
    
    




















    