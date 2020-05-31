# -*- coding: utf-8 -*-
"""
409
某次選舉有兩位候選人，分別是No.1: Nami、No.2: Chopper。請撰寫一程式，輸入五張選票，輸入值
如為1即表示針對1號候選人投票；輸入值如為2即表示針對2號候選人投票，如輸入其他值則視為廢票。每次投
完後需印出目前每位候選人的得票數，最後印出最高票者為當選人；如最終計算有相同的最高票數者或無法選出
最高票者，顯示【=> No one won the election.】。
3. 輸入輸出：
輸入說明

五個正整數（1、2或其他）
輸出說明

每次投完後需印出目前每位候選人的得票數
五張選票投票完成，最後印出最高票者為當選人
輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示

2
Total votes of No.1: Nami =  0
Total votes of No.2: Chopper =  1
Total null votes =  0
1
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  1
Total null votes =  0
8
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  1
Total null votes =  1
2
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  2
Total null votes =  1
2
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  3
Total null votes =  1
=> No.2 Chopper won the election.
"""
"""
Total votes of No.1: Nami = _
Total votes of No.2: Chopper = _
Total null votes = _

=> No.1 Nami won the election.
=> No.2 Chopper won the election.
=> No one won the election.
"""
no1=0
no2=0
nn=0


for i in range(5):
    n = eval(input())
    if n ==1:
        no1+=1
    elif n ==2:
        no2+=1
    else:
        nn+=1
    print('Total votes of No.1: Nami =  %d' % no1)
    print('Total votes of No.2: Chopper =  %d' % no2)
    print('Total null votes =  %d' % nn)
        
if no1>no2:
    print('=> No.1 Nami won the election.')
elif no1 <no2:        
    print('=> No.2 Chopper won the election.')  
else:
    print('=> No one won the election.')
        
        
        
        
        
        
        
        