





import pandas as pd

path=r"C:\Users\莫再提\Desktop\109交通A.json"
df=pd.read_json(path)
df['發生地點']=df['發生地點'].str[0:3]
df['發生時間']=df['發生時間'].str[0:7]
df['車種']=df['車種'].str.split(';')


for i in df['車種']:
    for ii in i:
        df[ii]=None
df['車種']=df['車種'].astype(list)

for i in range(df['車種'].size):
    for ii in range(len(i)):
       
        print(df['車種'][i][ii])