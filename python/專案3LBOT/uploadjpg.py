# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 23:04:22 2020

@author: 莫再提
"""


import numpy as np
import matplotlib.pyplot as plt
import pyimgur

from tkinter import *
import pymysql
import time
from datetime import *
import pandas as pd
import matplotlib.pyplot as plt


db = pymysql.connect( "Localhost"  ,'root' ,'1234' ,'test' ,charset='utf8')

sql="""SELECT date as '日期', SUM(price*quantity) as '銷售額'
FROM sell_list Where date between '{0}' and '{1}'
GROUP BY date""".format('2020-07-01','2020-07-31')
 
df=pd.read_sql(sql,con=db)
print(df)

