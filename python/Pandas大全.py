# -*- coding: utf-8 -*-
"""

"""


#Series物件的值是索引   
import pandas as pd

ss = pd.Series([5,10,15,20,25,30])
print(ss)
print(25 in ss)
print(0 in ss)
ss2 = pd.Series([6,10,15,20,25,30],index=[9,8,7,6,5,4])
print(10 in ss2)
print(4 in ss2)

---------------------------------

import pandas as pd
data={'name':['mona','judy'],'year':[1996,1997],'day':[10,20]}
mona in dara