# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:11:27 2020

@author: ASUS
"""

'''
602
2. 設計說明：
請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。

提示：J、Q、K以及A分別代表11、12、13以及1。

3. 輸入輸出：
輸入說明
5張牌數

輸出說明
5張牌的數值總和

輸入輸出範例
範例輸入
5
10
K
3
A
範例輸出
32
'''
cards = []
result = 0
for i in range(5):
    cards.append(input())
for i in range(5):
    if cards[i] == 'A': result +=1
    elif cards[i] == 'J': result +=11
    elif cards[i] == 'Q': result +=12
    elif cards[i] == 'K': result +=13
    elif cards[i] == '10': result +=10
    else:
        result += eval(cards[i])
print(result)
    
    
    
'''
604
設計說明：
請撰寫一程式，讓使用者輸入十個整數作為樣本數，輸出眾數（樣本中出現最多次的數字）及其
出現的次數。

提示：假設樣本中只有一個眾數。

3. 輸入輸出：
輸入說明
十個整數

輸出說明
眾數
眾數出現的次數

輸入輸出範例
範例輸入
34
18
22
32
18
29
30
38
42
18
範例輸出
18
3 
'''

'''
設定樣本數size=10
設定儲存樣本數值的串列sample
設定計數器count
用迴圈加入10個數值
'''
size =10
sample = []
count = [0]*size #[0,0,0,0,0,0,0,0,0,0]

for i in range(size):
    num = int(input())
    sample.append(num)
    count[sample.index(num)] +=1  #回傳該數值第一次出現在該串列的索引 
    #如果所引是3 count[3] 
    
num_occu = max(count)
print(sample[count.index(num_occu)])#在count中出現最多次的，套回在sample中同
print(num_occu)                     #位置找回原本的值



-------------
s=[1,5,6,5,8,4,3,1,5,2,3]
#count[s.index(5)]
s[2]=s[2]+1
s[2]=10
print(s)


'''
606
2. 設計說明：
請撰寫一程式，讓使用者輸入兩個正整數rows、cols，分別表示二維串列lst 的「第一個維度大小」與「第二個維度大小」。
串列元素[row][col]所儲存的數字
，其規則為：row、col 的交點值 = 第二個維度的索引col – 第一個維度的索引row。
接著以該串列作為參數呼叫函式compute()輸出串列。

提示：欄寬為4。

3. 輸入輸出：
輸入說明
兩個正整數（rows、cols）

輸出說明
格式化輸出row、col的交點值

輸入輸出範例
範例輸入
5
10
範例輸出
   0   1   2   3   4   5   6   7   8   9   第0維度
  -1   0   1   2   3   4   5   6   7   8   第1維度
  -2  -1   0   1   2   3   4   5   6   7   第2維度
  -3  -2  -1   0   1   2   3   4   5   6   第3維度
  -4  -3  -2  -1   0   1   2   3   4   5   第4維度
'''
def compute(lst):    #主要印出來
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print('%4d' % lst[i][j], end='')
        print()

row = eval(input())
column = eval(input())
lst = []            #產生2維串列
for i in range(row):#第一維  
    lst.append([])
    for j in range(column):#第2維
        lst[i].append(j-i)

compute(lst)

#會建立[[0,1,2,3,4,5,6,7,8,9],[-1,0,1,2,3,4,5,6,7,8],[-2,-1,0,1,2,3,4,5,6,7]]
#以此類推
#在用函式印出來

'''
608
2. 設計說明：
請撰寫一程式，讓使用者建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引。

3. 輸入輸出：
輸入說明
九個整數

輸出說明
矩陣最大值及其索引
矩陣最小值及其索引

輸入輸出範例
範例輸入
6
4
8
39
12
3
-3
49
33
範例輸出
Index of the largest number 49 is: (2, 1)
Index of the smallest number -3 is: (2, 0)
'''

size = 3
mat = []

for i in range(size):#[[],[],[]]
    mat.append([])
    for j in range(size): #資料加近串列
        mat[i].append(eval(input()))
max_num = min_num =mat[0][0]
max_index = min_index = [0,0]　#另外設個起始串列0, 0
for i in range(size):
    for j in range(size):
        if mat[i][j] >max_num:     #用迴圈跑每個數值分別給最大最小
            max_num = mat[i][j]
            max_index = [i,j]
        elif mat[i][j] < min_num:
            min_num = mat[i][j]
            min_index = [i,j]
print('Index of the largest number %d is: (%d, %d)'\
      %(max_num,max_index[0],max_index[1]))
print('Index of the smallest number %d is: (%d, %d)'\
      %(min_num,min_index[0],min_index[1]))
  

'''
610
設計說明：
請撰寫一程式，讓使用者輸入四週各三天的溫度，接著計算並輸出這四週的平均溫度及最高、最低溫度。

提示1：平均溫度輸出到小數點後第二位。
提示2：最高溫度及最低溫度的輸出，如為31時，則輸出31，如為31.1時，則輸出31.1。

3. 輸入輸出：
輸入說明
四週各三天的溫度

輸出說明
平均溫度
最高溫度
最低溫度

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
下圖中的 粉紅色點 為 空格
'''

num_week = 4
num_day = 3
temp = []
for i in range(num_week):
    temp.append([])
    print('Week %d:' % (i+1))
    for j in range(num_day):
        temp[i].append(eval(input('Day %d:' % (j+1))))  #困難在這要輸出同一排

comb = []    #將串列合併成一條 extend
for i in range(num_week):
    comb.extend(temp[i])
#print(comb)
avg = sum(comb) / (num_week * num_day)
print('Average: %.2f' % avg)
print('Highest:',max(comb))
print('Lowest:',min(comb))




















    
    