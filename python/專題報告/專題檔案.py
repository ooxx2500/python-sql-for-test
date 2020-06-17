# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 11:58:12 2020

@author: ooxx2
"""
from matplotlib import pyplot as plt
import csv

font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '9'}#設定字形樣式大小
plt.rc('font', **font) #設定PY繪圖系統的字型項目
plt.rc('axes',unicode_minus=False) #座標軸如果有負號再加上此參數就可解決



data=[]
with open(r'C:\Users\莫再提\Documents\python-sql-for-test\python\專題報告\108年交通B.csv','r',encoding = 'utf8') \
    as csvfile:#用編碼utf8開啟
        plots = csv.reader(csvfile, delimiter = ',')#用reader方法讀取 plots是個串列
                              #用delimiter設定資料以逗號分隔字元，藉以取出每個資料
    
        for i in plots:
            data.append(i)

del data[0]
del data[-2:]

new_data=[] 
area_dic=dict() #地區分類
date_dic=dict() #月份車禍
cars_dic=dict() #車量分類字典
scooter_dic=dict()
for i in range(len(data)): #統計區域事故人數
    address = data[i][1]
    district = address[0:3] #取出XX市
    date = data[i][0]
    month_date =date[0:7]#取出年度月份
    
    if district not in area_dic:
        area_dic[district]=1
    else:
        area_dic[district] +=1
        
    if month_date not in date_dic:
        date_dic[month_date]=1
    else:
        date_dic[month_date] +=1

    cars = data[i][3]
    type_cars = cars.split(';')
    for ii in type_cars:
        if ii not in cars_dic:
            cars_dic[ii] = 1
        else:
            cars_dic[ii]+=1
            
    for car in type_cars:  #找出含機車的縣市總數
        if '機車' in car:
           
            if district not in scooter_dic:
                scooter_dic[district] = 1
                
            else:
                scooter_dic[district] += 1
            break #當找到機車就跳出該迴圈找下一組是否有機車 
print(area_dic)                
print(scooter_dic)                

# print(cars_dic)

# c = sorted(cars_dic.items(), key=lambda item:item[1]) #照字典的V排序   

# print(c)




        
# print(area_dic)
# print(date_dic)

# a = sorted(area_dic.items(), key=lambda item:item[1]) #照字典的V排序   

# print(a)

# print(a[0][0])

# b = sorted(date_dic.items(), key=lambda item:item[1]) #照字典的V排序   

# print(b)

# print(b[0][0])





def dict_list(x):#字典變2串列
    lst1=[]
    lst2=[]
    for i in x:
        lst1.append(i)
        lst2.append(x[i])
    return lst1 , lst2
    
#畫車種圖    
# carss , car_counts = dict_list(cars_dic)    
# print(cars_dic)    
    

# x=carss
# y=car_counts
# plt.bar(x,y,align='edge')#align='center' 直條對齊坐標刻度 align='edge' 對齊刻度邊緣

# plt.title('車種事故')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()    
    
    
# #畫日期圖    
# dates , date_counts = dict_list(date_dic)
    
    
# x=dates
# y=date_counts
# plt.bar(x,y,align='edge')#align='center' 直條對齊坐標刻度 align='edge' 對齊刻度邊緣

# plt.title('車種事故')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()    
      
#---------------------------------------------------------------------------
    
#畫全車種地區圖    
    
areas , area_counts = dict_list(area_dic)
    
    
x=areas
y=area_counts
plt.bar(x,y,align='edge',width=-0.5,color='b',label='全車種事故')#align='center' 直條對齊坐標刻度 align='edge' 對齊刻度邊緣

plt.title('車種事故')
plt.ylabel('Y axis')
plt.xlabel('X axis')
     
    
    
#畫出含機車的縣市     
    
    
district_scooter , scooter_count = dict_list(scooter_dic)  
    
x1=district_scooter
y1=scooter_count
plt.bar(x1,y1,align='edge',width=0.5,color='r',label='含機車事故')#align='center' 直條對齊坐標刻度 align='edge' 對齊刻度邊緣

plt.title('108年分區事故圖')
plt.ylabel('事故總數')
plt.xlabel('縣市')
plt.xticks(rotation=45 ) #旋轉 Xticks 標籤文字 
plt.legend()

plt.show()     



