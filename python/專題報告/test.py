# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:15:50 2020

@author: mona
"""
for i in range(len(data)): #統計區域事故人數
    address = data[i][1]
    district = address[0:3] #取出XX市

    for car in type_cars:
        if district not in area_dic: #取出XX市
            area_dic[district] = 1               
        else:
            area_dic[district] += 1  