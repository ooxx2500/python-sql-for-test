# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:54:59 2020

@author: 莫再提
"""


a=lambda x: x+1
print(a(5))


def a(x):
    return x+1
print(a(5))

#-------------------------------
#排列串列
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'C', 10)]
print(sorted(students, key=lambda s: s[2]))            # 按年龄排序
print(sorted(students, key=lambda y: y[2], reverse=True))       # 按降序
#[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(sorted(students, key=lambda s: s[1]))            # 按a b c 排
print(sorted(students, key=lambda y: y[1], reverse=True))  

#-------------------------------
#排列字典

dict1 = {'a':40,'b':50,'c':25,'d':45,"f":100}

print(dict1.items()) #用字典items()方法將字典分解為串列+元祖

dict1_sort=sorted(dict1.items(),key=lambda x:x[1])
print(dict1_sort)
dict1_sort=sorted(dict1.items(),key=lambda x:x[1],reverse=1)
print(dict1_sort)
#---------------------------------
#每個seris加減 用群組分類 apply
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.randint(1,20,size = (4,3)))
print(frame)


f = lambda x: x.max() - x.min()
print(frame.apply(f))
#--------------------------------------
#套用在每個項目要用applymap
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.randint(1,20,size = (4,3)))
print(frame)

print(frame.applymap(lambda x: x*100))


#-----------------------------------------
#map()只要是作用將函式作用於一個Series的每一個元素，用法如下所示


import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.randint(1,20,size = (4,3)),columns=list('abc'))
print(frame)

print(frame['c'].map(lambda x: x*100))














