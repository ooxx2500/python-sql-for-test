# -*- coding: utf-8 -*-
"""
902
設計說明：
請撰寫一程式，讀取read.txt的內容（內容為數字，以空白分隔）並將這些數字加總後輸出。
檔案讀取完成後要關閉。

3. 輸入輸出：
輸入說明
讀取read.txt的內容（內容為數字，以空白分隔）

輸出說明
總和

輸入輸出範例
範例輸入
無

範例輸出
660
"""

f = open(r'C:\Users\ASUS\Documents\Python-SQL\python\TQC+\9_txt\read902.txt','r')
data = f.read()  #讀取所有的文字檔
f.close()

num = data.split(' ') #用空白分開變成串列
total=0
for i in range(0,len(num)):
    total +=eval(num[i])
print(total)

'''
開啟檔案 open()
讀取檔案 read()
關閉檔案 close()

'''


'''
904
請撰寫一程式，讀取read.txt（每一列的格式為名字和身高、體重，以空白分隔）並顯示檔案
內容、所有人的平均身高、平均體重以及最高者、最重者。

提示：輸出浮點數到小數點後第二位。

3. 輸入輸出：
輸入說明
讀取read.txt（每一行的格式為名字和身高、體重，以空白分隔）

輸出說明
輸出檔案中的內容
平均身高
平均體重
最高者
最重者

輸入輸出範例
範例輸入
無

範例輸出
Ben 175 65

Cathy 155 55

Tony 172 75
Average height: 167.33
Average weight: 65.00
The tallest is Ben with 175.00cm
The heaviest is Tony with 75.00kg
'''
#%%
data=[]
with open(r'C:\Users\ASUS\Documents\Python-SQL\python\TQC+\9_txt\read904.txt' \
          ,'r')as file:
    for line in file: #印出每一行資料
        print(line)                     #字串.strip() 移除頭尾字元
        tmp = line.strip('\n').split(' ') #先除掉字串頭尾換行字元 並用空格字元分割
        tmp = [tmp[0],eval(tmp[1]),eval(tmp[2])] #將姓名 身高 體重只定給串列tmp
        data.append(tmp) #將串列加到data串列

name = [data[x][0]for x in range(len(data))]  #將data資料中的姓名取出來成一個串列
height = [data[x][1]for x in range(len(data))] #將data資料中的身高取出來成一個串列
weight = [data[x][2]for x in range(len(data))] #將data資料中的體重取出來成一個串列
#%%
print('Average height: %.2f'%(sum(height)/len(height)))
print('Average weight: %.2f'%(sum(weight)/len(weight)))

max_h = max(height)
max_w = max (weight)
print('The tallest is %s with %.2fcm' % (name[height.index(max_h)],max_h))
print('The heaviest is %s with %.2fkg' % (name[weight.index(max_w)],max_w))
                  #用身高最高的數值在該串列中的索引套用在姓名的索引，找出身高最高的姓名


'''
906
請撰寫一程式，要求使用者輸入檔名data.txt、字串s1和字串s2。程式將檔案中的字串s1以s2取代之。

3. 輸入輸出：
輸入說明
輸入data.txt及兩個字串（分別為s1、s2，字串s1被s2取代）

輸出說明
輸出檔案中的內容
輸出取代指定字串後的檔案內容

輸入輸出範例
範例輸入
data.txt
pen
sneakers
範例輸出
=== Before the replacement
watch shoes skirt
pen trunks pants
=== After the replacement
watch shoes skirt
sneakers trunks pants
'''
#%%
f_name = input()
str_old = input()
str_new = input()
#%%
infile = open(f_name,'r')
data = infile.read()

print('=== Before the replacement')
print(data)
infile.close()

print('=== After the replacement')
new_data = data.replace(str_old,str_new) #取代資料給NEWDATA
print(new_data)

outfile = open(f_name,'w')
outfile.write(new_data)
outfile.close()


'''
910
請撰寫一程式，要求使用者讀入read.dat（以UTF-8編碼格式讀取），第一列為欄位名稱，第二列之後
是個人記錄。請輸出檔案內容並顯示男生人數和女生人數（根據"性別"欄位，0為女性、1為男性）。

3. 輸入輸出：
輸入說明
讀取read.dat

輸出說明
讀取檔案內容，並格式化輸出男生人數和女生人數

輸入輸出範例
範例輸入
無

範例輸出
學號 姓名 性別 科系

101 陳小華 0 餐旅管理

202 李小安 1 廣告

303 張小威 1 英文

404 羅小美 0 法文

505 陳小凱 1 日文
Number of males: 3
Number of females: 2

'''
f_name = 'read.dat'
c_male = c_female =0

with open(f_name,'rb') as file:
    for line in file:
        row = line.decode('utf-8') 
        print(row)
        row = row.strip('\n').split(' ')
        
        if row[2]=='1':
            c_male +=1
        elif row[2] =='0':
            c_female +=1
print('Number of males:',c_male)
print('Number of females:',c_female)
            
'''
將檔案以二進位開啟並設定給變數file
用迴圈已utf-8格式讀取存入row變數
資料.decode(編碼格式)
去除row資料中的換行及用空格符號分割
row變數即為資料
row[0]:學號
row[1]:姓名
row[2]:性別
row[3]:科系
性別row[2]判斷是男是女 是的話就加1
'''        
        
        
'''
908
請撰寫一程式，要求使用者輸入檔名read.txt，以及檔案中某單字出現的次數。輸出符合次數的單字，並依單字的第一個字母大小排序。（單字的判斷以空白隔開即可）

3. 輸入輸出：
輸入說明
讀取read.txt的內容，以及檔案中某單字出現的次數

輸出說明
輸出符合次數的單字，並依單字的第一個字母大小排序

輸入輸出範例
範例輸入
read.txt
3
範例輸出
a
is
programming
'''
#908複雜解法
f_name = input()
n = int(input())
word_dict=dict() #建立空字典

with open(f_name,'r',encoding = 'UTF-8') as file:
    for line in file:
        word = line.strip('\n').split(' ')
        
        for x in word:
            if x in word_dict:
                word_dict[x]+=1 #如果字典中已經有單字了再加一次
            else:
                word_dict[x]=1      #單字第一次出現變成新KEY，VALUE從一開始
                
word_list = word_dict.items() #.items()傳回字典中所有的k:v  dict_items([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')])
wordQTY = [x for (x,y) in word_list if y ==n]#利用迴圈的數值作為終止值取出word_list
sortedword=sorted(wordQTY)                   #中的字詞wordQTY

for x in sortedword:
    print(x)

'''
908簡單解法
'''

fn = input() #read.txt
n =int(input()) #輸入次數
with open(fn,'r',encoding = 'UTF-8') as fp:#用UTF-8編碼開啟
    data = sorted(fp.read().split()) #將讀取的檔案內容以空白分割再排序
for i in sorted(set(data)):
    if data.count(i)==n: #求單字i在該字典出現的次數
        print(i)

-----------------------------
b={1:'a',2:'b',3:'c',4:'d',5:'e',6:'b'}
b.items()
print(b.items())
wordQTY = [x for (x,y) in b.items() if y == 'b']
print(wordQTY)



-----------------------------------

n =int(input()) #輸入次數
with open(r'C:\Users\ASUS\Documents\Python-SQL\python\TQC+\9_txt\read.txt','r',encoding = 'UTF-8') as fp:#用UTF-8編碼開啟
    data = sorted(fp.read().split()) #將讀取的檔案內容以空白分割再排序
    print(data)




