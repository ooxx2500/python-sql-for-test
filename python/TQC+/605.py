# -*- coding: utf-8 -*-
"""
請撰寫一程式，讓使用者輸入十個成績，接下來將十個成績中最小和最大值（最小、最大值不重複）以外的成績
作加總及平均，並輸出結果。

    提示：平均值輸出到小數點後第二位。

3. 輸入輸出：
輸入說明

十個數字
輸出說明

總和
平均
輸入輸出範例
範例輸入

89
78
67
80
75
98
77
89
76
60

範例輸出

631
78.88

"""

s = []
for i in range(10):
    n=eval(input())
    s.append(n)

maxn=max(s)
minn=min(s) 
s.pop(s.index(maxn))
s.pop(s.index(minn))
print(sum(s))
print('%.2f' %(sum(s)/len(s)))   
