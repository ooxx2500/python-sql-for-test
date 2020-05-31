# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
Week _:
Day _: 
Average: _
Highest: _
Lowest: _
"""


temp = []
for i in range(1,5):
    print('Week %d:' % i )
    temp.append([])
    for ii in range(1,4):
        
        n=eval(input('Day %d:' % ii))
        temp[i-1].append(n)
        
        
        
count=[]        
        
for i in range(4):
    count.extend(temp[i])

avg = sum(count)/len(count)
    
print('Average: %.2f' %avg)
print('Highest:',max(count))
print('Lowest:',min(count))


----------------------------------------
num_week = 4
num_day = 3
temp = []
for i in range(num_week):
    temp.append([])
    print('Week %d:' % (i+1))
    for j in range(num_day):
        temp[i].append(eval(input('Day %d:' % (j+1)))) 

comb = []
for i in range(num_week):
    comb.extend(temp[i])
    
avg = sum(comb) / (num_week * num_day)
print('Average: %.2f' % avg)
print('Highest:',max(comb))
print('Lowest:',min(comb))