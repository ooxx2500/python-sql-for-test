





import json

import pandas as pd

with open( r'C:\Users\莫再提\Desktop\63.json',encoding = 'utf8')as file:
    rf_1 = json.load(file)
       
rf=pd.DataFrame(rf_1)


# rf=rf.drop([0,369,370,371,372,373,374])

df=pd.DataFrame(rf_1)

aaa= df.loc[369:374].index  
print(aaa)
df.drop(aaa)
     
df=df.drop(0)

print(df)



new_column=pd.DataFrame()
new_column['縣市']=rf['site_id'].str[0:3].apply(lambda x:x[0:3])
rf2=pd.concat([rf,new_column], axis=1)
rf2['people_total']=rf2['people_total'].astype(int)
rf2['area']=rf2['area'].astype(float)

citis=set()
for i in rf2['縣市']:
    citis.add(i)
    

areas=[]
for i in citis:
    new=[]       
    mask=rf2['縣市']==i #mask=過濾器
    total_people=rf2[mask]['people_total'].sum()
    total_area=rf2[mask]['area'].sum()
    new.append(i)
    new.append(total_people)
    new.append(total_area)
    areas.append(new)
print(areas)



for i in areas:
    print(i)