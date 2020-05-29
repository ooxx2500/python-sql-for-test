# -*- coding: utf-8 -*-
"""
Created on Fri May 29 09:09:03 2020

@author: ASUS
"""
'''
702
2. 設計說明：
請撰寫一程式，輸入並建立兩組數組，各以-9999為結束點（數組中不包含-9999）。將此兩數組
合併並從小到大排序之，顯示排序前的數組和排序後的串列。

3. 輸入輸出：
輸入說明
兩個數組，直至-9999結束輸入

輸出說明
排序前的數組
排序後的串列

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
Create tuple1:
9
0
-1
3
8
-9999
Create tuple2:
28
16
39
56
78
88
-9999
Combined tuple before sorting: (9, 0, -1, 3, 8, 28, 16, 39, 56, 78, 88)
Combined list after sorting: [-1, 0, 3, 8, 9, 16, 28, 39, 56, 78, 88]
'''

tup1 = ()
tup2 = ()
print('Create tuple1:')
while True:
    num = eval(input())
    if num == -9999:
        break
    tup1 +=(num,) #將元組新增一個元素後面要逗點
    
print('Create tuple2:')
while True:
    num = eval(input())
    if num == -9999:
        break
    tup2 +=(num,)

tup_comb = tup1 +tup2

print('Combined tuple before sorting:',tup_comb)

lst_comb= list(tup_comb)

print('Combined list after sorting:',sorted(lst_comb))




'''
兩個數組可以用+號和成一個數組
數組內容不可以變更，通程可以轉為串列後再進行運算，如排序改位置
'''
a=[1,9,5,7]
sorted(a,reverse = True) #不會改變元串列
print(a)


'''
704
設計說明：
請撰寫一程式，輸入數個整數並儲存至集合，以輸入-9999為結束點（集合中不包含-9999），
最後顯示該集合的長度（Length）、最大值（Max）、最小值（Min）、總和（Sum）。

3. 輸入輸出：
輸入說明
輸入n個整數至集合，直至-9999結束輸入

輸出說明
集合的長度
集合中的最大值
集合中的最小值
集合內的整數總和

輸入輸出範例
範例輸入
34
-23
29
7
0
-1
-9999
範例輸出
Length: 6
Max: 34
Min: -23
Sum: 46
'''
num =set()
while True:
    inp = eval(input())
    if inp == -9999:
        break
    num.add(inp)

print('Length:',len(num))
print('Max:',max(num))
print('Min:',min(num))
print('Sum:',sum(num))


'''
706
設計說明：
全字母句（Pangram）是英文字母表所有的字母都出現至少一次（最好只出現一次）的句子。
請撰寫一程式，要求使用者輸入一正整數k（代表有k筆測試資料），每一筆測試資料為一句子，
程式判斷該句子是否為Pangram，並印出對應結果True（若是）或False（若不是）。

提示：不區分大小寫字母

3. 輸入輸出：
輸入說明
先輸入一個正整數表示測試資料筆數，再輸入測試資料

輸出說明
輸入的資料是否為全字母句

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示 第1組
3
The quick brown fox jumps over the lazy dog
True
Learning Python is funny
False
Pack my box with five dozen liquor jugs
True

輸入與輸出會交雜如下，輸出的部份以粗體字表示 第2組
2
Quick fox jumps nightly above wizard
True
These can be weapons of terror
False
'''
num_alph = 26
k = eval(input())

for i in range(k):
    sentence = input()
    alphabet = set(sentence.lower()) #將輸入放進集合,轉為小寫，集合內的元素不重複
    alphabet.remove(' ')    #移除空白字元remove()也可以使用discard()
    print(len(alphabet) == num_alph) #比較集合是否為26個英文字母

-------------------------------------------


a='asdasd'
b=set(a)
print(b)
c='momodax'
b=set(c)
print(b)
b.discard(' ')
print(b)
--------------------------------------------
'''
708
請撰寫一程式，自行輸入兩個詞典（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），將此兩詞典合併，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值。

3. 輸入輸出：
輸入說明
輸入兩個詞典，直至end結束輸入

輸出說明
合併兩詞典，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一
key值

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
Create dict1:
Key: a
Value: apple
Key: b
Value: banana
Key: d
Value: durian
Key: end
Create dict2:
Key: c
Value: cat
Key: e
Value: elephant
Key: end
a: apple
b: banana
c: cat
d: durian
e: elephant

程式執行狀況擷圖
下圖中的 粉紅色點 為 空格

Alt text
'''
def compute(): #建立字典函式
    dic = {}
    while True:
        key = input('Key: ')
        if key == 'end':
            return dic
        value = input('Value: ')
        dic[key]=value
        
print('Create dict1:')
dict1 = compute()

print('Create dict2:')
dict2 = compute()


merge_dict = dict1.copy()  #複製dict1給另一個辭典去更新dict2
merge_dict.update(dict2)

sortedDict = sorted(merge_dict) #用sorted()排序
for i in sortedDict:
    print('%s: %s' % (i, merge_dict[i]))



'''
710
設計說明：
請撰寫一程式，為一詞典輸入資料（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），再輸入一鍵值並檢視此鍵值是否存在於該詞典中。

3. 輸入輸出：
輸入說明
先輸入一個詞典，直至end結束輸入，再輸入一個鍵值進行搜尋是否存在

輸出說明
鍵值是否存在詞典中

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
Key: 123-4567-89
Value: Jennifer
Key: 987-6543-21
Value: Tommy
Key: 246-8246-82
Value: Kay
Key: end
Search key: 246-8246-82
True

'''

my_dict={}
while True:
    key = input("Key: ")
    if key == 'end':
        break
    value = input('Value: ')
    my_dict[key]=value
    
search_key = input('Search key: ')
print(search_key in my_dict)



















