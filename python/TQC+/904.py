# -*- coding: utf-8 -*-
"""
904
請撰寫一程式，讀取read.txt（每一列的格式為名字和身高、體重，以空白分隔）並顯示檔案
內容、所有人的平均身高、平均體重以及最高者、最重者。

提示：輸出浮點數到小數點後第二位。

3. 輸入輸出：
輸入說明
讀取read.txt（每一行的格式為名字和身高、體重，以空白分隔）

輸出說明
輸出檔案中的內容
平均身高
平均體重
最高者
最重者

輸入輸出範例
範例輸入
無

範例輸出
Ben 175 65

Cathy 155 55

Tony 172 75
Average height: 167.33
Average weight: 65.00
The tallest is Ben with 175.00cm
The heaviest is Tony with 75.00kg
"""

f = open(r'C:\Users\ASUS\Documents\Python-SQL\python\TQC+\9_txt\read904.txt','r')

a = f.readline()

lst=[]
while a!='':
    print(a)
    s= a.strip('\n')
    s=s.split(' ')
    lst.append(s)
    a = f.readline()

name = [lst[x][0] for x in range(3)]
h = [eval(lst[x][1]) for x in range(3)]
w = [eval(lst[x][2]) for x in range(3)]

hmax= max(h)
wmax = max(w)
avgh=sum(h)/len(h)
avgw=sum(w)/len(w)

hname = name[h.index(hmax)]
wname = name[w.index(wmax)]

print('Average height: %.2f' % avgh)
print('Average weight: %.2f' % avgw)
print('The tallest is %s with %.2fcm' % (hname , hmax))
print('The heaviest is %s with %.2fkg' % (wname , wmax))






