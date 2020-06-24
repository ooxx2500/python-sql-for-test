# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 11:58:12 2020

@author: ooxx2
"""
from matplotlib import pyplot as plt
import csv

font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '8'}#設定字形樣式大小
plt.rc('font', **font) #設定PY繪圖系統的字型項目
plt.rc('axes',unicode_minus=False) #座標軸如果有負號再加上此參數就可解決



data=[]
with open(r'C:\Users\ASUS\Desktop\109A.csv','r',encoding = 'utf-8') \
    as csvfile:#用編碼utf8開啟
        plots = csv.reader(csvfile, delimiter = ',')#用reader方法讀取 plots是個串列
                              #用delimiter設定資料以逗號分隔字元，藉以取出每個資料
    
        for i in plots:
            data.append(i)
 
del data[0]
del data[-2:] #刪除表單的頭尾去除砸資料

new_data=[] 
area_dic=dict() #地區分類
date_dic=dict() #月份車禍
cars_dic=dict() #車量分類字典
scooter_dic=dict()#機車字典一個縣市計重複出現次數
scooter_area_dic=dict()#機車字典一個縣市只計一次
total_scooter=0
total_cards=0
total_not_cars=0  #非四輪車總數
for i in range(len(data)): #統計區域事故人數
    address = data[i][1]
    district = address[0:3] #取出XX市
    date = data[i][0]
    month_date =date[4:7]#取出年度月份
    year=date[0:4]
    
    if district not in area_dic:
        area_dic[district]=1
    else:
        area_dic[district] +=1
        
    if month_date not in date_dic: #月份的車禍數(無重複)
        date_dic[month_date]=1
    else:
        date_dic[month_date] +=1

    cars = data[i][3]    #找出所有的事故車
    type_cars = cars.split(';')
    for ii in type_cars:
        total_cards +=1
        if ii not in cars_dic:
            cars_dic[ii] = 1
        else:
            cars_dic[ii]+=1

    for car in type_cars:  #找出含機車的縣市(計算一次含機車的用BREAK)
        if '機車' in car:
           
            if district not in scooter_area_dic: #取出XX市
                scooter_area_dic[district] = 1
                break
                
            else:
                scooter_area_dic[district] += 1
                break

            
            
    for car in type_cars:  #找出含機車的縣市總數(包含重複值的)
        if '機車' in car:
            total_scooter+=1
           
            if district not in scooter_dic: #取出XX市
                scooter_dic[district] = 1
                
            else:
                scooter_dic[district] += 1
   
#print(scooter_area_dic)
print(scooter_dic)
#算出只含汽車的字典
                
only_cars=cars_dic.copy()#從總事故字典複製一份到only_cars
del_lst=[]
# print('******only_cars********')  
# print(only_cars)           
for i in only_cars:  #i就是車種
    
    if '機車' in i :
        total_not_cars+=only_cars[i]
        del_lst.append(i)
        
    elif '人'in i :
        total_not_cars+=only_cars[i]
        del_lst.append(i)
    elif '慢車'in i :
        total_not_cars+=only_cars[i]
        del_lst.append(i)
    elif '火車'in i :
        total_not_cars+=only_cars[i]
        del_lst.append(i)
        
        
for i in del_lst:     #從複製的字典中依序刪除其他車種
    del only_cars[i]
# print('******after del only_cars********')  
# print(only_cars) 
total_only_cars=total_cards-total_not_cars #總汽車數 = 所有車種數 - 所有非汽車數
total_other_cars=total_not_cars-total_scooter
# print(total_cards)
# print(total_scooter)   
# print(total_only_cars)
# print(total_other_cars)

def dict_list(x):#定義字典變2串列函式
    lst1=[]
    lst2=[]
    for i in x:
        lst1.append(i)
        lst2.append(x[i])
    return lst1 , lst2
    

    
#畫日期圖 (月份)   
dates , date_counts = dict_list(date_dic)
    
    
x=dates
y=date_counts
plt.bar(x,y,align='edge')#align='center' 直條對齊坐標刻度 align='edge' 對齊刻度邊緣

plt.title('各月份總事故-A1類')
plt.ylabel('總事故')
plt.xlabel(year)
plt.show()    
      
#---------------------------------------------------------------------------
    
#畫全車種地區圖


list_area_sort=sorted(area_dic.items(), key=lambda item:item[1],reverse=1)


list_scooter_sort=sorted(scooter_area_dic.items(), key=lambda item:item[1],reverse=1)

def list_to_2list(lst): #定義函式將column=2的串列轉為兩個串列
    lst1=[]
    lst2=[]
    for i in range(len(lst)):
        lst1.append(lst[i][0])
        lst2.append(lst[i][1])
    return lst1,lst2
        
    
areas , area_counts=list_to_2list(list_area_sort)

district_scooter , scooter_count=list_to_2list(list_scooter_sort)  


# print(list_area_sort)
# print('---------------------')
# print(list_scooter_sort)

   
    
x=areas
y=area_counts
plt.bar(x,y,align='edge',width=-0.5,color='#0080FF',label='全車種事故')#align='center' 直條對齊坐標刻度 align='edge' 對齊刻度邊緣

plt.title('**')
plt.ylabel('Y axis')
plt.xlabel('X axis')
            
#畫出重疊含機車的縣市      
    
x1=district_scooter
y1=scooter_count
plt.bar(x1,y1,align='edge',width=0.5,color='#FF5151',label='含機車事故')#align='center' 直條對齊坐標刻度 align='edge' 對齊刻度邊緣

plt.title('107年分區事故圖-A1類')
plt.ylabel('事故總數')
plt.xlabel('')
plt.xticks(rotation=45 ) #旋轉 Xticks 標籤文字 
plt.legend()

plt.show()     


#--------------------------------------


#劃出總事故比率圓餅圖(汽車 機車 及其他)


labels = ['車機','汽車','其他']
sizes=[total_scooter,total_only_cars,total_other_cars]
colors = ['red','green','y']
explode = (0.1,0,0) #0表示未分離 
plt.pie(sizes , explode = explode , labels=labels , colors = colors,
        labeldistance = 1.1 , autopct='%2.1f%%', shadow=True ,
        startangle = 45 , pctdistance = 0.5) #startangle 逆時針旋轉為正
plt.axis('equal')  
plt.title("107年總事故比率-A1類")       
plt.legend(loc = 'lower left',fontsize=12) 
plt.show()   

       
#-----------------


